# Troubleshooting

## YouTube opens in a normal browser tab

- Check that YouTube is installed as a PWA in the profile named in the rule.
- Compare the shortcut's **Properties → Target** with `--app-id` and `--profile-directory` in the configuration.
- Check the `chrome_proxy.exe` path and make sure the YouTube rules appear above the last catch-all rule.

## LinkRouter cannot find Chrome

Check every `program` path and `global.fallbackBrowserPath`. The template uses `chrome_proxy.exe` for the PWA rules and `chrome.exe` for the fallback. The Chrome Application directory varies between PCs and installation types.

## The placeholders are still in the config

Search the file for `YOUR_CHROME_PROFILE_DIRECTORY`, `YOUR_YOUTUBE_PWA_APP_ID`, and `PATH\\TO\\CHROME`. Replace every occurrence before using the config. The template is a starting point, not a ready-to-import config.

## Studio, activation, or Music links do not reach the requested page

- Confirm the cross-domain handoff extension is installed and enabled in the same Chrome profile as the PWA.
- Check that these rules retain the `__lr_pwa_handoff=1` marker and the captured destination after `#`.
- Keep specific rules above the regular YouTube rule and final fallback.
- Chrome may open out-of-scope pages outside the PWA window. The extension cannot permanently change the PWA's declared scope.

## A rule does not match

LinkRouter uses Go-style regular expressions and tries rules in order; the first match wins. Check the full URL, optional `www.`, the path, query string, and trailing slash. Avoid moving broad rules above specific rules.

## Save and rollback

After changing the active config in its editor, press **Ctrl + S**. Keep a backup of the previous file until tests pass. To roll back, restore that backup using the method documented for your LinkRouter version.

## Security

LinkRouter rules can launch programs and pass them arguments. Review every rule before importing a config. The handoff extension matches top-level HTTP/HTTPS pages; although it only redirects when the expected marker is present, check its code and Chrome's site-access permissions before enabling it.
