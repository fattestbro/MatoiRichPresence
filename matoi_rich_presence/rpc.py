from __future__ import annotations
from pypresence import Presence

class DiscordRPC:
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.rpc = Presence(client_id)
        self.connected = False

    def connect(self) -> bool:
        try:
            self.rpc.connect()
            self.connected = True
        except Exception:
            self.connected = False
        return self.connected

    def set_activity(self, activity, button_url: str | None = None):
        if not self.connected and not self.connect():
            return False
        buttons = [{"label": "Watch Video", "url": button_url}] if button_url else []
        try:
            self.rpc.update(details=activity.details, state=activity.state or None,
                            large_image=activity.large_image, small_image=activity.small_image or None,
                            buttons=buttons or None)
            return True
        except Exception:
            self.connected = False
            return False

    def clear(self):
        if self.connected:
            try:
                self.rpc.clear()
            except Exception:
                pass

    def close(self):
        try:
            self.rpc.close()
        except Exception:
            pass
