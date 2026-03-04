#!/usr/bin/env python3
"""Migrate an exported Zotero BibTeX library to the local library structure.

Copies PDFs/EPUBs to library/pdfs/, converts them to markdown in library/markdown/,
and rewrites BibTeX entries with pdf_path and md_path fields.

Usage:
    python migrate-zotero.py --bib exported.bib --files /path/to/attachments --output-dir /path/to/project
"""

import argparse
import os
import re
import shutil
import subprocess
import sys


# ---------------------------------------------------------------------------
# Minimal regex-based BibTeX parser (stdlib only)
# ---------------------------------------------------------------------------

_ENTRY_RE = re.compile(
    r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE
)
_FIELD_RE = re.compile(
    r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", re.IGNORECASE
)


def parse_bib(text):
    """Return a list of dicts with 'entry_type', 'key', and field values."""
    entries = []
    # Split on top-level @type{ patterns
    raw_entries = re.split(r"(?=@\w+\s*\{)", text)
    for raw in raw_entries:
        raw = raw.strip()
        if not raw:
            continue
        m = _ENTRY_RE.match(raw)
        if not m:
            continue
        entry = {
            "_entry_type": m.group(1).lower(),
            "_key": m.group(2),
        }
        for fm in _FIELD_RE.finditer(raw):
            entry[fm.group(1).lower()] = fm.group(2).strip()
        entries.append(entry)
    return entries


def entry_to_bib(entry):
    """Serialize an entry dict back to BibTeX."""
    lines = [f"@{entry['_entry_type']}{{{entry['_key']},"]
    skip = {"_entry_type", "_key"}
    for k, v in entry.items():
        if k in skip:
            continue
        lines.append(f"  {k} = {{{v}}},")
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File handling
# ---------------------------------------------------------------------------

SUPPORTED_EXTENSIONS = {".pdf", ".epub"}


def find_attachment(files_dir, citekey):
    """Try to locate a PDF or EPUB for a given citekey in files_dir."""
    if not files_dir or not os.path.isdir(files_dir):
        return None
    # Try exact citekey match first
    for ext in SUPPORTED_EXTENSIONS:
        candidate = os.path.join(files_dir, citekey + ext)
        if os.path.isfile(candidate):
            return candidate
    # Search subdirectories (Zotero storage uses key-based folders)
    for root, _dirs, filenames in os.walk(files_dir):
        for fn in filenames:
            _, ext = os.path.splitext(fn)
            if ext.lower() in SUPPORTED_EXTENSIONS:
                return os.path.join(root, fn)
    return None


def convert_to_markdown(file_path, md_dir):
    """Convert a PDF or EPUB to markdown, return output path."""
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
        print(f"  Warning: converter not found ({e.filename}), skipping {file_path}")
        return None
    except subprocess.CalledProcessError as e:
        print(f"  Warning: conversion failed for {file_path}: {e}")
        return None

    return md_path if os.path.exists(md_path) else None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Migrate a Zotero-exported BibTeX library to a local library structure."
    )
    parser.add_argument("--bib", required=True, help="Path to exported .bib file")
    parser.add_argument("--files", default=None,
                        help="Directory containing PDF/EPUB attachments")
    parser.add_argument("--output-dir", required=True,
                        help="Project directory (will create library/ and references.bib)")
    args = parser.parse_args()

    # Read input bib
    with open(args.bib, "r", encoding="utf-8") as f:
        bib_text = f.read()

    entries = parse_bib(bib_text)
    if not entries:
        print("No BibTeX entries found.")
        sys.exit(1)

    print(f"Found {len(entries)} entries in {args.bib}")

    # Create output directories
    pdf_dir = os.path.join(args.output_dir, "library", "pdfs")
    md_dir = os.path.join(args.output_dir, "library", "markdown")
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(md_dir, exist_ok=True)

    migrated = 0
    for entry in entries:
        citekey = entry["_key"]

        # Try to find and copy attachment
        attachment = find_attachment(args.files, citekey) if args.files else None
        if attachment:
            ext = os.path.splitext(attachment)[1].lower()
            dest = os.path.join(pdf_dir, citekey + ext)
            if not os.path.exists(dest):
                shutil.copy2(attachment, dest)
            entry["pdf_path"] = f"library/pdfs/{citekey}{ext}"

            # Convert to markdown
            md_path = convert_to_markdown(dest, md_dir)
            if md_path:
                entry["md_path"] = f"library/markdown/{citekey}.md"
                migrated += 1
                print(f"  ✓ {citekey}")
            else:
                print(f"  ~ {citekey} (copied, conversion failed)")
        else:
            entry["pdf_path"] = ""
            entry["md_path"] = ""

    # Write output references.bib
    out_bib = os.path.join(args.output_dir, "references.bib")
    with open(out_bib, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(entry_to_bib(entry))
            f.write("\n\n")

    print(f"\nDone: {len(entries)} entries → {out_bib}")
    print(f"  {migrated} files converted to markdown")
    print(f"  PDFs/EPUBs in: {pdf_dir}")
    print(f"  Markdown in:   {md_dir}")


if __name__ == "__main__":
    main()
