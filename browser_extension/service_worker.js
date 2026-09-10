const send = async tab => {
  if (!tab?.url || !/^https?:/i.test(tab.url)) return;
  try {
    await fetch('http://127.0.0.1:28741/context', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({url: tab.url, title: tab.title || ''})
    });
  } catch (_) {}
};
chrome.tabs.onActivated.addListener(async ({tabId}) => send(await chrome.tabs.get(tabId)));
chrome.tabs.onUpdated.addListener((_id, change, tab) => {
  if (change.status === 'complete') send(tab);
});
