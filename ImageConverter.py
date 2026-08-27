import cairosvg
import io
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image


window = Tk()
window.title("Image Converter")
window.minsize(800, 400)

mainframe = ttk.Frame()
mainframe.grid(column=0, row=0, sticky=NSEW)

fileNames = []


def browseFiles():
    files = filedialog.askopenfilenames(
        initialdir="/",
        title="Select Files",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.svg"), ("All Files", "*.*")]
    )

    fileNames.clear()

    for file in files:
        fileNames.append(file)

    label.config(text="\n".join(fileNames))
    print(fileNames)



def convert_images(target_ext, mode):
    for file in fileNames:
        name, extension = os.path.splitext(file)
        extension = extension.lower()

    if extension == ".svg":
        pngData = cairosvg.svg2png(url=file)
        image = Image.open(io.BytesIO(pngData))
    else:
        image = Image.open(file)


    if mode:
        image.convert(mode)

    outputFile = name + target_ext
    image.save(outputFile)


options = ["Select a Type:", ".png", ".jpeg"]
dropdownVar = StringVar()
dropdownVar.set(options[0])

# Widgets
label = ttk.Label(window, text="")
fileSearchBtn = ttk.Button(window, text="Select File...", command=browseFiles)
convertBtn = ttk.Button(window, text="Convert")
dropdownMenu = ttk.OptionMenu(window, dropdownVar, *options)


# Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)

# Rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=3)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

# Widget Position
label.grid(column=0, row=0)
fileSearchBtn.grid(column=3, row=3)
dropdownMenu.grid(column=4, row=2)
convertBtn.grid(column=4, row=3)

window.mainloop()