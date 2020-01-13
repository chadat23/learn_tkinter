from pathlib import Path
from tkinter import *

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('More learning')
root.iconbitmap(path / 'images' / 'favicon.ico')

my_image = ImageTk.PhotoImage(Image.open(path / 'images' / 'aspen.png'))
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text='Quite', command=root.quit)
button_quit.pack()

root.mainloop()
