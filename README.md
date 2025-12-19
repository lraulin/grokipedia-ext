# Grokipedia Redirect Extension

A Chrome extension that automatically redirects Wikipedia links to Grokipedia.

## Features

- Automatically redirects all Wikipedia URLs to their Grokipedia equivalents
- Supports all Wikipedia language variants (en.wikipedia.org, es.wikipedia.org, etc.)
- Preserves the full path, including article names, search queries, and URL fragments
- Lightweight and fast - runs as a background service worker

## Installation

### From Source (Developer Mode)

1. Clone this repository:
   ```bash
   git clone https://github.com/lraulin/grokipedia-ext.git
   cd grokipedia-ext
   ```

2. Open Chrome and navigate to `chrome://extensions/`

3. Enable "Developer mode" using the toggle in the top-right corner

4. Click "Load unpacked" and select the `grokipedia-ext` directory

5. The extension should now be installed and active!

## How It Works

When you navigate to any Wikipedia URL (e.g., `https://en.wikipedia.org/wiki/Example`), the extension automatically redirects you to the corresponding Grokipedia URL (e.g., `https://grok.com/en/wiki/Example`).

The redirect happens before the Wikipedia page loads, providing a seamless experience.

## Files

- `manifest.json` - Extension configuration and permissions
- `background.js` - Service worker that handles URL redirects
- `icons/` - Extension icons in various sizes

## Permissions

This extension requires the following permissions:

- `webRequest` - To intercept navigation requests
- `webNavigation` - To detect when users navigate to Wikipedia URLs
- `host_permissions` for `*.wikipedia.org` - To access Wikipedia URLs for redirection

## Development

To modify the extension:

1. Make your changes to the relevant files
2. Go to `chrome://extensions/`
3. Click the refresh icon on the Grokipedia Redirect extension card
4. Test your changes

## License

See [LICENSE](LICENSE) file for details.
