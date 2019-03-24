# @princesanjivy
# send blank whatsapp message
# from whatsapp web.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://web.whatsapp.com")

qr_done = input() # scan the QR
no_blk_msg = int(input()) # number of blank message to send

print("sending messages.")
if qr_done == "send":
    text = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
    time.sleep(2)
    for i in range(no_blk_msg): 
        text.send_keys(chr(1968))
        text.send_keys(Keys.ENTER)
        time.sleep(0.45)

driver.quit()
