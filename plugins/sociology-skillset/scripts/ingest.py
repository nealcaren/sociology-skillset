#!/usr/bin/env python3
"""Ingest a PDF or EPUB into the local library.

Copies the file to library/pdfs/, converts to markdown in library/markdown/,
fetches metadata from Crossref/Open Library, generates a citation key,
and appends an entry to references.bib.

Usage:
    python ingest.py --file paper.pdf
    python ingest.py --file paper.pdf --doi 10.1177/00031224231150000
    python ingest.py --file book.epub --title "Book Title" --author "Smith" --year 2023
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request


POLITE_EMAIL = "research-tools@example.com"
CROSSREF_BASE = "https://api.crossref.org/works/"
OPENLIBRARY_BASE = "https://openlibrary.org/isbn/"
SUPPORTED_EXTENSIONS = {".pdf", ".epub"}


# ---------------------------------------------------------------------------
# Metadata fetching
# ---------------------------------------------------------------------------

def _api_get(url):
    """GET with polite User-Agent header."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"ResearchTools/1.0 (mailto:{POLITE_EMAIL})"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError):
        return None


def fetch_crossref(doi):
    """Fetch metadata from Crossref by DOI."""
    data = _api_get(f"{CROSSREF_BASE}{doi}")
    if not data or "message" not in data:
        return None
    msg = data["message"]
    authors = []
    for a in msg.get("author", []):
        given = a.get("given", "")
        family = a.get("family", "")
        authors.append({"given": given, "family": family})
    title_parts = msg.get("title", [])
    title = title_parts[0] if title_parts else ""
    date_parts = msg.get("published-print", msg.get("published-online", {}))
    year = ""
    if date_parts and date_parts.get("date-parts"):
        year = str(date_parts["date-parts"][0][0])
    container = msg.get("container-title", [])
    journal = container[0] if container else ""
    volume = msg.get("volume", "")
    issue = msg.get("issue", "")
    pages = msg.get("page", "")
    entry_type = "article"
    if msg.get("type") in ("book", "monograph", "edited-book"):
        entry_type = "book"
    return {
        "type": entry_type,
        "authors": authors,
        "title": title,
        "year": year,
        "journal": journal,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "doi": doi,
    }


def fetch_openlibrary(isbn):
    """Fetch metadata from Open Library by ISBN."""
    data = _api_get(f"{OPENLIBRARY_BASE}{isbn}.json")
    if not data:
        return None
    title = data.get("title", "")
    authors = []
    for a in data.get("authors", []):
        name = a.get("name", "")
        parts = name.rsplit(" ", 1)
        if len(parts) == 2:
            authors.append({"given": parts[0], "family": parts[1]})
        else:
            authors.append({"given": "", "family": name})
    year = data.get("publish_date", "")
    if year:
        # Extract 4-digit year
        m = re.search(r"\d{4}", year)
        year = m.group(0) if m else year
    return {
        "type": "book",
        "authors": authors,
        "title": title,
        "year": year,
        "journal": "",
        "volume": "",
        "issue": "",
        "pages": "",
        "doi": "",
        "isbn": isbn,
    }


# ---------------------------------------------------------------------------
# DOI / ISBN extraction from text
# ---------------------------------------------------------------------------

_DOI_RE = re.compile(r"10\.\d{4,}/[^\s,;\"'}\]]+")
_ISBN_RE = re.compile(r"(?:ISBN[:\s-]*)?(\d{13}|\d{10})", re.IGNORECASE)


def extract_doi(text):
    """Extract first DOI from text."""
    m = _DOI_RE.search(text)
    return m.group(0).rstrip(".") if m else None


def extract_isbn(text):
    """Extract first ISBN from text."""
    m = _ISBN_RE.search(text)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Citation key generation (BBT-compatible)
# ---------------------------------------------------------------------------

def _sanitize(s):
    """Remove non-alphanumeric characters."""
    return re.sub(r"[^a-zA-Z0-9]", "", s)


def generate_citekey(authors, year, title):
    """Generate a BetterBibTeX-style citation key: AuthorYear_firstword."""
    if authors:
        family = authors[0].get("family", "Unknown")
    else:
        family = "Unknown"
    family = _sanitize(family)
    year = str(year) if year else "XXXX"
    # First significant word of title (skip articles)
    skip = {"a", "an", "the", "on", "in", "of", "for", "and", "to"}
    words = re.findall(r"[a-zA-Z]+", title or "untitled")
    first_word = "untitled"
    for w in words:
        if w.lower() not in skip:
            first_word = w.capitalize()
            break
    return f"{family}{year}_{first_word}"


# ---------------------------------------------------------------------------
# BibTeX writing
# ---------------------------------------------------------------------------

def make_bib_entry(meta, citekey, pdf_rel, md_rel):
    """Create a BibTeX entry string."""
    if meta["type"] == "book":
        entry_type = "book"
    else:
        entry_type = "article"

    authors_str = " and ".join(
        f"{a['family']}, {a['given']}" for a in meta.get("authors", [])
    )
    lines = [f"@{entry_type}{{{citekey},"]
    lines.append(f"  author = {{{authors_str}}},")
    lines.append(f"  title = {{{meta.get('title', '')}}},")
    lines.append(f"  year = {{{meta.get('year', '')}}},")
    if meta.get("journal"):
        lines.append(f"  journal = {{{meta['journal']}}},")
    if meta.get("volume"):
        lines.append(f"  volume = {{{meta['volume']}}},")
    if meta.get("issue"):
        lines.append(f"  number = {{{meta['issue']}}},")
    if meta.get("pages"):
        lines.append(f"  pages = {{{meta['pages']}}},")
    if meta.get("doi"):
        lines.append(f"  doi = {{{meta['doi']}}},")
    if meta.get("isbn"):
        lines.append(f"  isbn = {{{meta['isbn']}}},")
    lines.append(f"  pdf_path = {{{pdf_rel}}},")
    lines.append(f"  md_path = {{{md_rel}}},")
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File conversion
# ---------------------------------------------------------------------------

def convert_to_markdown(file_path, md_dir):
    """Convert a PDF or EPUB to markdown."""
    basename = os.path.splitext(os.path.basename(file_path))[0]
    md_path = os.path.join(md_dir, basename + ".md")
    if os.path.exists(md_path):
        return md_path

    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".pdf":
            subprocess.run(
                ["docling", file_path, "--to", "md",
                 "--image-export-mode", "placeholder",
                 "--output", md_dir],
                check=True, capture_output=True,
            )
        elif ext == ".epub":
            subprocess.run(
                ["pandoc", "-f", "epub", "-t", "markdown",
                 "--wrap=none", file_path, "-o", md_path],
                check=True, capture_output=True,
            )
    except FileNotFoundError as e:
        print(f"Error: converter not found: {e.filename}")
        print("Install docling (for PDFs) or pandoc (for EPUBs).")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: conversion failed: {e}")
        sys.exit(1)

    return md_path if os.path.exists(md_path) else None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Ingest a PDF or EPUB into the local library."
    )
    parser.add_argument("--file", required=True, help="Path to PDF or EPUB")
    parser.add_argument("--doi", default=None, help="DOI for metadata lookup")
    parser.add_argument("--isbn", default=None, help="ISBN for book metadata lookup")
    parser.add_argument("--title", default=None, help="Manual title override")
    parser.add_argument("--author", default=None, help="Manual author override (Family, Given)")
    parser.add_argument("--year", default=None, help="Manual year override")
    parser.add_argument("--citekey", default=None, help="Manual citation key override")
    args = parser.parse_args()

    file_path = os.path.abspath(args.file)
    ext = os.path.splitext(file_path)[1].lower()

    if ext not in SUPPORTED_EXTENSIONS:
        print(f"Error: Unsupported file type: {ext} (expected .pdf or .epub)")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    # Setup directories
    pdf_dir = os.path.join(".", "library", "pdfs")
    md_dir = os.path.join(".", "library", "markdown")
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(md_dir, exist_ok=True)

    # Copy file to library
    dest_basename = os.path.basename(file_path)
    dest = os.path.join(pdf_dir, dest_basename)
    if not os.path.exists(dest):
        shutil.copy2(file_path, dest)
    print(f"File: {dest}")

    # Convert to markdown
    md_path = convert_to_markdown(dest, md_dir)
    if md_path:
        print(f"Markdown: {md_path}")
        md_text = open(md_path, "r", encoding="utf-8", errors="replace").read()
    else:
        print("Warning: Markdown conversion failed")
        md_text = ""

    # Resolve metadata
    doi = args.doi
    isbn = args.isbn

    # Try extracting DOI/ISBN from text if not provided
    if not doi and md_text:
        doi = extract_doi(md_text)
        if doi:
            print(f"Extracted DOI: {doi}")
    if not isbn and not doi and md_text:
        isbn = extract_isbn(md_text)
        if isbn:
            print(f"Extracted ISBN: {isbn}")

    meta = None
    if doi:
        print(f"Fetching metadata from Crossref...")
        meta = fetch_crossref(doi)
    if not meta and isbn:
        print(f"Fetching metadata from Open Library...")
        meta = fetch_openlibrary(isbn)

    # Fall back to manual / filename-based metadata
    if not meta:
        if doi or isbn:
            print("Warning: API lookup returned no results, using manual metadata")
        meta = {
            "type": "article",
            "authors": [],
            "title": args.title or os.path.splitext(os.path.basename(file_path))[0],
            "year": args.year or "",
            "journal": "",
            "volume": "",
            "issue": "",
            "pages": "",
            "doi": doi or "",
        }

    # Apply manual overrides
    if args.title:
        meta["title"] = args.title
    if args.author:
        parts = args.author.split(",", 1)
        family = parts[0].strip()
        given = parts[1].strip() if len(parts) > 1 else ""
        meta["authors"] = [{"given": given, "family": family}]
    if args.year:
        meta["year"] = args.year

    # Generate citation key
    citekey = args.citekey or generate_citekey(
        meta.get("authors", []), meta.get("year"), meta.get("title")
    )

    # Rename files to use citekey
    citekey_dest = os.path.join(pdf_dir, citekey + ext)
    if dest != citekey_dest and not os.path.exists(citekey_dest):
        os.rename(dest, citekey_dest)
    citekey_md = os.path.join(md_dir, citekey + ".md")
    if md_path and md_path != citekey_md and not os.path.exists(citekey_md):
        os.rename(md_path, citekey_md)

    pdf_rel = f"library/pdfs/{citekey}{ext}"
    md_rel = f"library/markdown/{citekey}.md" if md_path else ""

    # Append to references.bib
    bib_entry = make_bib_entry(meta, citekey, pdf_rel, md_rel)
    bib_path = os.path.join(".", "references.bib")

    # Check for duplicate citekey
    if os.path.exists(bib_path):
        existing = open(bib_path, "r", encoding="utf-8").read()
        if f"{{{citekey}," in existing:
            print(f"\nWarning: Citation key '{citekey}' already exists in references.bib")
            print("Entry NOT appended. Use --citekey to specify a different key.")
            sys.exit(0)

    with open(bib_path, "a", encoding="utf-8") as f:
        f.write("\n" + bib_entry + "\n")

    print(f"\nAdded to references.bib:")
    print(f"  Key:    {citekey}")
    print(f"  Title:  {meta.get('title', 'N/A')}")
    if meta.get("authors"):
        print(f"  Author: {meta['authors'][0].get('family', 'N/A')}")
    print(f"  Year:   {meta.get('year', 'N/A')}")


if __name__ == "__main__":
    main()
