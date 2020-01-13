from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton, messagebox
import tkinter

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')


def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    # messagebox.showinfo('This is my popup.', 'Hello human.')
    response = messagebox.askyesno('This is my popup.', 'Hello human.')
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()



Button(root, text='Popup', command=popup).pack()

root.mainloop()
