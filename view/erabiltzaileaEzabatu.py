import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db

Izena = ""

class erabiltzaileaEzabatu():

    def __init__(self):
        super(erabiltzaileaEzabatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('220x250')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen identifikazioa")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        zer = db.erabiltzaileGuztiakLortu()
        print(zer)

        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken", )
        izenaErabiltzaile.pack()

        # botoia ezabatu
        button = tk.Button(self.window, text="EZABATU", command=())
        button.pack()
        # botoia ezabatu