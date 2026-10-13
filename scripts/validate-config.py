#!/usr/bin/env python3
"""Check JSON syntax and required LinkRouter rule fields."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "linkrouter-template.json"
config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CONFIG
try:
    data = json.loads(config_path.read_text(encoding="utf-8-sig"))
except FileNotFoundError:
    print(f"ERROR: file not found: {config_path}", file=sys.stderr)
    raise SystemExit(2)
except json.JSONDecodeError as exc:
    print(f"ERROR: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}", file=sys.stderr)
    raise SystemExit(1)

if not isinstance(data, dict) or not isinstance(data.get("rules"), list):
    print("ERROR: expected a JSON object with a 'rules' array", file=sys.stderr)
    raise SystemExit(1)

for index, rule in enumerate(data["rules"], start=1):
    for field in ("regex", "program", "arguments"):
        if not isinstance(rule.get(field), str):
            print(f"ERROR: rule {index} is missing a string '{field}' field", file=sys.stderr)
            raise SystemExit(1)
    try:
        re.compile(rule["regex"])
    except re.error as exc:
        print(f"ERROR: rule {index} has a regex Python cannot compile: {exc}", file=sys.stderr)
        raise SystemExit(1)

print(f"Valid JSON structure: {config_path}")
print(f"Rules: {len(data['rules'])}")
print("Required fields and regex syntax checks passed.")
if any(token in config_path.read_text(encoding="utf-8-sig") for token in ("YOUR_CHROME_PROFILE_DIRECTORY", "YOUR_YOUTUBE_PWA_APP_ID", "PATH\\\\TO\\\\CHROME")):
    print("NOTE: This appears to be a template; replace its placeholders before using it.")
