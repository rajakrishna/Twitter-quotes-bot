import os

import glob
from PIL import Image

images = glob.glob("images/*.png")
for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        img.show()

