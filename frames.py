from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN
import tkinter

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')

frame = tkinter.LabelFrame(root, text='This is my frame...', padx=5, pady=5)
frame.pack(padx=10, pady=10)

button = Button(frame, text='Click me?')
button.grid(row=0, column=0)
button1 = Button(frame, text='No, click me!')
button1.grid(row=1, column=1)

root.mainloop()
