from matoi_rich_presence.core import ActivityEngine

def test_youtube_activity():
    a = ActivityEngine().detect("chrome.exe", "Cool video - YouTube", "https://www.youtube.com/watch?v=abc")
    assert a.details == "Watching YouTube"
    assert a.url.endswith("watch?v=abc")
    assert a.large_image == "youtube"

def test_github_activity():
    a = ActivityEngine().detect("chrome.exe", "repo", "https://github.com/fattestbro/MatoiRichPresence")
    assert a.details == "Working on GitHub"

def test_desktop_activity():
    a = ActivityEngine().detect("explorer.exe", "")
    assert a.details == "On the desktop"

def test_unknown_process():
    a = ActivityEngine().detect("example.exe", "Window")
    assert a.details == "Using example"
