# coded by Prince!
# saving an image from an URL

import requests
from io import BytesIO
from PIL import Image

image_url = "https://tinyurl.com/y2y9k3gu"
req = requests.get(image_url)
im = Image.open(BytesIO(req.content))
im.save("Image.png", quality=95)


##image Source google