@echo off
setlocal
py -3.10 -m venv .venv
if errorlevel 1 exit /b 1
call .venv\Scripts\activate.bat
python -m pip install -U pip
pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --windowed --name MatoiRichPresence -m matoi_rich_presence
endlocal
