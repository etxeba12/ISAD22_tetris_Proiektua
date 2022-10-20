import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db
import view.aukerenPantaila as ap

Izena = ""

class erabiltzaileaEzabatu():

    def __init__(self):
        super(erabiltzaileaEzabatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen identifikazioa")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            self.ezabatuErabil(Izena)

        zer = db.erabiltzaileGuztiakLortu()
        for i in zer:
            bat = tk.StringVar()
            bat.set("  ERABILTZAILE IZENA  ")

            Infolabel = tk.Label(self.window, textvariable=tk.StringVar(value=str(i[0]) + " → Puntuazioa: " + str(i[1])), borderwidth=3, relief="sunken", )
            Infolabel.pack()

        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken", )
        izenaErabiltzaile.pack()

        # botoia ezabatu
        button = tk.Button(self.window, text="EZABATU", command=(datuakJaso))
        button.pack()
        # botoia ezabatu

    def ezabatuErabil(self,Izena):
        db.erabiltzaileEzabatu(Izena)
        self.window.destroy()
        ap.aukerenPantaila()