from tkinter import Tk, filedialog, messagebox, simpledialog

from numpy import asarray, savetxt

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

root = Tk() # open the dialog box
root.withdraw() # first hide the root window
# open the dialog
filein = filedialog.askopenfilename(
title = "Select image to digitize",
filetypes = (
("png files","*.png"),
("jpeg files","*.jpg"))
)

# show the image
img = mpimg.imread(filein)
_, ax = plt.subplots()
ax.imshow(img)

# ax.axis('off') # clear x-axis and y-axis
# get reference length in x direction

def getReferenceLength(index):