# Release checklist

- [ ] Verify the README's PWA installation steps with the current desktop version of Chrome.
- [ ] Confirm `config/linkrouter-template.json` contains placeholders, not a personal app ID or profile.
- [ ] Run `py .\scripts\validate-config.py` and test the customized output on Windows.
- [ ] Confirm the customization script reads the template and leaves it untouched.
- [ ] Test all documented routes on the Windows, Chrome, and LinkRouter versions being reported.
- [ ] Verify the cross-domain handoff extension's release ZIP and add its download link to README.md and links.md.
- [ ] Verify all Chrome Web Store and upstream release links.
- [ ] Check that no unrelated personal information appears in the project files or screenshots.
- [ ] Review license and attribution text before publishing.
- [ ] Do not claim that routes were tested on other computers unless that testing was done.
