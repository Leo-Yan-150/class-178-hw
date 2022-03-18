from tkinter import *
import random

root=Tk()
root.title("Something")
root.geometry("400x400")
root.config(bg="lavender")

label = Label(root, bg="orchid3",fg="white", font=("Times",40))
label.place(relx=0.5,rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        self._score=0
    def updateGame(self):
        self.text=["orange","red","yellow","green","cyan","blue","purple","navy","forestgreen","skyblue"]
        self.number = random.randint(0,9)
        self.number2 = random.randint(0,9)
        label["text"]=self.text[self.number]
        label["fg"]=self.text[self.number2]
        
gaem = game()

btn=Button(root,text="Start",command=gaem.updateGame())
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
    
root.mainloop()