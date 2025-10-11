#!/usr/bin/env bash
# =============================================================================
# Script: run_nose_xml.sh
# Purpose: Run nosetests and export XML report with timestamped filename.
# =============================================================================

set -euo pipefail  # safer bash mode: stop on error, unset vars, pipe fails

REPORT_DIR="reports"
TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')
REPORT_FILE="${REPORT_DIR}/nosetests_${TIMESTAMP}.xml"

echo "📦 Starting nosetests (XML report mode)..."
echo "→ Report directory: ${REPORT_DIR}"
echo "→ Report file: ${REPORT_FILE}"

# Create report directory if missing
if ! mkdir -p "$REPORT_DIR"; then
  echo "❌ Failed to create report directory: $REPORT_DIR" >&2
  exit 1
fi

# Run tests and capture result
if nosetests --with-xunit --xunit-file="$REPORT_FILE"; then
  echo "✅ Tests completed successfully."
else
  echo "⚠️  Tests failed (non-zero exit code). Check XML report: $REPORT_FILE" >&2
  exit 2
fi

echo "📄 Report saved: $REPORT_FILE"
exit 0
