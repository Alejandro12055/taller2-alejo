import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def generate_star_background(width=800, height=600, num_stars=300):
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)

    for _ in range(num_stars):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        brightness = np.random.randint(150, 256)  # Blancos brillantes
        draw.point((x, y), fill=(brightness, brightness, brightness))

    return img

def draw_star_wars_logo(img):
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # Intenta usar una fuente estándar
    except:
        font = ImageFont.load_default()  # Fuente por defecto si no se encuentra otra

    text = "STAR WARS"
    bbox = draw.textbbox((0, 0), text, font=font)  # Obtiene las dimensiones del texto
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((img.width - text_width) // 2, img.height // 4)
    draw.text(position, text, fill="yellow", font=font)

    return img

img = generate_star_background()
img = draw_star_wars_logo(img)

plt.imshow(img)
plt.axis("off")
plt.show()
