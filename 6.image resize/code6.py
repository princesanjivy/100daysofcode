##coded by Prince!
##a script to resize any image using
##PYTHON
##prerequisite
##----------##
##pip install Pillow (for PIL - Python Imaging Library)

import argparse
from PIL import Image 

ap = argparse.ArgumentParser()
ap.add_argument("image", help="image file")
ap.add_argument("width", help="width to be resize")
ap.add_argument("height", help="height to be resize")
arg = vars(ap.parse_args())

im = Image.open(arg["image"])
print("Original image size",im.size)
im = im.resize((int(arg["width"]), int(arg["height"])), Image.ANTIALIAS)
im.save(arg["image"][:-4] + "_resized.png", quality=95)
print("Resized image size",im.size)