# LinkRouter PWA Cross-Domain Handoff

This extension is a small bridge for LinkRouter rules that send a URL to a page on the PWA's own origin with the marker `__lr_pwa_handoff=1`, then place the requested HTTP(S) destination after `#`.

## Download and install

Use the packaged ZIP linked from this repository's Releases section once it is published. Extract it to a permanent folder, open `chrome://extensions` in the same Chrome profile as the PWA, enable **Developer mode**, and select **Load unpacked**. Choose the extracted folder containing `manifest.json`. Keep the folder in place while the extension is enabled.

## Example rule pattern

For a destination captured as `$1` by LinkRouter, the bridge argument has this form:

```text
--app-launch-url-for-shortcuts-menu-item="https://YOUR_PWA_ORIGIN/?__lr_pwa_handoff=1#$1"
```

Replace `YOUR_PWA_ORIGIN` with a URL belonging to the PWA you intend to launch. Use that PWA's actual executable, profile, and app ID. The project template uses the YouTube PWA; it should not be copied blindly to another PWA.

## Limits and permissions

This does not change a PWA's declared scope or guarantee that every destination stays inside the app window. Chrome may open an out-of-scope URL in a regular browser window, depending on its navigation behavior.

The content script matches HTTP and HTTPS pages and only redirects when the explicit handoff marker and a valid HTTP(S) target are present. It rejects other protocols and URLs containing embedded credentials. Review the source and the browser's site-access information before enabling it.
