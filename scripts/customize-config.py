#!/usr/bin/env python3
"""Create a local LinkRouter config from config/linkrouter-template.json."""
import json
from pathlib import Path, PureWindowsPath

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "config" / "linkrouter-template.json"
DEFAULT_OUTPUT = ROOT / "config" / "linkrouter.local.json"


def required(prompt_text: str) -> str:
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Please enter a value; it cannot be blank.")


def main() -> None:
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Could not read valid source template: {exc}")

    print("This creates a local copy and leaves config\\linkrouter-template.json unchanged.")
    app_id = required("YouTube PWA app ID (from the shortcut's Target): ")
    profile = required("Chrome profile directory (for example, Default or Profile 1): ")
    default_app_dir = r"C:\Program Files\Google\Chrome\Application"
    app_dir_text = input(f"Chrome Application folder [{default_app_dir}]: ").strip()
    app_dir = app_dir_text or default_app_dir
    output_text = input(f"Output file [{DEFAULT_OUTPUT}]: ").strip()
    output = Path(output_text) if output_text else DEFAULT_OUTPUT
    if not output.is_absolute():
        output = ROOT / output

    win_app_dir = PureWindowsPath(app_dir)
    chrome_proxy_path = str(win_app_dir / "chrome_proxy.exe")
    chrome_path = str(win_app_dir / "chrome.exe")

    # The template uses the same placeholders across all rules.
    for rule in data.get("rules", []):
        program = rule.get("program", "")
        if program.lower().endswith("chrome_proxy.exe"):
            rule["program"] = chrome_proxy_path
        elif program.lower().endswith("chrome.exe"):
            rule["program"] = chrome_path

        args = rule.get("arguments", "")
        args = args.replace("YOUR_YOUTUBE_PWA_APP_ID", app_id)
        args = args.replace("YOUR_CHROME_PROFILE_DIRECTORY", profile)
        rule["arguments"] = args

    global_config = data.get("global")
    if isinstance(global_config, dict):
        global_config["fallbackBrowserPath"] = chrome_path

    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Could not write output file: {exc}")

    print(f"Created: {output}")
    print("Review this file before applying it to LinkRouter. The script does not test your app ID or route behavior.")
    print("Open LinkRouter's active config, apply the completed JSON there, and press Ctrl+S to save it.")


if __name__ == "__main__":
    main()
