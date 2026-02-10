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

fileString = []
fileNames = []

def browseFiles():
    files = filedialog.askopenfilenames(
        initialdir="/",
        title="Select Files",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")]
    )

    fileNames.clear()

    for file in files:
        fileNames.append(file)

    label.config(text="\n".join(fileNames))
    print(fileNames)

def convertToJPEG():
    for file in fileNames:
        im = Image.open(file)
        rgbIm = im.convert("RGB")

        f, e = os.path.splitext(file)
        if e == ".jpeg":
            print("Can not convert JPEG file to JPEG.")

        name = f + ".jpeg"
        print(name)
        rgbIm.save(name)


# Widgets
label = ttk.Label(window, text="")
fileSearchBtn = ttk.Button(window, text="Select File...", command=browseFiles)
convertBtn = ttk.Button(window, text="Convert", command=convertToJPEG)

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

# Widget Position
label.grid(column=0, row=0)
fileSearchBtn.grid(column=3, row=2)
convertBtn.grid(column=4, row=2)

window.mainloop()