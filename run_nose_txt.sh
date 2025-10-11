#!/usr/bin/env bash
# =============================================================================
# Script: run_nose_txt.sh
# Purpose: Run nosetests, capture full output (stdout + stderr) into timestamped text log.
# =============================================================================

set -euo pipefail

REPORT_DIR="reports"
TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')
REPORT_FILE="${REPORT_DIR}/nosetests_${TIMESTAMP}.txt"

echo "📦 Starting nosetests (text log mode)..."
echo "→ Report directory: ${REPORT_DIR}"
echo "→ Report file: ${REPORT_FILE}"

if ! mkdir -p "$REPORT_DIR"; then
  echo "❌ Failed to create report directory: $REPORT_DIR" >&2
  exit 1
fi

# Run tests, output both stdout and stderr into file
if nosetests -s >"$REPORT_FILE" 2>&1; then
  echo "✅ Tests completed successfully."
else
  echo "⚠️  Tests failed (non-zero exit code). See details: $REPORT_FILE" >&2
  exit 2
fi

echo "📄 Log saved: $REPORT_FILE"
exit 0
