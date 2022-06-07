#!/usr/bin/python

##################################################
#         Gui examples
#         Name : Jamo         
#         date: 7 / 6 / 2022 Tuesday

###########

from tkinter import *
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("House of your choice")
    top.configure(bg = 'green')
    msg = label(top,text = "Welcome to fantabulous houses", font = ('Mistral 18')) .place(x=150,y=150)

window = Tk()
window.title("Welcome to my fantabulous House ")
window.configure(bg = 'blue')
window.geometry("400x400")# fix the window size
f_name = Label(window, text="First Name", font=('Arial bold',20))
s_name = Label(window, text="Second Name", font=('Arial bold',20))
f_name.grid(column = 60,row = 100)
s_name.grid(column = 60,row = 120)

btn = Button(window ,text = 'click me', bg = 'red', fg = 'black')
btn.grid(column = 100 , row = 180)

txt_box = Entry(window , width = 20)
txt_box.grid(column = 100, row = 100)

txt_box = Entry(window , width = 20)
txt_box.grid(column = 100, row = 120)

#def open_popup():
#    top = Toplevel(window)
#    top.geometry("300x300")
#    top.title("House of your choice")
#    top.configure(bg = 'green')
#    msg = label(top,text = "Welcome to fantabulous houses" font = ('Mistral 18')) .place(x=150,y=150)

window.mainloop()