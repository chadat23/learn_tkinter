from tkinter import *

root = Tk()

def when_clicked():
    my_label = Label(root, text='You clicked the button!')
    my_label.pack()

my_button1 = Button(root, text='Click me 1!', command=when_clicked)
my_button2 = Button(root, text='Click me 2!', state=DISABLED)
my_button3 = Button(root, text='Click me 3!', padx=50, pady=20, fg='blue', bg='#ff00ff')

my_button1.pack()
my_button2.pack()
my_button3.pack()

root.mainloop()
