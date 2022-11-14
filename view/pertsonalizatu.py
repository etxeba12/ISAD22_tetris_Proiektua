import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import model.datuBase as db
import view.aukerenPantaila as ap

Izena = ""

class pertsonalizatu():

    def __init__(self):
        super(pertsonalizatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen Pertsonalizazioa")

        def datuakLortu():
            forma = comboLaukiak.get()
            kolorea = comboKoloreak.get()
            self.pertsonalizazioGorde(forma,kolorea)

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        laukia = tk.StringVar()
        laukia.set("  LAUKI BAT AUKERATU  ")

        laukialabel = tk.Label(self.window, textvariable=laukia, borderwidth=3, relief="sunken", )
        laukialabel.pack()

        #combobox laukiak
        comboLaukiak = ttk.Combobox(self.window, width=17)
        opciones = ["laukia", "zutabea", "lforma", "lformaAlderantzizko", "zforma", "zformaAlderantzizko", "tforma"]
        comboLaukiak['values'] = opciones
        comboLaukiak.pack()
        kolorea = tk.StringVar()
        kolorea.set("  KOLORE BAT AUKERATU  ")

        kolorelabel = tk.Label(self.window, textvariable=kolorea, borderwidth=3, relief="sunken", )
        kolorelabel.pack()

        #combobox Koloreak
        comboKoloreak = ttk.Combobox(self.window, width=17)
        opciones = ["yellow", "cyan", "blue", "orange", "green", "red", "purple"]
        comboKoloreak['values'] = opciones
        comboKoloreak.pack()


        #botoia gorde
        buttonGorde = tk.Button(self.window, text="ONARTU",command=(datuakLortu))
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=(self.bueltatu))
        buttonBueltatu.pack()

        self.window.mainloop()

    def pertsonalizazioGorde(self,forma,kolorea):
        print(forma,kolorea)
        db.kolore_Pertsonalizatu(Izena,forma,kolorea)
        self.window.destroy()
        ap.aukerenPantaila()

    def bueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()