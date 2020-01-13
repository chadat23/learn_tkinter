from tkinter import *

root = Tk()

# e = Entry(root)
e = Entry(root, width=50, bg='blue', fg='white', borderwidth=5)
e.pack()
e.insert(0, 'Enter your name:')


def when_clicked():
    my_label = Label(root, text=f'Hello {e.get()}!')
    my_label.pack()


my_button = Button(root, text='Enter your name', command=when_clicked)
my_button.pack()

root.mainloop()
