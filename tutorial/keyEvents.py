from tkinter import *

def doSomething(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

def submit(event):
    print('submitted')
window = Tk()
window.bind('<Return>',submit)
window.bind('<w>',submit)
window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()