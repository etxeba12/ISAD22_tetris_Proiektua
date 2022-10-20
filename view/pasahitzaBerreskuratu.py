import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db
import view.PasahitzaAldatu as pa

Izena = ""

class pasahitzaBerreskuratu():

    def __init__(self):
        super(pasahitzaBerreskuratu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title("Pasahitza Berreskuratu")

        def datuakJaso():
            izenaErabil = izenaErabiltzaile.get()
            g1 = Erabiltzaileerantzun1.get()
            g2 = Erabiltzaileerantzun2.get()
            self.datuakKonprobatu(izenaErabil,g1,g2)

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        # erabiltzaile izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3,relief="sunken",)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken")
        izenaErabiltzaile.pack()
        # erabiltzaile izena

        # 1.galdera
        galdera1 = tk.StringVar()
        galdera1.set("     ZEIN DA ZURE NAN ZENBAKIA?     ")

        galdera1label = tk.Label(self.window, textvariable=galdera1, borderwidth=3,relief="sunken",)
        galdera1label.pack()

        Erabiltzaileerantzun1 = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3,relief="sunken")
        Erabiltzaileerantzun1.pack()
        # 1.galdera

        # 2.galdera
        galdera2 = tk.StringVar()
        galdera2.set("ZEIN DA ZURE LEHEN MASKOTAREN IZENA?")

        galdera2label = tk.Label(self.window, textvariable=galdera2, borderwidth=3, relief="sunken", )
        galdera2label.pack()

        Erabiltzaileerantzun2 = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken" )
        Erabiltzaileerantzun2.pack()
        # 2.galdera

        #botoia onartu
        button = tk.Button(self.window, text="BERRESKURATU",command=(datuakJaso))
        button.pack()
        #botoia onartu


        self.window.mainloop()

    def datuakKonprobatu(self,izenaErabil,g1,g2):
        self.window.destroy()
        erantzun = db.pasahitzaBerreskuratu(izenaErabil)
        if erantzun is None:
            pasahitzaBerreskuratu()
        else:
            if erantzun[1] == g1:
                if erantzun[2] == g2:
                    pa.Izena = izenaErabil
                    pa.PasahitzaAldatu()
                else:
                    pasahitzaBerreskuratu()
            else:
                pasahitzaBerreskuratu()
