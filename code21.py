# @princesanjivy
# drawing random polygon using PIL

from PIL import Image, ImageDraw
import random
size = 500

im = Image.new("RGB",(size,size),"white")
draw = ImageDraw.Draw(im)

for do in range(size//2):
	#vertices of triangle
	dim = [ (random.randint(0,size), random.randint(0,size)),
			(random.randint(0,size), random.randint(0,size)),
			(random.randint(0,size), random.randint(0,size))] 
	#random colors
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

	draw.polygon(dim, "rgb({}, {}, {})".format(r, g, b))

del draw
im.show()