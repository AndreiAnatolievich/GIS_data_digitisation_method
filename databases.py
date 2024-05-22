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
            messagebox.showinfo("Select the END of {:s} direction".format(direction),

"Click the END of {:s}.".format(direction))
coord2 = plt.ginput(1,timeout=0,show_clicks=True)
data2 = simpledialog.askfloat("Enter MAX","Enter the MAXIMUM in {:s} direction".format(direction))
if isinstance(data2, float):
    validLength = True
else:
    messagebox.showerror("Error","Please provide a valid MAX.")

# factor=data1 data2 coord1 coord2# то, что нужно для расчётов и то, что функция возвращает
reply = messagebox.askyesno("Information",
You selected from {:4.4f} to {:4.4f} in {:s}. Is this correct?".format(data1,data2,direction)
)
PiForPo=(coord2[0][index]-coord1[0][index])/(data2-data1)
return [PiForPo,data1,coord1]
xfactor = getReferenceLength(0)
yfactor = getReferenceLength(1)

# digitize curves until stoped by the user
messagebox.showinfo("Digitize curve",
"Please digitize the curve. The first point is the origin." +
"Left click: select point; Right click: undo; Middle click: finish"
)

# get the curve points
data = plt.ginput(-1,timeout=0,show_clicks=True)
data = asarray(data)
ax.plot(data[:,0],data[:,1],'g','linewidth',1.5)
plt.draw()

# convert the curve points from pixels to coordinates

