import tkinter as tk
from PIL import ImageTk, Image
import  view.PertsonalizazioAukera as per
import view.aukerenPantaila as ap

Izena = ""

class Pertsonalizatu():

    def __init__(self):
        super(Pertsonalizatu, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title(" Pertsonalizazio aukerak")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img, bg='white')
        panel.pack(side="top", fill="both", expand="no")

        per.Izena=Izena

        # Adreilu aldatzeko botoia
        adreiluaAldButton = tk.Button(self.window, text="ADREILU KOLOREA ALDATU",
                                      command=self.piezaAukera)
        adreiluaAldButton.pack()
        # Adreilu aldatzeko botoia

        # Pantaila aldatzeko botoia
        pantailaAlButton = tk.Button(self.window, text="PANTAILA KOLOREA ALDATU",
                                     command=self.pantailaAukera )
        pantailaAlButton.pack()
        # Pantaila aldatzeko botoia

        # Musika aldatzeko botoia
        musikaAldButton = tk.Button(self.window, text="      MUSIKA ALDATU      ", command=self.musikaAukera)
        musikaAldButton.pack()
        # Musika aldatzeko botoia

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu)
        buttonBueltatu.pack()


        self.window.mainloop()

    def pantailaAukera(self):
        self.window.destroy()
        per.Aukera=1
        per.PertsonalizazioAukera()

    def piezaAukera(self):
        self.window.destroy()
        per.Aukera = 2
        per.PertsonalizazioAukera()

    def musikaAukera(self):
        self.window.destroy()
        per.Aukera = 3
        per.PertsonalizazioAukera()

    def bueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()
