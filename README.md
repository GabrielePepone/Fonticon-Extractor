# Font Icon Generator

This Python script generates icon images from glyphs in the Segoe Fluent Icons font. It renders a specified Unicode glyph (in the format \uE701) as an image using the PIL (Python Imaging Library). The generated icon is saved as a PNG file.
Features

    Font Detection: Automatically finds the Segoe Fluent Icons font installed on your system.
    Generate Icon: Converts a Unicode glyph (e.g., \uE701) to an image.
    Customizable Options: You can set the font size, image size, and text color for the generated icon.
    Output: Saves the icon as a PNG file (icon.png by default).

---

## How It Works

    The script prompts you to input a glyph code in the format \uE701 (Unicode).
    The Segoe Fluent Icons font is loaded from the system (it must be installed).
    The script renders the glyph as an image, centered within the defined size and color, and saves it to disk as a PNG file.

If the font is not found, the script will notify you with an error message.

---

## Customization Options

    Font Size: Adjust the size of the icon by changing the font_size parameter (default is 512).
    Image Size: Control the output image's dimensions with the image_size parameter (default is (512, 512)).
    Text Color: Set the icon's text color using the text_color parameter (default is "black").
