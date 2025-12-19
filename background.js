// Background service worker for redirecting Wikipedia to Grokipedia

chrome.webNavigation.onBeforeNavigate.addListener(
  function(details) {
    // Only process main frame navigations (not iframes)
    if (details.frameId !== 0) {
      return;
    }

    const url = new URL(details.url);
    
    // Check if this is a Wikipedia URL
    if (url.hostname.endsWith('.wikipedia.org')) {
      // Extract the language code (e.g., 'en' from 'en.wikipedia.org')
      const langMatch = url.hostname.match(/^([^.]+)\.wikipedia\.org$/);
      
      if (langMatch) {
        const lang = langMatch[1];
        const path = url.pathname + url.search + url.hash;
        
        // Construct the Grokipedia URL
        // Format: https://grok.com/{language_code}{wikipedia_path}
        // Example: en.wikipedia.org/wiki/Article -> grok.com/en/wiki/Article
        const grokipediaUrl = `https://grok.com/${lang}${path}`;
        
        // Redirect to Grokipedia
        chrome.tabs.update(details.tabId, { url: grokipediaUrl });
      }
    }
  },
  { url: [{ hostSuffix: '.wikipedia.org' }] }
);
