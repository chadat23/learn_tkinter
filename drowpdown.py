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

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

clicked = tkinter.StringVar()
clicked.set(days[0])

drop = tkinter.OptionMenu(root, clicked, *days)
drop.pack()


Button(root, text='Slider Location', command=lambda: Label(root, text=clicked.get()).pack()).pack()

root.mainloop()
