import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import model.datuBase as db
import view.aukerenPantaila as ap

Izena = ""

class sariakIkusi():

    def __init__(self):
        super(sariakIkusi, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x600')
        self.window.title("Sariak pantaila")
        self.window.configure(bg='white')

        # Logoa
        self.img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        self.panel = tk.Label(self.window, image=self.img, bg='white')
        self.panel.pack(side="top", fill="both", expand="no")

        izena = tk.StringVar()
        izena.set("  SARIAK  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", width=15, height=2)
        izenalabel.pack(pady=4)

        zer = db.erabiltzaileSariakLortu(Izena)
        print(zer)
        maila = 0
        while maila < 4:
            bat = tk.StringVar()
            bat.set("  ERABILTZAILE IZENA  ")

            Infolabel = tk.Label(self.window,
                                 textvariable=tk.StringVar(value=str(Izena) + " → saria maila " + str(maila + 1) + ": " + str(zer[maila])),
                                 borderwidth=3, relief="sunken", width=25, height=2)
            Infolabel.pack(pady=2)
            maila = maila + 1

        # botoia atzera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELTATU", command=(self.atzerabueltatu), width=25, height=2)
        button.pack()
       # botoia atzera bueltatu

    def atzerabueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()