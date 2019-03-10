# @princesanjivy
# square fit an image using PIL

from PIL import Image,ImageFilter
im = Image.open("image.jpg")
bg = im
size = (1080,1080) 

if im.size != size:
    bg = bg.resize(size,Image.ANTIALIAS)
    bg = bg.filter(ImageFilter.GaussianBlur(50)) #bg blur
    im = im.resize((size[0],size[1]-200),Image.ANTIALIAS)
    bg.paste(im,(0,100))
    
bg.save("image_squarefit.png")
