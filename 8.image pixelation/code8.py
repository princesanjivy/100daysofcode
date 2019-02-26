# coded by Prince!
# a script to pixelate any image
# prerequisite
# pip install pillow

from PIL import Image 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("image", help="Image to be pixelated")
arg = vars(ap.parse_args())

im = Image.open(arg["image"])
pix = im.resize((64,64), Image.NEAREST)
im = pix.resize(im.size, Image.NEAREST)
im.save(arg["image"][:-4] + "_pixelated.png", quality=100)
print("Image pixelated!")