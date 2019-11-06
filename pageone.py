from tkinter import *
from tkinter import  ttk, filedialog
from PIL import ImageTk, Image
from vector import *
from extract import *
from threading import Thread

LARGE_FONT = ('Verdana', 16)

image_path = None
db_path = 'pins.db'
db = None
t_compare = 3


class PageOne(Frame):
    # Frame utama, menghandle hampir semua fungsionalitas seperti membuka file gambar, melakukan
    # matching dan menampilkan gambar asal dan gambar hasil matching

    # Atribut
    sub1 = None
    
    fig1 = None
    
    matched_images = []
    disp_images = []

    imgname2 = None
    imgname3 = None
    imgname4 = None

    accuracy2 = None
    accuracy3 = None
    accuracy4 = None
    
    buttons = None
    lcanvas = None
    rcanvas = None
    msg = None
    mainframe = None

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

        self.lcanvas = Canvas(self.mainframe, borderwidth=4, relief = GROOVE, height = 360, width = 360)
        self.lcanvas.pack(side = LEFT)
        
        self.rcanvas = Canvas(self.mainframe, borderwidth=4, relief = GROOVE)
        self.rcanvas.pack(side = RIGHT, expand = True, fill = BOTH)

        button0 = ttk.Button(self.buttons, text="Pilih Gambar", command = lambda: self.SelectImage(controller))
        button0.grid(row = 2, column = 0, padx = (20, 20), sticky = "E")

        
        button2 = ttk.Button(self.buttons, text="Match (CS)", command = lambda: Thread(target = self.matchs, args = (True,)).start())
        button2.grid(row = 2, column = 1, padx = (20, 20), sticky = "W")
        
        button2 = ttk.Button(self.buttons, text="Match (ED)", command = lambda: Thread(target = self.matchs, args = (False,)).start())
        button2.grid(row = 2, column = 2, padx = (20, 20), sticky = "W")


    def draw_image(self):
        # Menampilkan gambar sumber yang akan diuji
        global image_path

        self.sub1 = ImageTk.PhotoImage(Image.open(image_path).resize((360, 360), Image.ANTIALIAS))
        if (self.fig1 is None):
            self.fig1 = self.lcanvas.create_image(0, 0, anchor = NW, image = self.sub1)
        else:
            self.lcanvas.itemconfig(self.fig1, image = self.sub1)

    def draw_matches(self):
        # Menampilkan hasil gambar yang "mirip" setelah dilakukan matching
        global t_compare
        for i in range(t_compare):
            if (i >= len(self.disp_images)):
                self.disp_images.append(dict())
            self.disp_images[i]['img'] = ImageTk.PhotoImage(Image.open(self.matched_images[i]['path']).resize((100, 100), Image.ANTIALIAS))
            if not ('fig' in self.disp_images[i].keys()):
                self.disp_images[i]['fig'] = self.rcanvas.create_image(20, 20 + 120 * i, anchor = NW, image = self.disp_images[i]['img'])
                self.disp_images[i]['str'] = '#' + str(i + 1) + '\nPath : ' + self.matched_images[i]['path'] + '\nSimilarity : ' + str(self.matched_images[i]['x'])
                self.disp_images[i]['text'] = self.rcanvas.create_text(140, 20 + 120 * i, anchor = NW, text = self.disp_images[i]['str'])
            else:
                self.rcanvas.itemconfig(self.disp_images[i]['fig'], image = self.disp_images[i]['img'])
                self.disp_images[i]['str'] = '#' + str(i + 1) + '\nPath : ' + self.matched_images[i]['path'] + '\nSimilarity : ' + str(self.matched_images[i]['x'])
                self.rcanvas.itemconfig(self.disp_images[i]['text'], text = self.disp_images[i]['str'])

    def SelectImage(self, controller):
        # Mengupload gambar uji
        global image_path
        upload_img = filedialog.askopenfilename(initialdir = "./", title = "Select file", filetypes =  (("jpeg files","*.jpg"),("all files","*.*")))
        print(type(upload_img), len(upload_img))
        if type(upload_img) == str:
            if len(upload_img) > 0:
                image_path = upload_img
                print(image_path)
                self.draw_image()
                self.msg.set('Opened %s.' %image_path.split('/')[-1])

    def load_db(self, path):
        # Memuat database yang telah dibuat
        global db
        if os.path.exists(path):
            dbfile = open('pins.db', 'rb')
            db = pickle.load(dbfile)
        else:
            self.msg.set('pins.db not found. Please run generate-pickle-file.py to generate it.')

    def matchs(self , use_cs):
        # Melakukan matching dan menghasilkan 3 gambar teratas yang paling "mirip"
        global db
        global t_compare
        global image_path
        if image_path is not None:
            self.buttons.pack_forget()
            self.msg.set('Extracting %s...' %image_path.split('/')[-1])
            self.matched_images = []
            dsc = extractFeatures(image_path)
            for compared_path in db:
                self.msg.set('\rMatching: %s' %compared_path)
                compared_data = dict()
                compared_data['path'] = compared_path
                compared_image = db[compared_path]
                if use_cs:
                    compared_data['x'] = calcCosineSimilarity(dsc, compared_image)
                else:
                    compared_data['x'] = calcEuclideanDistance(dsc, compared_image)
                self.matched_images.append(compared_data)
                self.matched_images = sorted(self.matched_images, key = lambda x: -x['x'])
                if len(self.matched_images) > t_compare:
                    self.matched_images = self.matched_images[0:t_compare]
        
            self.buttons.pack(side = BOTTOM, pady = 20)
            self.draw_matches()
            self.msg.set('Match with: ' + self.matched_images[0]['path'] + ' (' + str(self.matched_images[0]['x']) + ') ')
        else:
            self.msg.set('Open a file first.')


