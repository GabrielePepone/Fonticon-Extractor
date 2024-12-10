from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from colorama import Fore, Style

def find_font(font_family):
    for font in font_manager.findSystemFonts(fontpaths=None, fontext='ttf'):
        font_prop = font_manager.FontProperties(fname=font)
        if font_family.lower() in font_prop.get_name().lower():
            return font
    return None

def generate_icon(glyph, output_path, font_size=512, image_size=(512, 512), text_color="black"):
    font_path = find_font("Segoe Fluent Icons")
    if not font_path:
        print(Fore.RED + "Font Segoe Fluent Icons non trovato. Assicurati che sia installato." + Style.RESET_ALL)
        return

    try:
        image = Image.new("RGBA", image_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, font_size)
        bbox = font.getbbox(glyph)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
        draw.text(position, glyph, font=font, fill=text_color)
        image.save(output_path)
        print(Fore.GREEN + f"Successfully saved in {output_path}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.YELLOW + "Insert the code glyph (ex. \\uE701): " + Style.RESET_ALL, end="")
    glyph_input = input()
    
    if glyph_input.startswith("&#x"):
        glyph_char = chr(int(glyph_input[3:], 16))
    elif glyph_input.startswith("\\u"):
        glyph_char = chr(int(glyph_input[2:], 16))
    else:
        glyph_char = glyph_input

    print(Fore.MAGENTA + f"Glyph: {glyph_char}, Unicode: {ord(glyph_char)}" + Style.RESET_ALL)
    output_path = "icon.png"
    generate_icon(glyph_char, output_path)
