from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN
import tkinter

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('More learning')
root.iconbitmap(path / 'images' / 'favicon.ico')

images = [ImageTk.PhotoImage(Image.open(path / 'images' / 'aspen.png')),
          ImageTk.PhotoImage(Image.open(path / 'images' / 'aspen2.png')),
          ImageTk.PhotoImage(Image.open(path / 'images' / 'me1.png')),
          ImageTk.PhotoImage(Image.open(path / 'images' / 'me2.png')),
          ImageTk.PhotoImage(Image.open(path / 'images' / 'me3.png'))
          ]
image_index = 0

status = Label(root, text=f'Image 1 of {len(images)}', bd=1, relief=SUNKEN, anchor=tkinter.E)

my_label = Label(image=images[0])
my_label.grid(row=0, column=0, columnspan=3)


def next_image():
    global image_index, button_next, button_back, my_label

    if image_index < len(images) - 1:
        image_index += 1
        my_label.grid_forget()
        my_label = Label(image=images[image_index])
        my_label.grid(row=0, column=0, columnspan=3)
        button_back = Button(root, text='<<', command=last_image)
        button_back.grid(row=1, column=0)
    if image_index == len(images) - 1:
        button_next = Button(root, text='>>', command=next_image, state=DISABLED)
        button_next.grid(row=1, column=2)
    status = Label(root, text=f'Image {image_index+1} of {len(images)}', bd=1, relief=SUNKEN, anchor=tkinter.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W+tkinter.E)



def last_image():
    global image_index, button_next, button_back, my_label

    if image_index > 0:
        image_index -= 1
        my_label.grid_forget()
        my_label = Label(image=images[image_index])
        my_label.grid(row=0, column=0, columnspan=3)
        button_next = Button(root, text='>>', command=next_image)
        button_next.grid(row=1, column=2)
    if image_index == 0:
        button_back = Button(root, text='<<', command=last_image, state=DISABLED)
        button_back.grid(row=1, column=0)
    status = Label(root, text=f'Image {image_index+1} of {len(images)}', bd=1, relief=SUNKEN, anchor=tkinter.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W+tkinter.E)


button_quit = Button(root, text='Quite', command=root.quit)
button_back = Button(root, text='<<', command=last_image, state=DISABLED)
button_next = Button(root, text='>>', command=next_image)

button_quit.grid(row=1, column=1, pady=10)
button_next.grid(row=1, column=2)
button_back.grid(row=1, column=0)

status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W+tkinter.E)

root.mainloop()
