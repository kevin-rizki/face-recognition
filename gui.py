import tkinter
from tkinter import filedialog
from extract import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np


window = tkinter.Tk()
window.wm_title("Embedding in Tk")
window.geometry('1000x750')

# Images
window.filename = filedialog.askopenfilename(initialdir = "./", title = "Select file",filetypes = (("jpeg files","*.jpg"), ("all files", ".")))

img = mpimg.imread(window.filename)

# img = mpimg.imread('./Justin_Bieber_2010_3.jpg')

fig = plt.figure(figsize=(8,5) ,dpi=100)
# Subplot 1st row 2nd col
fig.add_subplot(2, 3, 2)
plt.imshow(img)

# Subplot 2nd row 1st col
fig.add_subplot(2, 3, 4)
plt.imshow(img)

# Subplot 2nd row 2nd col
fig.add_subplot(2, 3, 5)
plt.imshow(img)

# Subplot 2nd row 3rd col
fig.add_subplot(2, 3, 6)
plt.imshow(img)

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# toolbar = NavigationToolbar2Tk(canvas, window)
# toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    window.quit()     
    window.destroy()  


button = tkinter.Button(master=window, text="Kembali Ke Menu Awal", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put window.destroy() here, it will cause an error if the window is
# closed with the window manager.