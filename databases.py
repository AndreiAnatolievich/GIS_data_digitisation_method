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
    direction = 'x' if index == 0 else 'y'
    reply = False
    while not reply:
        reply = False
        validLength = False
    while not validLength:
        messagebox.showinfo("Select the START of {:s} direction".format(direction),
        "Click the START of {:s}.".format(direction))
        coord1 = plt.ginput(1,timeout=0,show_clicks=True) # (число точек, ?, показать точки)
        data1 = simpledialog.askfloat("Enter MIN","Enter the MINIMUM in {:s} direction".format(direction))
        if isinstance(data1, float):
            validLength = True
        else:
            messagebox.showerror("Error","Please provide a valid MIN.")