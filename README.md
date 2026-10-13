# YT ReVanced Experience for PC

This is my Windows setup for opening YouTube links in a YouTube app window instead of bouncing between browser tabs. It uses the YouTube PWA installed from Chrome, LinkRouter, and a small cross-domain handoff extension for a few links that do not normally belong to the YouTube site's app scope.

This is a set of configuration files and setup instructions, not an official ReVanced PC client. It is not affiliated with Google, YouTube, ReVanced, LinkRouter, or the developers of the extensions linked below.

## What this setup does

The LinkRouter template has rules for YouTube Shorts, mobile YouTube URLs, `youtu.be` links, Community posts, embedded-video links, YouTube Studio, `yt.be/activate`, YouTube Music, regular YouTube links, and a final fallback to Chrome for other HTTP/HTTPS links. The rules are order-sensitive: specific YouTube rules must stay above the final catch-all rule.

## What you need

- A Windows PC with Google Chrome installed.
- YouTube installed as a Chrome web app/PWA.
- LinkRouter for Windows and its Chromium browser companion.
- The **LinkRouter PWA Cross-Domain Handoff** extension for the Studio, activation, and Music handoff rules. The downloadable ZIP will be posted in this repository's Releases section; the direct download link will be added once the release is published.
- Any optional YouTube extensions you want. They are listed in [`links.md`](links.md) and are not required for LinkRouter itself.

## 1. Install YouTube as a Chrome PWA

Do this in the Chrome profile you want to use for YouTube. If you use more than one Chrome profile, make sure you install the PWA in the same one that you will put in the LinkRouter rules.

1. Install or open [Google Chrome](https://www.google.com/chrome/).
2. Open [youtube.com](https://www.youtube.com/) in Chrome.
3. In the top-right corner, click Chrome's three-dot menu.
4. Choose **Cast, save, and share** and then **Install page as app…**. Depending on the Chrome version or the page, an **Install** icon may also appear at the right of the address bar.
5. Follow the prompts and click **Install**.
6. Open the newly installed YouTube app once so you can confirm it works. You can launch it from the Start menu or the shortcut Chrome creates.

If the install option is missing, check that you are using the desktop version of Chrome and that it is up to date. Google's current instructions are in [Use web apps in Chrome](https://support.google.com/chrome/answer/9658361?co=GENIE.Platform%3DDesktop&hl=en).

### Find the PWA app ID and Chrome profile

1. Find the YouTube shortcut Chrome created. If needed, open `chrome://apps`, right-click YouTube, and choose **Create shortcut**.
2. Right-click the Windows YouTube shortcut and select **Properties**.
3. Look in the **Target** field for `--app-id=`. Copy the ID immediately after it, without adding spaces or quotation marks.
4. In the same Target field, find `--profile-directory=` if it is present. Copy the profile name, such as `Default` or `Profile 1`. If you have more than one Chrome profile, check that this is the profile where you installed YouTube.

The ID and profile in the example template are placeholders; every person should use the values for their own installation.

## 2. Download LinkRouter

1. Open the [official LinkRouter releases page](https://github.com/kolbasky/LinkRouter/releases/latest).
2. Download the current Windows installer, or use the portable build if you prefer that option.
3. Run it and follow the instructions in the upstream project. LinkRouter needs to be registered as a handler for the protocols you want it to catch. Use the upstream README if you need help with this step.
4. Download the Chromium browser companion from the same [official releases page](https://github.com/kolbasky/LinkRouter/releases/latest). Follow the release instructions to install it. The Chromium companion may need to be loaded in Developer mode, depending on the release package.

LinkRouter tries rules in order and uses the first match. Read the rules before you enable them; a rule can start a program and pass it command-line arguments.

## 3. Install the cross-domain handoff extension

The Studio, activation, and Music rules use the `__lr_pwa_handoff=1` marker. They need the **LinkRouter PWA Cross-Domain Handoff** extension enabled in the same Chrome profile as the YouTube PWA.

1. Download the extension ZIP from this project's Releases section once it is published.
2. Extract it to a folder you plan to keep. Do not delete or move that folder while the unpacked extension is enabled.
3. In the Chrome profile used for YouTube, open `chrome://extensions`.
4. Turn on **Developer mode**.
5. Click **Load unpacked** and select the extracted folder containing `manifest.json`.
6. Leave the extension enabled. Review the extension source and Chrome's site-access details before using it; it matches HTTP and HTTPS pages but only acts when the explicit handoff marker is present.

This extension does not change a PWA's declared scope. Chrome may still open an out-of-scope destination in a regular browser window, depending on its navigation behaviour. Test it on your setup instead of assuming every destination will stay inside the PWA.

## 4. Set up `linkrouter-template.json`

Open [`config/linkrouter-template.json`](config/linkrouter-template.json). Make a copy first if you want to keep an untouched template. The file contains placeholders so it does not publish one computer's Chrome profile or app ID.

### Replace these placeholders

**`C:\\PATH\\TO\\CHROME\\Application`**

Replace this base path wherever it appears, including `global.fallbackBrowserPath` and the `program` values in the rules. Use the location of your own Chrome `Application` folder. The PWA rules must point to `chrome_proxy.exe`; the last fallback rule must point to `chrome.exe`. A common location is `C:\Program Files\Google\Chrome\Application`, but it can be different on your PC.

Because this is JSON, Windows path separators must be doubled in the file. For example, use `C:\\Program Files\\Google\\Chrome\\Application` in JSON, not single backslashes.

**`YOUR_CHROME_PROFILE_DIRECTORY`**

Replace every occurrence with the profile directory from the YouTube shortcut's Target field, for example `Default` or `Profile 1`.

**`YOUR_YOUTUBE_PWA_APP_ID`**

Replace every occurrence with the app ID from the same shortcut's Target field, immediately after `--app-id=`.

These are plain text placeholders, not LinkRouter variables. Replace every occurrence before using the file. You can edit a copy by hand, or run the optional script below to make a separate local config.

### Make a local config with the script (optional)

If Python 3 is installed, open a terminal at the repository folder and run:

```powershell
py .\scripts\customize-config.py
```

Enter your PWA app ID, Chrome profile directory, and Chrome `Application` folder when asked. The script creates `config/linkrouter.local.json` and leaves the template alone. Review the output before using it.

You can check the JSON syntax and required fields with:

```powershell
py .\scripts\validate-config.py .\config\linkrouter.local.json
```

The validator checks the file format and required fields. It does not prove that all URLs route correctly.

### Save the active LinkRouter configuration

1. Back up your current `linkrouter.json` before replacing anything.
2. Open LinkRouter's active configuration using its **Edit config** command (or the method documented for your installed version).
3. Copy the complete, customized JSON into the active configuration editor, replacing the old contents if that is how you are applying the template.
4. Press **Ctrl + S** to save the configuration.
5. Reopen or reload the config if LinkRouter requires it, then test the links below.

Saving `config/linkrouter-template.json` by itself does not necessarily change the active configuration that LinkRouter is reading. Make sure you save the file that LinkRouter actually uses.

### Important notes

- Keep the rules in their current order. In particular, do not move the final `^(https?://.*)$` fallback above the YouTube rules.
- The template is written for Chrome. Another browser's PWA may use a different app ID, profile directory, executable, and launch arguments.
- For Edge, Brave, or another Chromium-based browser, install YouTube as a web app in that browser first, find its shortcut's **Properties → Target**, and identify the browser executable, profile, and app ID or equivalent. Adapt the `program` paths **and** launch arguments to that browser's supported format. Do not assume Chrome's `chrome_proxy.exe`, `--app-id`, and `--app-launch-url-for-shortcuts-menu-item` arguments will work unchanged in another browser. Test all routes before using it as your main configuration.
- The fallback rule opens other HTTP/HTTPS URLs in normal Chrome. If you want a different fallback browser, update `global.fallbackBrowserPath`, `global.fallbackBrowserArgs`, and the final rule as needed.

## 5. Test the routes

Start with one example of each type: a normal YouTube URL, a Shorts link, a `youtu.be` link, a Community post, a mobile YouTube URL, an embedded YouTube link, a Studio URL, `yt.be/activate`, a YouTube Music URL, and an unrelated HTTPS link. Check that each one opens in the expected place. If something goes wrong, restore your backup and check [`docs/troubleshooting.md`](docs/troubleshooting.md).

## Optional extensions

The other browser extensions in [`links.md`](links.md) are add-ons used in the reference setup. They are optional; install only the ones you want and review their permissions and privacy information.

## Files in this repository

- `config/linkrouter-template.json` — shareable template with placeholders.
- `scripts/customize-config.py` — creates a local configuration with your values.
- `scripts/validate-config.py` — checks JSON syntax and required fields.
- `extensions/cross-domain-handoff/` — source and notes for the custom handoff extension.
- `docs/setup.md` and `docs/troubleshooting.md` — extra setup and troubleshooting notes.
- `links.md` — LinkRouter, Chrome, and optional extension links.
- `THIRD_PARTY_NOTICES.md` — attribution and licensing notes.

## License and credits

The project files are provided under the license in [`LICENSE`](LICENSE). Third-party extensions are linked, not bundled. Their names, code, logos, licences, permissions, and privacy policies belong to their respective owners. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
