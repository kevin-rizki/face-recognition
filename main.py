from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

LARGE_FONT = ("Verdana", 16)

image_path = "test"
fig = plt.figure(figsize=(8,5) ,dpi=100)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "KetokMagicHalal")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True) 
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        global image_path
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self, text="Pilih Gambar", command = lambda: self.SelectImage(controller))
        button1.pack()
        
    def SelectImage(self, controller):
        global image_path
        upload_img = filedialog.askopenfilename(initialdir = "./", title = "Select file", filetypes =  (("jpeg files","*.jpg"),("all files","*.*")))
        image_path = upload_img
        controller.show_frame(PageOne)
        print(image_path)
        
        
class PageOne(tk.Frame):
    
    sub1 = None
    sub2 = None
    sub3 = None
    sub4 = None
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global image_path
        label = ttk.Label(self, text="Page One", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
            
            # def on_key_press(event):
            #     print("you pressed {}".format(event.key))
            #     key_press_handler(event, canvas, toolbar)
        
        button0 = ttk.Button(self, text="Draw Image", command = lambda: self.draw_image())
        button0.pack()
        
        button1 = ttk.Button(self, text="Back To Home", command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="Clear plot", command = lambda: self.clear_image())
        button2.pack()
    
    def draw_image(self):
        global image_path
        global fig
        img = mpimg.imread(image_path)
        print(image_path)

        # Subplot 1st row 2nd col
        self.sub1 = fig.add_subplot(2, 3, 2)
        plt.imshow(img)
        
        # Subplot 2nd row 1st col
        self.sub2 = fig.add_subplot(2, 3, 4)
        plt.imshow(img)
        
        # Subplot 2nd row 2nd col
        self.sub3 = fig.add_subplot(2, 3, 5)
        plt.imshow(img)
        
        # Subplot 2nd row 3rd col
        self.sub4 = fig.add_subplot(2, 3, 6)
        plt.imshow(img)
        
        canvas = FigureCanvasTkAgg(fig, self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # toolbar = NavigationToolbar2Tk(canvas, window)
        # toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    def clear_image(self):
        print('ANjing')
        plt.close(fig)
        
        
if __name__ == '__main__':        
    app = SeaofBTCapp()
    app.geometry("1280x720")
    app.mainloop()
        
        
