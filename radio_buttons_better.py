from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton
import tkinter

from PIL import ImageTk, Image

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')

def selected(value):
    my_label = Label(root, text=value)
    my_label.pack()

toppings = [('Pepperoni', 'pepperoni'),
            ('Cheese', 'cheese'),
            ('Mushroom', 'mushroom'),
            ('Onion', 'onion')
            ]

pizza = tkinter.StringVar()
pizza.set(toppings[0][1])

[Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=tkinter.W  )
 for text, topping
 in toppings]

# topping_label = Label(root, text=pizza.get())
# topping_label.pack()

topping_button = Button(root, text='Click Me', command=lambda: selected(pizza.get()))
topping_button.pack()

root.mainloop()
