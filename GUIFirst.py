from tkinter import Tk, Label,Button
from tkinter import Entry

window = Tk() # Creates the window class

window.title("First Window")

# Creating a label class

lbl = Label(window,text="Hello",\
    font =("Arial Bold", 20))
lbl.grid(row=0,column=0)

# Setting window size 
window.geometry('350x200')

#Creating inputs
txt = Entry(window,width=10)
txt.grid(column=2,row=0)
txt.focus()


#Creating a button widget
def clicked():
    res = txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Submit",\
    bg = "yellow", fg = "red",\
        command=clicked)
btn.grid(column =1,row=0)



window.mainloop()# for the window to appear to users


