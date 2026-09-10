from __future__ import annotations
import ctypes
import os
from ctypes import wintypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32


def active_window() -> tuple[str, str]:
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        return "", ""
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    try:
        handle = kernel32.OpenProcess(0x0410, False, pid.value)
        buf = ctypes.create_unicode_buffer(260)
        kernel32.QueryFullProcessImageNameW(handle, 0, buf, ctypes.byref(wintypes.DWORD(260)))
        kernel32.CloseHandle(handle)
        process = os.path.basename(buf.value)
    except Exception:
        process = ""
    length = user32.GetWindowTextLengthW(hwnd)
    title = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, title, length + 1)
    return process, title.value
