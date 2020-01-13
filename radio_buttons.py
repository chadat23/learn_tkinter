from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton
import tkinter

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')

r = tkinter.IntVar()
r.set(2)

def selected(value):
    my_label = Label(root, text=value)
    my_label.pack()

Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: selected(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: selected(r.get())).pack()

my_label = Label(root, text=r.get())
my_label.pack()

root.mainloop()
