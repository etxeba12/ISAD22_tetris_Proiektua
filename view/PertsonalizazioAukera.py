import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import model.datuBase as db
import view.Pertsonalizatu as per
import view.aukerenPantaila as ap

Izena = ""
Aukera=0
class PertsonalizazioAukera():

    def __init__(self):
        super(PertsonalizazioAukera, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen Pertsonalizazioa")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img, bg='white')
        panel.pack(side="top", fill="both", expand="no")

        if Aukera==1:
            self.koloreaAldatu(True)
        if Aukera==2:
            self.koloreaAldatu(False)
        if Aukera==3:
            self.musikaAukeratu()

        self.window.mainloop()

    def pertsonalizazioGorde(self, comboLaukiak, comboKoloreak):
        forma = comboLaukiak.get()
        kolorea = comboKoloreak.get()
        db.kolore_Pertsonalizatu(Izena, forma, kolorea)
        self.apBueltatu()

    def adreiluAldatu(self, comboKoloreak):
        laukia = tk.StringVar()
        laukia.set("  LAUKI BAT AUKERATU  ")

        laukialabel = tk.Label(self.window, textvariable=laukia, borderwidth=3, relief="sunken", )
        laukialabel.pack()

        #combobox laukiak
        comboLaukiak = ttk.Combobox(self.window, width=17)
        opciones = ["laukia", "zutabea", "lforma", "lformaAlderantzizko", "zforma", "zformaAlderantzizko", "tforma"]
        comboLaukiak['values'] = opciones
        comboLaukiak.pack()

        #botoia gorde

        buttonGorde = tk.Button(self.window, text="ONARTU",command=lambda:self.pertsonalizazioGorde(comboLaukiak,comboKoloreak))
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu)
        buttonBueltatu.pack()


    def koloreaAldatu(self, pantaila):
        kolorea = tk.StringVar()
        kolorea.set("  KOLORE BAT AUKERATU  ")

        kolorelabel = tk.Label(self.window, textvariable=kolorea, borderwidth=3, relief="sunken", )
        kolorelabel.pack()

        # combobox Koloreak
        comboKoloreak = ttk.Combobox(self.window, width=17)
        opciones = ["yellow", "cyan", "blue", "orange", "green", "red", "purple"]
        comboKoloreak['values'] = opciones
        comboKoloreak.pack()
        if pantaila:
            # botoia gorde
            buttonGorde = tk.Button(self.window, text="ONARTU", command=lambda:self.pantailaKolAld(comboKoloreak)  )
            buttonGorde.pack()

            buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu)
            buttonBueltatu.pack()

        else:
            self.adreiluAldatu(comboKoloreak)

    def pantailaKolAld(self, comboKolorea):
        db.pantailaKolEguneratu(Izena, comboKolorea.get())
        if db.kolBera(Izena, comboKolorea.get()):
            messagebox.showinfo(message="Kolore horrekin dago jada pamtaila", title="KoloreBera")
        self.apBueltatu()

    def musikaAukeratu(self):
        musika = tk.StringVar()
        musika.set("  MUSIKA BAT AUKERATU  ")

        musikalabel = tk.Label(self.window, textvariable=musika, borderwidth=3, relief="sunken", )
        musikalabel.pack()

        # combobox Koloreak
        comboMusikak = ttk.Combobox(self.window, width=17)
        opciones = ["Help", "LaFlaca", "Tetris", "Thunderstruck"]
        comboMusikak['values'] = opciones
        comboMusikak.pack()

         # botoia gorde
        buttonGorde = tk.Button(self.window, text="ONARTU", command=lambda:self.musikaAldatu(comboMusikak) )
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu)
        buttonBueltatu.pack()


    def musikaAldatu(self, comboMusikak):
        db.musikaEguneratu(Izena, comboMusikak.get())
        if db.musBera(Izena, comboMusikak.get()):
            messagebox.showinfo(message="Kolore horrekin dago jada pamtaila", title="KoloreBera")
        self.apBueltatu()

    def apBueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()

    def bueltatu(self):
        self.window.destroy()
        per.Pertsonalizatu()