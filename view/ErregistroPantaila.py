import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db
import view.Identifikatu as Id

class ErregistroPantaila():

    Izena = ""
    Pasahitza = ""
    Galdera1 = ""
    Galdera2 = ""

    def __init__(self):
        super(ErregistroPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x350')
        self.window.configure(bg='white')
        self.window.title("Erregistro pantaila")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            Pasahitza = ErabiltzailePasahitza.get()
            Galdera1 = galdera1erantzun.get()
            Galdera2 = galdera2erantzun.get()
            self.erregistratu(Izena,Pasahitza,Galdera1,Galdera2)

        #izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", )
        izenaErabiltzaile.pack()
        #izena

        #pasahitza
        pasahitza = tk.StringVar()
        pasahitza.set("          PASAHITZA          ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3, relief="sunken", )
        pasahitzalabel.pack()

        ErabiltzailePasahitza = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                         show='*', borderwidth=3, relief="sunken", )
        ErabiltzailePasahitza.pack()
        #pasahitza

        #galdera 1 testua
        galdera1 = tk.StringVar()
        galdera1.set("   Zure NAN zenbakia   ")

        galdera1label = tk.Label(self.window, textvariable=galdera1, borderwidth=3, relief="sunken", )
        galdera1label.pack()

        galdera1erantzun = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", )
        galdera1erantzun.pack()
        #galdera 1 testua

        #galdera 2 testua
        galdera2 = tk.StringVar()
        galdera2.set("   1.animaliaren izena   ")

        galdera2label = tk.Label(self.window, textvariable=galdera2, borderwidth=3, relief="sunken", )
        galdera2label.pack()

        galdera2erantzun = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                    borderwidth=3, relief="sunken", )
        galdera2erantzun.pack()
        #galdera 2 testua

        # botoia erregistratu
        button = tk.Button(self.window, text="ERREGISTRATU", command=(datuakJaso))
        button.pack()
        # botoia erregistratu

        self.window.mainloop()

    def erregistratu(self,Izena,Pasahitza,Galdera1,Galdera2):
        self.window.destroy()
        print(Izena,Pasahitza,Galdera1,Galdera2)
        sartuta = db.erregistratu(Izena,Pasahitza,Galdera1,Galdera2)
        if(sartuta):
            ErregistroPantaila()
        else:
            Id.Identifikatu()
