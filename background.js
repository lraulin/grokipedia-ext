// Background service worker for Grokipedia Redirect extension
// The actual redirect logic is handled by declarativeNetRequest rules in rules.json

// Listen for extension installation
chrome.runtime.onInstalled.addListener(() => {
  console.log("Grokipedia Redirect extension installed");
});
