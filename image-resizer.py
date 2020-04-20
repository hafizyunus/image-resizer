
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image

size = 1500,1100

Tk().withdraw()
filename = askopenfilename()

im = Image.open(filename)
im_resized = im.resize(size, Image.ANTIALIAS)
save_file = asksaveasfilename(defaultextension=".jpg",filetypes = (("JPEG files","*.jpg"),('all files','*.*')))
im_resized.save(save_file, "JPEG")