#!/bin/bash
# Convert PDF or EPUB to Markdown (with caching)
# Usage: ./convert-to-md.sh <file_path> [output_dir]
#
# Detects file type by extension:
#   .pdf  → docling
#   .epub → pandoc
#
# If output_dir is provided, writes markdown there; otherwise same folder as input.
# If markdown already exists, skips conversion and returns existing file.

set -e

FILE_PATH="$1"
OUTPUT_DIR="$2"

if [ -z "$FILE_PATH" ]; then
    echo "Usage: $0 <file_path> [output_dir]"
    echo "Supports: .pdf (via docling), .epub (via pandoc)"
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File not found: $FILE_PATH"
    exit 1
fi

# Determine output location
FILE_DIR=$(dirname "$FILE_PATH")
FILENAME=$(basename "$FILE_PATH")
EXT="${FILENAME##*.}"
BASENAME="${FILENAME%.*}"

if [ -n "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
    MD_FILE="$OUTPUT_DIR/$BASENAME.md"
else
    MD_FILE="$FILE_DIR/$BASENAME.md"
fi

# Check if markdown already exists (cache hit)
if [ -f "$MD_FILE" ]; then
    echo "$MD_FILE"
    exit 0
fi

# Convert based on file type
case "$EXT" in
    pdf|PDF)
        docling "$FILE_PATH" \
            --to md \
            --image-export-mode placeholder \
            --output "$(dirname "$MD_FILE")" 2>/dev/null
        ;;
    epub|EPUB)
        pandoc -f epub -t markdown --wrap=none "$FILE_PATH" -o "$MD_FILE" 2>/dev/null
        ;;
    *)
        echo "Error: Unsupported file type: .$EXT (expected .pdf or .epub)"
        exit 1
        ;;
esac

# Verify output
if [ -f "$MD_FILE" ]; then
    echo "$MD_FILE"
else
    echo "Error: Markdown file not created"
    exit 1
fi
