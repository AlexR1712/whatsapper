# -*- coding: utf8 -*- 

from tkinter import *
import tkMessageBox

top = Tk()
# Code to add widgets will go here...
def send(text=""):
   tkMessageBox.showinfo( "Hello Python", "Hello World"+text)

# Field
L1 = Label(top, text="Mensaje")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

B = Button(top, text ="Enviar", command = lambda: send(E1.get()))
B.pack()
# Code to add widgets will go here...
top.mainloop()