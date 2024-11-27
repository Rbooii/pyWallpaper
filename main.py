import numpy as np
from PIL import Image
import random

# Gradient wallpaper dimensions (4K resolution)
width, height = 3840, 2160
theme = "light"  # Change this to "light" for a lighter theme

while True :
    # Define two random colors for the gradient (RGB format)
    if theme == "dark":
        color1 = np.random.randint(0, 100, size=(1, 1, 3))  # Darker colors (0-100)
        color2 = np.random.randint(0, 100, size=(1, 1, 3))
    else:  # theme == "light"
        color1 = np.random.randint(155, 256, size=(1, 1, 3))  # Lighter colors (155-255)
        color2 = np.random.randint(155, 256, size=(1, 1, 3))

    # Create linear gradients for blending
    y_gradient = np.linspace(0, 1, height).reshape(height, 1, 1)
    x_gradient = np.linspace(0, 1, width).reshape(1, width, 1)

    # Blend colors horizontally and vertically
    vertical_gradient = (1 - y_gradient) * color1 + y_gradient * color2
    gradient = (1 - x_gradient) * vertical_gradient + x_gradient * color2

    # Add noise for texture effect
    noise = np.random.normal(0, 25, gradient.shape).astype(np.int16)
    gradient = np.clip(gradient + noise, 0, 255).astype(np.uint8)

    # Convert the array to an image
    gradient_image = Image.fromarray(gradient)
    gradient_image.save('image/4k_fast_noise_gradient_wallpaper.png', format='JPEG', quality=90, optimize=True)
    print("Generated the " + theme +" themed Image successfully !")
    print("                                  ")
    #gradient_image.show()

    #cheking user consent
    state = input("reGenerate ? [y/n]  ")
    if state == "y":
        continue
    else:
        break

