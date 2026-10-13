# Setup guide

## 1. Install the YouTube PWA in Chrome

1. Install [Google Chrome](https://www.google.com/chrome/) if needed.
2. Open [YouTube](https://www.youtube.com/) in the Chrome profile you want to use.
3. Open Chrome's three-dot menu and choose **Cast, save, and share → Install page as app…**. If Chrome shows an **Install** icon beside the address bar, you can use that instead.
4. Follow the prompts and install the app.
5. Open the app once. Find its Windows shortcut, right-click it, and choose **Properties**. In **Target**, note the value after `--app-id=` and the value after `--profile-directory=` if present. These are the values you will enter in the configuration.

Google's instructions: [Use web apps in Chrome](https://support.google.com/chrome/answer/9658361?co=GENIE.Platform%3DDesktop&hl=en).

## 2. Install LinkRouter

1. Download LinkRouter from the [official releases page](https://github.com/kolbasky/LinkRouter/releases/latest).
2. Run the Windows installer or follow the upstream instructions for the portable build.
3. Register it as a handler for the protocols you want it to receive.
4. Get the Chromium browser companion from the official release/installer instructions and install it as documented for that release.

## 3. Install the cross-domain handoff extension

The extension download will be linked from this repository's Releases page when published.

1. Download and extract the release ZIP to a folder you plan to keep.
2. In the same Chrome profile used by the YouTube PWA, open `chrome://extensions`.
3. Enable **Developer mode**, click **Load unpacked**, and select the extracted folder containing `manifest.json`.
4. Keep the extension enabled and leave its folder in place.

It can match HTTP and HTTPS pages, but only acts when the deliberate `__lr_pwa_handoff=1` marker is present. Review the source and Chrome's site-access details before enabling it.

## 4. Configure LinkRouter

1. Back up the active LinkRouter `linkrouter.json`.
2. Open `config/linkrouter-template.json` and make a working copy, or run the customizer from the repository folder:

   ```powershell
   py .\scripts\customize-config.py
   ```

3. Replace `C:\\PATH\\TO\\CHROME\\Application` with your Chrome Application folder, `YOUR_CHROME_PROFILE_DIRECTORY` with the PWA's profile directory, and `YOUR_YOUTUBE_PWA_APP_ID` with the app ID from the shortcut's Target field. The Chrome PWA rules use `chrome_proxy.exe`; the fallback uses `chrome.exe`.
4. If editing JSON by hand, keep path separators doubled as `\\` in the JSON file.
5. Open LinkRouter's active config with its **Edit config** command. Apply the completed JSON there, then press **Ctrl + S** to save the active configuration. Saving a separate template file does not automatically change LinkRouter's active config.
6. Keep the rules in the supplied order. The final HTTP/HTTPS fallback belongs at the bottom.

To validate a local config file:

```powershell
py .\scripts\validate-config.py .\config\linkrouter.local.json
```

## 5. Different browser

The template is for Chrome. For Edge, Brave, or another browser, install YouTube as a web app in that browser and inspect the shortcut's **Properties → Target**. Update the browser executable, PWA app identifier, profile, and launch arguments to match that browser. Chrome's `chrome_proxy.exe` and launch switches are not guaranteed to work in other browsers. Test the full set of routes before relying on it.

## 6. Test the routes

Test a regular YouTube link, Shorts link, `youtu.be` link, Community post, mobile URL, embed URL, Studio URL, `yt.be/activate`, Music URL, and an unrelated HTTPS URL. Confirm the destination and which window opens. Keep your backup until everything behaves as expected.

Optional extension links are in [`../links.md`](../links.md).
