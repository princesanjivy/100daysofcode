# coded by Prince!
# OCR(Optical Character Recognition) using pytesseract
# prerequisite 
# pip install pytesseract
# pip install pillow

import pytesseract
from PIL import Image

im_text = Image.open("im_text.png")
text = pytesseract.image_to_string(im_text)
print(text)
