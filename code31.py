# @princesanjivy
# rock paper scissor game using tkinter
from tkinter import *
import random
 
window = Tk()
window.title("Rock Paper Scissor")
window.geometry('400x100')
lbl = Label(window, text="Your selection")
lbl1 = Label(window)
lbl1.grid(column=1, row=0)
result = Label(window)
result.grid(column=0, row=2)

def click(btn):
    lbl["text"] = btn["text"]
    lbl1["text"] = random.choice(["Rock","Paper","Scissor"])

    Rock["state"] = "disabled"
    Paper["state"] = "disabled"
    Scissor["state"] = "disabled"

    if lbl["text"] == lbl1["text"]:
        result["text"] = "DRAW"
    elif lbl["text"] == "Rock" and lbl1["text"] == "Paper":
        result["text"] = "COMPUTER WINS!"
    elif lbl["text"] == "Rock" and lbl1["text"] == "Scissor":
        result["text"] = "YOU WIN!"
    elif lbl["text"] == "Paper" and lbl1["text"] == "Rock":
        result["text"] = "YOU WIN!"
    elif lbl["text"] == "Paper" and lbl1["text"] == "Scissor":
        result["text"] = "COMPUTER WINS!"
    elif lbl["text"] == "Scissor" and lbl1["text"] == "Paper":
        print("you wins!")
    elif lbl["text"] == "Scissor" and lbl1["text"] == "Rock":
        result["text"] = "COMPUTER WINS!"

lbl.grid(column=0, row=0)
Rock= Button(window, text="Rock", width=10, command=lambda : click(Rock))
Paper= Button(window, text="Paper", width=10, command=lambda : click(Paper))
Scissor= Button(window, text="Scissor", width=10, command=lambda : click(Scissor))
Rock.grid(column=0, row=1)
Paper.grid(column=1, row=1)
Scissor.grid(column=2, row=1)

window.mainloop()
