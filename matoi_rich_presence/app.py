from __future__ import annotations
import os, sys, time
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QCheckBox
from PySide6.QtCore import QTimer
from .core import ActivityEngine
from .rpc import DiscordRPC
from .windows import active_window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MatoiRichPresence")
        self.resize(520, 330)
        self.engine = ActivityEngine(); self.rpc = None; self.started = False
        root = QWidget(); layout = QVBoxLayout(root)
        self.status = QLabel("Discord: not connected")
        self.client = QLineEdit(); self.client.setPlaceholderText("Discord Application ID")
        self.private = QCheckBox("Private mode")
        self.current = QLabel("No activity detected")
        self.toggle = QPushButton("Start Rich Presence")
        self.toggle.clicked.connect(self.toggle_presence)
        layout.addWidget(QLabel("MatoiRichPresence")); layout.addWidget(self.status); layout.addWidget(self.client)
        layout.addWidget(self.private); layout.addWidget(self.current); layout.addWidget(self.toggle)
        self.setCentralWidget(root)
        self.timer = QTimer(self); self.timer.timeout.connect(self.tick); self.timer.start(3000)

    def toggle_presence(self):
        self.started = not self.started
        self.toggle.setText("Stop Rich Presence" if self.started else "Start Rich Presence")
        if not self.started and self.rpc: self.rpc.clear()

    def tick(self):
        if not self.started or self.private.isChecked():
            self.status.setText("Discord: paused"); return
        client_id = self.client.text().strip()
        if not client_id: self.status.setText("Discord: enter Application ID"); return
        if not self.rpc or self.rpc.client_id != client_id: self.rpc = DiscordRPC(client_id)
        process, title = active_window()
        activity = self.engine.detect(process, title)
        self.current.setText(f"{activity.details}\n{activity.state}")
        ok = self.rpc.set_activity(activity, activity.url)
        self.status.setText("Discord: connected" if ok else "Discord: waiting for Discord")

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MatoiRichPresence")
    window = MainWindow(); window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())
