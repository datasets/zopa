## Update Script Maintenance Report

Date: 2026-03-04

- Ran updater: `python data.py`.
- Root cause: legacy script depended on unavailable `datautil` package and obsolete environment assumptions.
- Fixes made:
  - Replaced updater with a minimal `requests`-based fetch path and added `requirements.txt`.
  - Added first scheduled/manual workflow with explicit `contents: write`.
- Validation summary: script now executes with modern dependencies; upstream `uk.zopa.com` endpoint currently fails DNS resolution and blocks data refresh.
