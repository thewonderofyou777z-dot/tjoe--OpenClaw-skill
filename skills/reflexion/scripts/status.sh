#!/usr/bin/env bash
# reflexion/scripts/status.sh
# Dashboard showing learning stats, source/category breakdown, and recent entries.
set -euo pipefail

PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
REFLEX_DIR="$PROJECT_ROOT/.reflexion"

if [ ! -d "$REFLEX_DIR/entries" ]; then
  echo "No .reflexion/ directory found. Run init.sh or let capture.sh auto-initialize."
  exit 0
fi

# Use Python for comprehensive stats (handles JSON fields cleanly)
if command -v python3 &>/dev/null; then
  python3 << 'PYEOF'
import json, glob, os
from collections import Counter

entries = []
for f in sorted(glob.glob(os.path.expanduser('$REFLEX_DIR') + '/entries/RFX-*.json')):
    try:
        with open(f) as fp:
            entries.append(json.load(fp))
    except: pass

total = len(entries)
errors = sum(1 for e in entries if e.get('type') == 'error')
corrections = sum(1 for e in entries if e.get('type') == 'correction')
insights = sum(1 for e in entries if e.get('type') == 'insight')
patterns = sum(1 for e in entries if e.get('type') == 'pattern')
promoted = sum(1 for e in entries if e.get('promoted'))
resolved = sum(1 for e in entries if e.get('resolution', '').strip())
unresolved = total - resolved - promoted
if unresolved < 0: unresolved = 0

# Source breakdown
sources = Counter(e.get('source', 'unknown') for e in entries)

# Category breakdown
categories = Counter(e.get('category', 'bug-fix') for e in entries)

# Stats
stats = {}
if os.path.exists('$REFLEX_DIR/stats.json'):
    try:
        with open('$REFLEX_DIR/stats.json') as f:
            stats = json.load(f)
    except: pass

# Promotion candidates
candidates = [e for e in entries if not e.get('promoted') and e.get('occurrences', 1) >= 2 and e.get('resolution', '').strip()]
hot_unresolved = [e for e in entries if not e.get('resolution', '').strip() and e.get('occurrences', 1) >= 2]

# Keywords count
kw_count = 0
if os.path.exists('$REFLEX_DIR/index.txt'):
    with open('$REFLEX_DIR/index.txt') as f:
        kw_count = len(f.read().strip().splitlines())

# Recent entries
recent = sorted(entries, key=lambda e: e.get('last_seen', ''), reverse=True)[:5]

print()
print("  ╔══════════════════════════════════════════════════╗")
print("  ║           reflexion status dashboard              ║")
print("  ╠══════════════════════════════════════════════════╣")
print(f"  ║  Entries:  {total} total")
print(f"  ║    errors: {errors}  corrections: {corrections}  insights: {insights}  patterns: {patterns}")
print(f"  ║    resolved: {resolved}  unresolved: {unresolved}  promoted: {promoted}")
print(f"  ║")
print(f"  ║  Index:    {kw_count} keywords")
print(f"  ║")
print("  ║  Sources:                                          ║")
for src, cnt in sources.most_common(5):
    bar = '█' * min(cnt, 20)
    print(f"  ║    {src:20s} {bar} ({cnt})")
print("  ║")
print("  ║  Categories:                                      ║")
for cat, cnt in categories.most_common(5):
    bar = '█' * min(cnt, 20)
    print(f"  ║    {cat:20s} {bar} ({cnt})")
print(f"  ║")
print(f"  ║  Activity:                                        ║")
tc = stats.get('total_captured', 0)
tr_ = stats.get('total_recalled', 0)
tp_ = stats.get('total_promoted', 0)
lc = stats.get('last_capture', 'never')
lr = stats.get('last_recall', 'never')
print(f"  ║    captures:   {tc} (last: {lc})")
print(f"  ║    recalls:    {tr_} (last: {lr})")
print(f"  ║    promotions: {tp_}")
print(f"  ║")
print(f"  ║  Promotion candidates (2+ occurrences): {len(candidates)}")
print("  ╚══════════════════════════════════════════════════╝")
print()

if hot_unresolved:
    print("  Hot unresolved (recurring, no fix yet):")
    for e in hot_unresolved[:3]:
        print(f"    [{e['id']}] {e.get('type','error')} (x{e.get('occurrences',1)}): {e.get('trigger','')[:70]}")
    print()

print("  Recent entries:")
for e in recent:
    status = 'promoted' if e.get('promoted') else ('resolved' if e.get('resolution', '').strip() else 'open')
    src = e.get('source', '-')
    cat = e.get('category', '-')
    print(f"    [{e['id']}] {e.get('type','?'):10s} {status:8s} src:{src:18s} cat:{cat} (x{e.get('occurrences',1)}) {e.get('trigger','')[:50]}")
print()
PYEOF
else
  # Fallback: basic grep-based output
  TOTAL="$(find "$REFLEX_DIR/entries" -name 'RFX-*.json' 2>/dev/null | wc -l | tr -d ' ')"
  ERRORS="$(grep -rl '"type".*"error"' "$REFLEX_DIR/entries/" 2>/dev/null | wc -l | tr -d ' ')"
  CORRECTIONS="$(grep -rl '"type".*"correction"' "$REFLEX_DIR/entries/" 2>/dev/null | wc -l | tr -d ' ')"
  INSIGHTS="$(grep -rl '"type".*"insight"' "$REFLEX_DIR/entries/" 2>/dev/null | wc -l | tr -d ' ')"
  PATTERNS="$(grep -rl '"type".*"pattern"' "$REFLEX_DIR/entries/" 2>/dev/null | wc -l | tr -d ' ')"
  echo "  Basic stats (install python3 for full dashboard):"
  echo "    $TOTAL total: $ERRORS errors, $CORRECTIONS corrections, $INSIGHTS insights, $PATTERNS patterns"
fi
