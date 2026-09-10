from __future__ import annotations
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Activity:
    details: str
    state: str = ""
    url: str | None = None
    large_image: str = "matoi"
    small_image: str = ""

class ActivityEngine:
    def __init__(self):
        self.rules = {
            "chrome": self._browser,
            "msedge": self._browser,
            "firefox": self._browser,
            "brave": self._browser,
            "opera": self._browser,
            "discord": lambda _: Activity("Using Discord", "Keeping an eye on the server list"),
            "steam": lambda _: Activity("Browsing Steam", "Looking for something to play"),
            "robloxstudio": lambda w: Activity("Developing in Roblox Studio", self._clean(w)),
            "code": lambda w: Activity("Writing code", self._clean(w)),
            "blender": lambda w: Activity("Working in Blender", self._clean(w)),
            "obs64": lambda _: Activity("Recording with OBS", "Setting up the shot"),
        }

    @staticmethod
    def _clean(value: str) -> str:
        value = re.sub(r"\s+", " ", value or "").strip()
        return value[:120]

    def detect(self, process: str, title: str = "", url: str = "") -> Activity:
        key = process.lower().removesuffix(".exe")
        fn = self.rules.get(key)
        if fn:
            return fn((title, url)) if key in {"chrome", "msedge", "firefox", "brave", "opera"} else fn(title)
        if key in {"explorer", "shellexperiencehost", "searchhost"}:
            return Activity("On the desktop", "Taking a look around")
        return Activity(f"Using {key or 'Windows'}", self._clean(title))

    def _browser(self, data) -> Activity:
        title, url = data
        host = url.lower()
        if "youtube.com" in host:
            name = self._clean(re.sub(r"\s+-\s+YouTube$", "", title)) or "YouTube"
            return Activity("Watching YouTube", name, url or None, "youtube")
        if "github.com" in host:
            return Activity("Working on GitHub", self._clean(title), url or None, "github")
        if "twitch.tv" in host:
            return Activity("Watching Twitch", self._clean(title), url or None, "twitch")
        if "reddit.com" in host:
            return Activity("Browsing Reddit", self._clean(title), url or None, "reddit")
        return Activity("Browsing the web", self._clean(title))
