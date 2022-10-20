import tkinter as tk
from PIL import ImageTk, Image
import view.aukerenPantaila as ap
import view.ErregistroPantaila as ep
import model.datuBase as db
import view.PasahitzaAldatu as pa

Izena = ""
Pasahitza = ""

class pasahitzaBerreskuratu():

    def __init__(self):
        super(pasahitzaBerreskuratu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('220x250')
        self.window.configure(bg='white')
        self.window.title("Pasahitza Berreskuratu")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            Pasahitza = ErabiltzailePasahitza.get()
            self.aukerenPantaila(Izena,Pasahitza)

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        # erabiltzaile izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3,relief="sunken",)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken",)
        izenaErabiltzaile.pack()
        # erabiltzaile izena

        # 1.galdera
        pasahitza = tk.StringVar()
        pasahitza.set("          PASAHITZA          ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3,relief="sunken",)
        pasahitzalabel.pack()

        ErabiltzailePasahitza = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,show='*', borderwidth=3,relief="sunken",)
        ErabiltzailePasahitza.pack()
        # 1.galdera
        #botoia onartu
        button = tk.Button(self.window, text="BERRESKURATU",command=(datuakJaso))
        button.pack()
        #botoia onartu


        self.window.mainloop()