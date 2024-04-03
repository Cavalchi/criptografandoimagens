import os
import time
from tkinter import Tk, Button, filedialog
from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            if len(pixel) == 4:
                r, g, b, a = pixel
            else:
                r, g, b = pixel

            r = (r * key) % 256
            g = (g * key) % 256
            b = (b * key) % 256

            if len(pixel) == 4:
                pixels[x, y] = (r,g,b,a)
            else:
                pixels[x, y] = (r,g,b)

    return img

def on_button_click():
    file_paths = filedialog.askopenfilenames(filetypes=[('Image Files', '*.png;*.jpg')])
    for file_path in file_paths:
        if file_path:
            encrypted_image = encrypt_image(file_path, 123)
            if not os.path.exists('imagenscodificadas'):
                os.makedirs('imagenscodificadas')
            timestamp = int(time.time())
            encrypted_image.save(f'imagenscodificadas/encrypted_image_{timestamp}.png')

root = Tk()
root.title('Criptografar imagem')

button = Button(root, text='Criptografar imagem', command=on_button_click)
button.pack()

root.mainloop()