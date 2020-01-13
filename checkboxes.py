from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton, messagebox, Toplevel, \
    filedialog
import tkinter
import json

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')
root.geometry('400x500')

var = tkinter.IntVar()

c = tkinter.Checkbutton(root, text="Here's the first checkbox!", variable=var)
c.deselect()
c.pack()


def show():
    label = Label(root, text=var.get())
    label.pack()


Button(root, text='Slider Location', command=show).pack()

root.mainloop()
