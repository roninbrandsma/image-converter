from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Image Converter")
root.minsize(800, 400)

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

filePath = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Images", "*.png *.jpg *.jpeg"), ("All Files", "*.*")]
)
print("Selected file:", filePath)

files = filedialog.askopenfilenames(
    title="Select Multiple Files",
    filetypes=[("Image Files", "*.jpg;*.png"), ("All Files", "*.*")]
)
print("Selected files:", files)

root.mainloop()