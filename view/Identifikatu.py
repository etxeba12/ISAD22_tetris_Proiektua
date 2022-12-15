import tkinter as tk
from PIL import ImageTk, Image
import view.aukerenPantaila as ap
import view.ErregistroPantaila as ep
import model.datuBase as db
import view.PasahitzaAldatu as pa
import view.pasahitzaBerreskuratu as pb
from tkinter import messagebox

Izena = ""
Pasahitza = ""

class Identifikatu():

    def __init__(self):
        super(Identifikatu, self).__init__()
        db.taulaSortu()
        self.window = tk.Tk()
        self.window.geometry('300x400')
        self.window.configure(bg='white')
        self.window.title("Erabiltzailearen identifikazioa")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            Pasahitza = ErabiltzailePasahitza.get()
            self.aukerenPantaila(Izena,Pasahitza)

        #Logoa
        self.img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        self.panel = tk.Label(self.window, image=self.img, bg='white')
        self.panel.pack(side="top", fill="both", expand="no")

        # Identifikatzeko datuak jarri
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  " )

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3,relief="sunken",width=25,height=2)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL, borderwidth=3, relief="sunken",width=25)
        izenaErabiltzaile.pack()

        pasahitza = tk.StringVar()
        pasahitza.set("          PASAHITZA          ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3,relief="sunken",width=25,height=2)
        pasahitzalabel.pack()

        ErabiltzailePasahitza = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,show='*', borderwidth=3,relief="sunken",width=25)
        ErabiltzailePasahitza.pack()

        #botoia onartu
        button = tk.Button(self.window, text="ONARTU",command=(datuakJaso),width=23,height=2)
        button.pack()
        #botoia onartu

        #etiketa erregistroa
        erregistroEtiqueta = tk.Label(self.window, text='ez zaude erregistratua?',width=25,height=2)
        erregistroEtiqueta.pack()
        erregistroEtiqueta.bind('<Button-1>', self.erregistroPantaila)
        #etiketa erregistroa

        # etiketa pasahitza berreskuratu
        pasahitzaEtiqueta = tk.Label(self.window, text='pasahitza ahaztu duzu?',width=25,height=2)
        pasahitzaEtiqueta.pack()
        pasahitzaEtiqueta.bind('<Button-1>', self.berreskuratu)
        # etiketa pasahitza berreskuratu

        self.window.mainloop()

    def aukerenPantaila(self,Izena,Pasahitza):
        # Izena eta Pasahitza zuzenak badira, aukerenPantaila lehioa zabalduko da, hau itxiz
        # bestela, errore mezua eta berriz saiatu
        ondo = db.identifikatu(Izena,Pasahitza)
        ap.Izena = Izena
        pa.Izena = Izena
        if(ondo):
            self.window.destroy()
            ap.aukerenPantaila()
        else:
            messagebox.showinfo(message="Erabiltzaile edo pasahitza txarto dago", title="ErabiltzaileTxartoIdentifikatu")
            self.window.destroy()
            Identifikatu()

    def erregistroPantaila(self,arg):
        # Erabiltzaile bat erregistratzeko lehioa zabaltzen du, hau itxiz.
        self.window.destroy()
        ep.ErregistroPantaila()

    def berreskuratu(self,arg):
        # Erabiltzaile bat pasahitza aldatzeko aukera ematen dion lehioa zabaltzen du, hau itxiz.
        self.window.destroy()
        pb.pasahitzaBerreskuratu()