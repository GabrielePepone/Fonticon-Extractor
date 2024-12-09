# FontIcon to Image Generator

This Python script allows you to generate an image file from a FontIcon glyph, such as `&#xE717;`. You can specify the glyph, choose a font file, and define the output image properties. Additionally, the script uses `colorama` to display messages in colored text for a better user experience.

---

## Features

- Accepts Unicode glyph input in various formats (e.g., `&#xE717;`, `\uE717`).
- Supports custom font files, such as `segmdl2.ttf` (Segoe MDL2 Assets).
- Generates a PNG image with the glyph rendered in the specified font and color.
- Uses the `Pillow` library for image processing.
- Displays console messages in colored text:
  - Yellow for input prompts.
  - Green for success messages.
  - Red for error messages.

---

## Requirements

Before running the script, ensure you have the following installed:

1. Python 3.13 or later
2. Pillow: Install via pip:
   pip install pillow
3. Colorama: Install via pip:
   pip install colorama

---

## How to Use

1. Prepare a font file:
   - Place a font file such as `segmdl2.ttf` (Segoe MDL2 Assets) in the same directory as the script, or update the `font_path` variable with the correct location of your font file.

2. Run the script:
   - Execute the script in a terminal or console:
     python main.py

3. Enter the glyph code:
   - When prompted, enter the glyph code in one of the supported formats:
     - Unicode escape: `\uE717`

4. Check the output:
   - The script generates an image (`icon.png` by default) with the glyph rendered at the center.

---

## Script Options

Glyph Input
The script supports three formats for glyph input:
- Unicode escape: `\uE717`

Font File
Update the `font_path` variable in the script to specify the path to the font file you want to use:
font_path = "segmdl2.ttf"  # Update with your font file path

Image Customization
You can modify the following parameters in the `generate_icon` function:
- `font_size`: Size of the glyph in the image (default: `200`).
- `image_size`: Dimensions of the output image in pixels (default: `(256, 256)`).
- `text_color`: Color of the glyph (default: `"black"`).

---

Console Messages
The script uses `colorama` for colored console messages. The input prompt will appear in yellow, success messages in green, and error messages in red.
