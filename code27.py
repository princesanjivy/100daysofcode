# @princesanjivy
# take screenshot

import pyscreenshot, time
time.sleep(3)

# capture full screen
im = pyscreenshot.grab()
im.save("screenshot.png")
