from tkinter import *
from tkinter import ttk 
from time import strftime

root = Tk()
root.title('Digital clock')
root.geometry("400x400")

def time():
    x = strftime('%H:%M:%S %p')
    label.config(text = x)
    label.after(1000,time)

label = Label(root, font = ("cambria",80), background = 'black',foreground = 'cyan')
label.pack(anchor = 'center')
time()
mainloop()