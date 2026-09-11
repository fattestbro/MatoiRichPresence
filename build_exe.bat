@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul || (echo Python launcher not found.&exit /b 1)
py -3.10 -m venv .buildenv || exit /b 1
call .buildenv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt pyinstaller==6.17.0
python -m pytest -q || exit /b 1
python -m PyInstaller --noconfirm --clean --distpath "%~dp0" --workpath "%~dp0.build" --specpath "%~dp0" MatoiRichPresence.spec || exit /b 1
if exist "%~dp0MatoiRichPresence.exe" echo Build complete: "%~dp0MatoiRichPresence.exe"
endlocal
