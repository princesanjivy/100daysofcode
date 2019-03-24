# @princesanjivy
# draw text on an image using PIL

from PIL import Image, ImageDraw, ImageFont
im = Image.open("image.jpg")
font = ImageFont.truetype("font.ttf", 160)

draw = ImageDraw.Draw(im)
size = im.size[0]//2+10, im.size[1]//2-95
text = input("enter text: ")
draw.text(size, text, fill="white", font=font)
del draw

im.save("textonimage.png", quality=95)
