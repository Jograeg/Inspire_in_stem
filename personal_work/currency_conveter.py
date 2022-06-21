import os 
from tkinter import *
from tkinter import ttk
#from currency_converter import CurrencyConverter

root = Tk()
root.title("Currency Conveter")
currency(root)
root.mainloop() 

class Currency(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.currency = CurrencyConverter()
        self.options = ["ksh", "EUR", "USD", "CAD", "NZD", "CNY", "AUD", "GBP","DKK"]

        self.amount_label = Label(root, text="Amount: ")
        self.amount_label.grid(column=0, row=0)
        self.amount_entry = Entry(root)
        self.amount_entry.grid(column=1, row=0)

        self.selection_frame = LabelFrame(root, text="Currencies: ")
        self.selection_frame.grid(column=0, row=1, columnspan=2)
        self.frame_label = Label(self.selection_frame, text="From: ")
        self.frame_label.grid(column=0, row=0)
        self.to_label = Label(self.selection_frame, text="To: ")
        self.to_label.grid(column=1, row=0)

        self.from_menu = ttk.Combobox(self.selection_frame, values=self.options)
        self.from_menu.grid(column=0, row=1)
        self.from_menu.current(0)
        self.to_menu = ttk.Combobox(self. selection_frame, values = self.options)
        self.to_menu.grid(column=1, row=1)
        self.to_menu.current(0)

        self.result_label = Label(root, text=f"")
        self.result.grid(column=0, row=2, columnspan=2)
        self.converter_button = Button(root, text="Convert!", command=self.conveter)
        self.converter_button.grid(column=0, row=3, columnspan=2)

    def converter(self):
        try:
            currency_result = round(self.currency.Convert(float(self.amount_entry.get()), self.from_menu.get(), self.to_menu.get()), 2)
            self.result_label.configure(text=f"{self.result_label} {self.to_menu.get()}")
        except valueError:
            self.result_label.configure(text="This is not a number")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))