# MatoiRichPresence

Windows desktop Discord Rich Presence client with context-aware activity detection, browser integration, smart status text, dynamic buttons, privacy controls and a red/black anime-inspired interface.

## Included

- Foreground application and game detection
- Context-aware Activity Engine
- Browser context bridge
- YouTube-aware activity with public metadata
- Dynamic `Watch Video` and channel buttons
- Public / Limited / Private modes
- Per-EXE exclusions and custom rules
- Local activity history
- System tray controls
- Custom background image support
- One-file Windows build

## Run

For users, launch `MatoiRichPresence.exe` from the project root.

For source development:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m matoi_rich_presence
```

`build_exe.bat` installs the build dependencies, runs the tests and writes `MatoiRichPresence.exe` directly to the project root. The final executable is not left in `dist`.

## Discord setup

Create a Discord application, copy its Application ID and enter it in the app settings.

## Browser connector

Load `browser_extension/` as an unpacked extension. It sends only the active tab URL, title, browser marker and timestamp to `127.0.0.1:28741`.

## Privacy

The client does not need a Discord account token. It does not intentionally read keystrokes, clipboard contents, screenshots or file contents. Private mode clears the published activity.

## License

MIT
