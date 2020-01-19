from tkinter import Tk, Label

window = Tk() # Creates the window class

window.title("First Window")

# Creating a label class

lbl = Label(window,text="Hello",\
    font =("Arial Bold", 50))
lbl.grid(row=0,column=0)

# Setting window size 
window.geometry('350x200')

window.mainloop()# for the window to appear to users


