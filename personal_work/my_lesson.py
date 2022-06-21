from tkinter import *
import tkinter.messagebox

#LARGE_FONT = ("Verdana", 12)
#NORM_FONT = ("Helvetica", 10)
#SMALL_FONT = ("Helvetica", 8)

#def popupmsg(msg):
#    popup = tk.Tk()
#    popup.wm_title("!")
#    label = ttk.Label(popup, text=msg, font=NORM_FONT)
#    label.pack(side="top", fill="x", pady=10)
#    B1 = ttk.button(popup, text="okay", command = popup.destroy)
#    B1.pack()
    
window = Tk()
window.title("Welcome to my fantabulous House ")
window.configure(bg = 'blue')
window.geometry("400x400")# fix the window size
f_name = Label(window, text="First Name", font=('Arial bold',20))
s_name = Label(window, text="Second Name", font=('Arial bold',20))
f_name.grid(column = 60,row = 100)
s_name.grid(column = 60,row = 120)

def open_window():
    out = tkinter.messagebox.askquestion('Prompt', 'Do you want to continue?')
    if out == 'yes':
        label(win, text="Thank you for Response!", font=('Helvetica 22 bold'))#.pack(pady=40)
    else:
        win.destroy()    


btn = Button(window ,text = 'click me',command='open_window', bg = 'red', fg = 'black')
btn.grid(column = 100 , row = 180)
#btn.pack(pady=50)

txt_box = Entry(window , width = 20)
txt_box.grid(column = 100, row = 100)

txt_box = Entry(window , width = 20)
txt_box.grid(column = 100, row = 120)
window.mainloop()