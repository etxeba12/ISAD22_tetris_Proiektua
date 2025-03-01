import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db
import view.aukerenPantaila as ap
from tkinter import messagebox

Izena = ""

class erabiltzaileaEzabatu():

    def __init__(self):
        super(erabiltzaileaEzabatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('300x450')
        self.window.configure(bg='white')
        self.window.title("Ezabatu jokalari")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img, bg='white')
        panel.pack(side="top", fill="both", expand="no")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            self.ezabatuErabil(Izena)

        zer = db.erabiltzaileGuztiakLortu()
        for i in zer:
            bat = tk.StringVar()
            bat.set("  ERABILTZAILE IZENA  ")

            Infolabel = tk.Label(self.window, textvariable=tk.StringVar(value=str(i[0]) + " → Puntuazioa: " + str(i[1])), borderwidth=3, relief="sunken",width=25,height=2 )
            Infolabel.pack()

        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", width=25,height=2)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken", width=29)
        izenaErabiltzaile.pack()

        # botoia ezabatu
        button = tk.Button(self.window, text="EZABATU", command=(datuakJaso),width=25,height=2)
        button.pack()
        # botoia ezabatu

        # botoia atzera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELTATU", command=(self.atzerabueltatu),width=25,height=2)
        button.pack()
        # botoia atzera bueltatu

    def ezabatuErabil(self,Izena):
        if(Izena != "Iker" and Izena != "Miriam" and Izena != "Imanol"):
            db.erabiltzaileEzabatu(Izena)
        else:
            messagebox.showinfo(message="erabiltzaile hau ezin da ezabatu", title="errorea")
        self.window.destroy()
        ap.aukerenPantaila()

    def atzerabueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()

