import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import model.datuBase as db
import view.PasahitzaAldatu as pa
import view.erabiltzaileaEzabatu as ez

Izena = " "
listaDatuak = ""

class aukerenPantaila():

    def __init__(self):
        super(aukerenPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x280')
        self.window.title("Aukeren pantaila")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        listaDatuak = db.datuakLortu(Izena)

        #izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(value=listaDatuak[0]), state=tk.DISABLED,borderwidth=3, relief="sunken", )
        izenaErabiltzaile.pack()
        #izena

        # Puntuazioa
        puntuazioa = tk.StringVar()
        puntuazioa.set("        PUNTUAZIOA        ")

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, borderwidth=3, relief="sunken", )
        puntuazioalabel.pack()

        puntuazioErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(value=listaDatuak[2]), state=tk.DISABLED,borderwidth=3, relief="sunken", )
        puntuazioErabiltzaile.pack()
        # Puntuazioa

        # botoia maila
        buttonMaila = tk.Button(self.window, text="   MAILA AUKERATU   ", command=())
        buttonMaila.pack()
        # botoia maila

        # botoia pasahitza
        buttonPasahitza = tk.Button(self.window, text=" PASAHITZA ALDATU ", command=(self.PasahitzaLehioa))
        buttonPasahitza.pack()
        # botoia pasahitza

        # botoia admin
        buttonAdmin = tk.Button(self.window, text=" EZABATU JOKALARI ", command=(self.ErabiltzaileEzabatu))
        buttonAdmin.pack()
        # botoia admin


        self.window.mainloop()

    def PasahitzaLehioa(self):
        self.window.destroy()
        pa.PasahitzaAldatu()

    def ErabiltzaileEzabatu(self):
        if Izena == "iker" or Izena == "imanol":
            self.window.destroy()
            ez.erabiltzaileaEzabatu()
        else:
            messagebox.showinfo(message="Ez duzu hau egiteko baimena", title="BaimenikEz")
            self.window.destroy()
            aukerenPantaila()

