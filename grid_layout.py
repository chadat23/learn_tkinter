from tkinter import Tk
from tkinter.ttk import Label

root = Tk()

my_label1 = Label(root, text='Hello world!')
my_label2 = Label(root, text='My name is Chad!')
my_label3 = Label(root, text='                  ')

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=5)
my_label3.grid(row=1, column=1)

root.mainloop()
