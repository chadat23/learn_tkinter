from pathlib import Path
from tkinter import Tk, Label, Button, DISABLED, SUNKEN, Radiobutton, messagebox, Toplevel, \
    filedialog
import tkinter
import json

path = Path('.')

root = Tk()
root.title('Frames!!')
root.iconbitmap(path / 'images' / 'favicon.ico')


def get_defaults():
    with open('open_file_defaults.json', 'r') as f:
        try:
            return json.load(f)
        except:
            return {}


root.filename = filedialog.askopenfilename(initialdir=get_defaults().get('open_dialog'),
                                           title='Select A File',
                                           filetypes=(('png files', '*.png'), ('all files', '*.*')))


def set_default(property_name: str, val: str):
    with open('open_file_defaults.json', 'r') as f:
        try:
            data = json.load(f.read())
        except:
            data = {}
    with open('open_file_defaults.json', 'w') as f:
        data[property_name] = val
        j = json.dumps(data, indent=4)
        f.write(j)


set_default('open_dialog', str(Path(root.filename).parents[0]))

root.mainloop()
