# MatoiRichPresence

A Windows Discord Rich Presence client built around context rather than a pile of hard-coded statuses.

## Current release

**5.0.0** — release candidate

### Included

- Foreground Windows application detection
- Context-aware Activity Engine
- Browser context bridge for Chromium/Firefox-based browsers
- YouTube, GitHub, Twitch and Reddit URL awareness
- Discord Rich Presence integration
- Dynamic `Watch Video` button for detected YouTube URLs
- PySide6 desktop UI
- Private mode
- Windows executable build script
- Windows GitHub Actions test matrix

## Requirements

- Windows 10/11
- Python 3.10+ for source execution
- Discord desktop client for Rich Presence
- A Discord Application ID

## Run from source

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m matoi_rich_presence
```

Or run `build_exe.bat` on Windows to create `dist\MatoiRichPresence.exe`.

## Browser bridge

Load `browser_extension/` as an unpacked extension in Chromium/Firefox-compatible development tooling. The extension sends only the active tab URL and title to the localhost bridge used by the desktop client.

## Privacy

The project is designed around public activity context. It does not require a Discord account token and does not intentionally collect passwords, clipboard contents, keystrokes or screenshots. Use Private mode when you do not want an activity published.

## Development

Run:

```powershell
pytest -q
```

See `CONTRIBUTING.md` and `SECURITY.md` before opening a pull request or reporting a security issue.

## License

MIT
