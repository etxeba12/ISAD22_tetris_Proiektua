import tkinter as tk
from PIL import ImageTk, Image
import view.aukerenPantaila as ap
import view.ErregistroPantaila as ep
import model.datuBase as db


class Identifikatu():

    Izena = ""
    Pasahitza = ""

    def __init__(self):
        super(Identifikatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('220x250')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen identifikazioa")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            Pasahitza = ErabiltzailePasahitza.get()
            self.aukerenPantaila(Izena,Pasahitza)

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3,relief="sunken",)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken",)
        izenaErabiltzaile.pack()


        pasahitza = tk.StringVar()
        pasahitza.set("          PASAHITZA          ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3,relief="sunken",)
        pasahitzalabel.pack()

        ErabiltzailePasahitza = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,show='*', borderwidth=3,relief="sunken",)
        ErabiltzailePasahitza.pack()

        #botoia onartu
        button = tk.Button(self.window, text="ONARTU",command=(datuakJaso))
        button.pack()
        #botoia onartu

        #etiketa erregistroa
        erregistroEtiqueta = tk.Label(self.window, text='Ez zaude erregistratua?')
        erregistroEtiqueta.pack()
        erregistroEtiqueta.bind('<Button-1>', self.erregistroPantaila)
        #etiketa erregistroa

        self.window.mainloop()


    def aukerenPantaila(self,Izena,Pasahitza):
        self.window.destroy()
        ondo = db.identifikatu(Izena,Pasahitza)
        if(ondo):
            ap.aukerenPantaila()
            print("aukeren pantaila")
        else:
            Identifikatu()
            print("identifikatu")

    def erregistroPantaila(self,arg):
        self.window.destroy()
        ep.ErregistroPantaila()


