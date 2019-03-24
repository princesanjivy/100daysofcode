# @princesanjivy
# save instagram user's story pic as PNG
##---made only for learning purpose---##

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import time, requests

options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
driver.get("https://www.instagram.com/accounts/login/")

print("Login")
ig_username, ig_password = input("username: "), input("password: ") # login
username = driver.find_element_by_name("username")
username.send_keys(ig_username)
password = driver.find_element_by_name("password")
password.send_keys(ig_password)
password.send_keys(Keys.ENTER)
time.sleep(3)
profile_name = input("profile name: ")
driver.get("https://www.instagram.com/stories/" + profile_name)
time.sleep(3)

img_class = driver.find_element_by_class_name("qbCDp")
soup = BeautifulSoup(img_class.get_attribute("innerHTML"), features="lxml")
img_src = soup.findAll("img")
for src_url in img_src:
	img_url = src_url["src"]
driver.close()

req = requests.get(img_url)
im = Image.open(BytesIO(req.content))
im.save(profile_name + "_story.png", quality=95)
print("Image saved!")

