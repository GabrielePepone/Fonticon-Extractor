from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Style

def generate_icon(glyph, font_path, output_path, font_size=200, image_size=(256, 256), text_color="black"):
    """
    Genera un'immagine da una fonticon.
    
    Args:
        glyph (str): Il codice unicode del carattere (es. '\uE717').
        font_path (str): Il percorso del file del font (es. 'segmdl2.ttf').
        output_path (str): Percorso di output per salvare l'immagine (es. 'icon.png').
        font_size (int): Dimensione del font.
        image_size (tuple): Dimensioni dell'immagine in pixel (larghezza, altezza).
        text_color (str/tuple): Colore del testo nell'immagine.
    """
    try:
        # Crea un'immagine vuota con sfondo trasparente
        image = Image.new("RGBA", image_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        
        # Carica il font
        font = ImageFont.truetype(font_path, font_size)
        
        # Ottieni le dimensioni del testo
        bbox = font.getbbox(glyph)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
        
        # Disegna il carattere
        draw.text(position, glyph, font=font, fill=text_color)
        
        # Salva l'immagine
        image.save(output_path)
        print(Fore.GREEN + f"Succesfully saved in {output_path}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

# Funzione principale
if __name__ == "__main__":
    print(Fore.YELLOW + "Insert the code glyph (ex. \\uE700): " + Style.RESET_ALL, end="")
    glyph_input = input()
    
    # Converte il codice in carattere (se necessario)
    if glyph_input.startswith("&#x"):
        glyph_char = chr(int(glyph_input[3:], 16))
    elif glyph_input.startswith("\\u"):
        glyph_char = chr(int(glyph_input[2:], 16))
    else:
        glyph_char = glyph_input  # Assume che l'utente inserisca direttamente il carattere

    # Percorso del font (assicurati di specificare il percorso corretto)
    font_path = "segmdl2.ttf"  # Cambia con il percorso del file del font

    # Percorso di output
    output_path = "icon.png"

    # Genera l'immagine
    generate_icon(glyph_char, font_path, output_path)