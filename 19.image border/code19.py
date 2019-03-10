# @princesanjivy
# adding a border to an image using PIL

from PIL import Image,ImageDraw

im = Image.open("100daysofcode.jpg")
bdr_data = input("border thickness and color:")
draw = ImageDraw.Draw(im)

for w in range(1, int(bdr_data.split()[0])):
	draw.rectangle([(0+w, 0+w), (im.size[0]-1-w, im.size[1]-1-w)], 
					outline = bdr_data.split()[1])
del draw
im.save("bordered.png", quality=95)