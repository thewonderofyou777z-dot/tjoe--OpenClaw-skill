#!/usr/bin/env bash
# reflexion/scripts/export.sh
# Export learnings to JSON for sharing or backup.
set -euo pipefail

PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
REFLEX_DIR="$PROJECT_ROOT/.reflexion"
OUTPUT_FILE="${1:-.reflexion/export.json}"

if [ ! -d "$REFLEX_DIR/entries" ]; then
  echo "No .reflexion/ directory found."
  exit 1
fi

EXPORT_TIME="$(date -Iseconds)"
TOTAL="$(find "$REFLEX_DIR/entries" -name 'RFX-*.json' 2>/dev/null | wc -l | tr -d ' ')"

# Build export
python3 -c "
import json, os, glob
from datetime import datetime

entries = []
for f in sorted(glob.glob('$REFLEX_DIR/entries/RFX-*.json')):
    try:
        with open(f) as fp:
            e = json.load(fp)
            entries.append(e)
    except: pass

export = {
    'export_time': '$EXPORT_TIME',
    'total_entries': len(entries),
    'entries': entries
}

with open('$OUTPUT_FILE', 'w') as f:
    json.dump(export, f, ensure_ascii=False, indent=2)

print(f'Exported {len(entries)} entries to $OUTPUT_FILE')
" 2>/dev/null || echo "Export failed (python3 required)"
