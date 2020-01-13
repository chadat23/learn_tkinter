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

vertical = tkinter.Scale(root, from_=0, to=200)
vertical.pack()


# def slide(val):
#     Label(root, text=horizontal.get()).pack()
#     root.geometry(f'{horizontal.get()}x500')
#
#
# horizontal = tkinter.Scale(root,
#                            from_=0, to=400,
#                            orient=tkinter.HORIZONTAL,
#                            command=slide)
# horizontal.pack()


horizontal = tkinter.Scale(root, from_=0, to=155, orient=tkinter.HORIZONTAL)


def slide():
    Label(root, text=horizontal.get()).pack()
    root.geometry(f'{horizontal.get()}x500')


Button(root, text='Slider Location', command=slide).pack()

root.mainloop()
