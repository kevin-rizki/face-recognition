from tkinter import  *
from tkinter import ttk, filedialog
from pageone import *
LARGE_FONT = ("Verdana", 16)

class MainApp(Tk):
    currentFrame = None

    def __init__(self, *args, **kwargs):
        global db_path

        Tk.__init__(self, *args, **kwargs)
        
        Tk.wm_title(self, "KetokMagicHalal")
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True) 
        
        
        self.frames = {}
        for F in ([PageOne]):
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack_forget()
        
        self.show_frame(PageOne)
        self.currentFrame.load_db(db_path)

    def show_frame(self, cont):
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = self.frames[cont]
        self.currentFrame.pack(side=TOP, fill=BOTH, expand=True, padx = 20, pady= 20)
        
        
        
if __name__ == '__main__':        
    app = MainApp()
    app.geometry("800x600")
    app.mainloop()
        
        
