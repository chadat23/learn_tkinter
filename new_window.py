from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton, messagebox, Toplevel
import tkinter

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')


def open_window():
    global image
    top = Toplevel()
    top.title('You know it!')
    Label(top, text='Spawned').pack()
    image = ImageTk.PhotoImage(Image.open(Path() / 'images' / 'me1.png'))
    Label(top, image=image).pack()
    Button(top, text='Close', command=top.destroy).pack()


Button(root, text='Open a window', command=open_window).pack()

root.mainloop()
