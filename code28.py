# @princesanjivy
# a screenshot application with tkinter

from tkinter import *
import pyscreenshot, time

window = Tk()
window.title("python screenshot")
window.geometry("200x200")
window.wm_state("iconic")

def onclicked():
	window.iconify()
	time.sleep(0.5)
	im = pyscreenshot.grab()
	im.save("screenshot.png")

btn = Button(window, text="Take screenshot", command=onclicked)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()