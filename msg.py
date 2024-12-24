from tkinter import *
from tkinter import messagebox
win= Tk()
win.geometry("400x400")

def mag():
    messagebox.showwarning("Alert", "Stop virus was found.")
b= Button(win, text= "Scan for virus", command= mag) 
b.place(x= 60, y= 80)
win.mainloop()