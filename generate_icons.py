#!/usr/bin/env python3
"""
Simple script to generate placeholder icons for the Chrome extension.
Requires PIL (Pillow): pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow is required. Install it with: pip install Pillow")
    exit(1)

def create_icon(size, output_path):
    """Create a simple icon with 'G' for Grokipedia"""
    # Create a new image with a blue background
    img = Image.new('RGB', (size, size), color='#4285f4')
    draw = ImageDraw.Draw(img)

    # Try to use a font, fallback to default if not available
    try:
        # Try to use a system font
        font_size = int(size * 0.7)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", int(size * 0.7))
        except:
            font = ImageFont.load_default()

    # Draw a white 'G' in the center
    text = "G"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) // 2 - bbox[0], (size - text_height) // 2 - bbox[1])

    draw.text(position, text, fill='white', font=font)
    img.save(output_path)
    print(f"Created {output_path}")

if __name__ == "__main__":
    import os

    # Create icons directory if it doesn't exist
    os.makedirs("icons", exist_ok=True)

    # Generate icons in different sizes
    create_icon(16, "icons/icon16.png")
    create_icon(48, "icons/icon48.png")
    create_icon(128, "icons/icon128.png")

    print("\nIcons generated successfully!")

