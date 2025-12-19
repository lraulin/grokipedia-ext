# Grokipedia Redirect Chrome Extension

A Chrome extension that automatically redirects all Wikipedia links to Grokipedia.

## Features

- Automatically redirects any Wikipedia URL to the corresponding Grokipedia URL
- Preserves the full path and query parameters
- Works with all Wikipedia language subdomains (en.wikipedia.org, fr.wikipedia.org, etc.)
- Uses Chrome's declarativeNetRequest API for efficient, privacy-preserving redirects

## Installation

### From Source

1. Clone or download this repository
2. Generate extension icons (see below)
3. Open Chrome and navigate to `chrome://extensions/`
4. Enable "Developer mode" (toggle in the top right)
5. Click "Load unpacked"
6. Select the `grokipedia-ext` directory

### Generating Icons

The extension requires icon files. You can generate them using the provided script:

```bash
python3 generate_icons.py
```

Or manually create PNG files:

- `icons/icon16.png` (16x16 pixels)
- `icons/icon48.png` (48x48 pixels)
- `icons/icon128.png` (128x128 pixels)

## How It Works

The extension uses Chrome's `declarativeNetRequest` API to intercept requests to Wikipedia domains and redirect them to Grokipedia. The redirect rules are defined in `rules.json` and use regex pattern matching to preserve the full URL structure.

## Files

- `manifest.json` - Extension configuration
- `background.js` - Service worker (minimal, redirects handled by declarative rules)
- `rules.json` - Declarative redirect rules
- `icons/` - Extension icons directory

## License

See LICENSE file for details.
