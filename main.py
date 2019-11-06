from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from tkinter import  *
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 16)

image_path = "test"
#fig = plt.figure(figsize=(8,5) ,dpi=100)

class Window(tk.Tk):
    currentFrame = None

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
            frame.pack_forget()
            #frame.pack(side="top", fill = "both", expand = True)
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = self.frames[cont]
        self.currentFrame.pack(side=TOP, fill=BOTH, expand=True)
        
        
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
    
    fig1 = None
    fig2 = None
    fig3 = None
    fig4 = None
    
    imgname2 = None
    imgname3 = None
    imgname4 = None

    accuracy2 = None
    accuracy3 = None
    accuracy4 = None
    
    buttons = None
    canvas = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global image_path
        #label = ttk.Label(self, text="Page One", font = LARGE_FONT)
        #label.pack(pady = 10, padx = 10)
            
            # def on_key_press(event):
            #     print("you pressed {}".format(event.key))
            #     key_press_handler(event, canvas, toolbar)
        
        self.buttons = tk.Frame(self)
        self.buttons.grid(row = 1, column = 0, sticky = "NEWS")

        self.canvas = tk.Canvas(self, width=1280, height=600)
        self.canvas.grid(row = 0, column = 0, sticky = "NEWS")
        
        button0 = ttk.Button(self.buttons, text="Pilih Gambar", command = lambda: self.SelectImage(controller))
        button0.grid(row = 2, column = 0, padx = (20, 20), sticky = "E")

        button1 = ttk.Button(self.buttons, text="Update", command = lambda: self.draw_image())
        button1.grid(row = 2, column = 1, padx = (20, 20), sticky = "W")
        
        button2 = ttk.Button(self.buttons, text="Match", command = lambda: controller.show_frame(StartPage))
        button2.grid(row = 2, column = 2, padx = (20, 20), sticky = "W")

    def draw_image(self):
        global image_path
        global fig
        #img = mpimg.imread(image_path)
        print(image_path)

        # Subplot 1st row 2nd col
        # self.sub1 = fig.add_subplot(2, 3, 2)
        # plt.imshow(img)
        self.sub1 = ImageTk.PhotoImage(Image.open(image_path).resize((540, 540), Image.ANTIALIAS))
        if (self.fig1 is None):
            self.fig1 = self.canvas.create_image(20, 20, anchor = NW, image = self.sub1)
        else:
            self.canvas.itemconfig(self.fig1, image = self.sub1)
        # Subplot 2nd row 1st col
        # self.sub2 = fig.add_subplot(2, 3, 4)
        # plt.imshow(img)
        self.sub2 = ImageTk.PhotoImage(Image.open(image_path).resize((160, 160), Image.ANTIALIAS))
        if (self.fig2 is None):
            self.fig2 = self.canvas.create_image(580, 40, anchor = NW, image = self.sub2)
            self.imgname2 = self.canvas.create_text(820, 60, text = "Titit gede")
            self.accuracy2 = self.canvas.create_text(820, 90, text = "Gede banget ahhhh")
        else:
            self.canvas.itemconfig(self.fig2, image = self.sub2)

        # Subplot 2nd row 2nd col
        # self.sub3 = fig.add_subplot(2, 3, 5)
        # plt.imshow(img)
        self.sub3 = ImageTk.PhotoImage(Image.open(image_path).resize((160, 160), Image.ANTIALIAS))
        if (self.fig3 is None):
            self.fig3 = self.canvas.create_image(580, 220, anchor = NW, image = self.sub3)
            self.imgname3 = self.canvas.create_text(820, 240, text = "Titit gede")
            self.accuracy3 = self.canvas.create_text(820, 270, text = "Gede banget ahhhh")
        else:
            self.canvas.itemconfig(self.fig3, image = self.sub3)
        

        # Subplot 2nd row 3rd col
        # self.sub4 = fig.add_subplot(2, 3, 6)
        # plt.imshow(img)
        self.sub4 = ImageTk.PhotoImage(Image.open(image_path).resize((160, 160), Image.ANTIALIAS))
        if (self.fig4 is None):
            self.fig4 = self.canvas.create_image(580, 400, anchor = NW, image = self.sub4)
            self.imgname4 = self.canvas.create_text(820, 420, text = "Titit gede")
            self.accuracy4 = self.canvas.create_text(820, 450, text = "Gede banget ahhhh")
        else:
            self.canvas.itemconfig(self.fig4, image = self.sub4)
        

        #canvas = FigureCanvasTkAgg(fig, self)  # A tk.DrawingArea.
        #canvas.draw()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # toolbar = NavigationToolbar2Tk(canvas, window)
        # toolbar.update()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1) 
    def SelectImage(self, controller):
        global image_path
        upload_img = filedialog.askopenfilename(initialdir = "./", title = "Select file", filetypes =  (("jpeg files","*.jpg"),("all files","*.*")))
        image_path = upload_img
        #controller.show_frame(PageOne)
        self.draw_image()
        print(image_path)
        
if __name__ == '__main__':        
    app = Window()
    app.geometry("1280x720")
    app.mainloop()
        
        
