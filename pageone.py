from tkinter import *
from tkinter import  ttk, filedialog
from PIL import ImageTk, Image
from vector import *
from extract import *
from threading import Thread
import recog

LARGE_FONT = ('Verdana', 16)

image_path = None
db_path = 'pins.db'
db = None
t_compare = 10


class PageOne(Frame):
    # Frame utama, menghandle hampir semua fungsionalitas seperti membuka file gambar, melakukan
    # matching dan menampilkan gambar asal dan gambar hasil matching

    # Atribut
    sub1 = None
    
    fig1 = None
    text1 = None

    matched_images = []
    disp_images = []

    buttons = None
    lcanvas = None
    rcanvas = None
    msg = None
    mainframe = None

    scroll = 0
    score_name = 'Score'

    def __init__(self, parent, controller):
        # Menginisiasi frame
        Frame.__init__(self, parent)
        global image_path
        label = ttk.Label(self, text="Ketok Magic Halal", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
            
        self.msg = StringVar()
        ttk.Label(self, textvariable=self.msg).pack(side = BOTTOM)
        self.msg.set('Welcome')
        
        self.buttons = Frame(self)
        self.buttons.pack(side = BOTTOM, pady = 20)
        
        self.mainframe = Frame(self)
        self.mainframe.pack(side = TOP, expand = True, fill = BOTH);

        button_up = ttk.Button(self.mainframe, text="Up", command = lambda: self.b_up())
        button_up.pack(side = TOP)

        button_down = ttk.Button(self.mainframe, text="Down", command = lambda: self.b_down())
        button_down.pack(side = BOTTOM)

        self.lcanvas = Canvas(self.mainframe, borderwidth=4, relief = GROOVE, height = 400, width = 360)
        self.lcanvas.pack(side = LEFT)
        
        self.rcanvas = Canvas(self.mainframe, borderwidth=4, relief = GROOVE)
        self.rcanvas.pack(side = RIGHT, expand = True, fill = BOTH)

        self.button0 = ttk.Button(self.buttons, text="Open Image", command = lambda: self.SelectImage(controller))    
        self.button1 = ttk.Button(self.buttons, text="Match (CS)", command = lambda: Thread(target = recog.matchs, args = (image_path, db, t_compare, True, self)).start())
        self.button2 = ttk.Button(self.buttons, text="Match (ED)", command = lambda: Thread(target = recog.matchs, args = (image_path, db, t_compare, False, self)).start())
        self.show_buttons()
    
    def show_buttons(self):
        self.button0.grid(row = 2, column = 0, padx = (20, 20), sticky = "E")
        self.button1.grid(row = 2, column = 1, padx = (20, 20), sticky = "W")
        self.button2.grid(row = 2, column = 2, padx = (20, 20), sticky = "W")
    
    def hide_buttons(self):
        self.button0.grid_forget()
        self.button1.grid_forget()
        self.button2.grid_forget()
 
    def draw_image(self):
        # Menampilkan gambar sumber yang akan diuji
        global image_path

        self.sub1 = ImageTk.PhotoImage(Image.open(image_path).resize((360, 360), Image.ANTIALIAS))
        if (self.fig1 is None):
            self.fig1 = self.lcanvas.create_image(0, 0, anchor = NW, image = self.sub1)
            self.text1 = self.lcanvas.create_text(10, 370, anchor = NW, text = image_path.split('/')[-1])
        else:
            self.lcanvas.itemconfig(self.fig1, image = self.sub1)
            self.lcanvas.itemconfig(self.text1, text = image_path.split('/')[-1])

    def draw_matches(self):
        # Menampilkan hasil gambar yang "mirip" setelah dilakukan matching
        global t_compare
        self.reset_scroll()
        for i in range(len(self.matched_images)):
            if (i >= len(self.disp_images)):
                self.disp_images.append(dict())
            self.disp_images[i]['img'] = ImageTk.PhotoImage(Image.open(self.matched_images[i]['path']).resize((100, 100), Image.ANTIALIAS))
            if not ('fig' in self.disp_images[i].keys()):
                self.disp_images[i]['fig'] = self.rcanvas.create_image(20, 20 + 120 * i, anchor = NW, image = self.disp_images[i]['img'])
                self.disp_images[i]['str'] = '#' + str(i + 1) + '\nPath : ' + self.matched_images[i]['path'] + '\n' + self.score_name + ' : ' + str(self.matched_images[i]['x'])
                self.disp_images[i]['text'] = self.rcanvas.create_text(140, 20 + 120 * i, anchor = NW, text = self.disp_images[i]['str'])
            else:
                self.rcanvas.itemconfig(self.disp_images[i]['fig'], image = self.disp_images[i]['img'])
                self.disp_images[i]['str'] = '#' + str(i + 1) + '\nPath : ' + self.matched_images[i]['path'] + '\n' + self.score_name + ' : ' + str(self.matched_images[i]['x'])
                self.rcanvas.itemconfig(self.disp_images[i]['text'], text = self.disp_images[i]['str'])

    def update_scroll(self, ds):
        self.scroll += ds
        for i in range(len(self.disp_images)):
            self.rcanvas.move(self.disp_images[i]['fig'], 0, -120 * ds)
            self.rcanvas.move(self.disp_images[i]['text'], 0, -120 * ds)

    def reset_scroll(self):
        self.update_scroll(-self.scroll)

    def b_up(self):
        if self.scroll > 0:
            self.update_scroll(-1)

    def b_down(self):
        global t_compare
        if self.scroll < len(self.disp_images) - 1:
            self.update_scroll(1)


    def SelectImage(self, controller):
        # Mengupload gambar uji
        global image_path
        upload_img = filedialog.askopenfilename(initialdir = "./", title = "Select file", filetypes =  (("jpeg files","*.jpg"),("all files","*.*")))
        if type(upload_img) == str:
            if len(upload_img) > 0:
                image_path = upload_img
                self.draw_image()
                self.msg.set('Opened %s.' %image_path.split('/')[-1])

    def load_db(self, path):
        # Memuat database yang telah dibuat
        global db
        if os.path.exists(path):
            dbfile = open('pins.db', 'rb')
            db = pickle.load(dbfile)
        else:
            self.buttons.pack_forget()
            self.msg.set('pins.db not found. Please run generate-pickle-file.py to generate it.')

