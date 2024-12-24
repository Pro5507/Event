from tkinter import *
window= Tk()
window.title("Event")
window.geometry("200x200")
def abc(event):
    print(event.char)
window.bind("<Key>", abc)
def abc_handle(event):
    print("\nThe button was clicked")
b= Button(text= "Click me")
b.pack()
b.bind("<Button-1>", abc_handle)
window.mainloop()