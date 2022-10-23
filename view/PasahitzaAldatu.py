import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import model.datuBase as db
import view.aukerenPantaila as ap

Izena = ""

class PasahitzaAldatu():

    def __init__(self):
        super(PasahitzaAldatu, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.configure(bg='white')
        self.window.title("Pasahitza Aldatu")

        def datuakJaso():
            Pasahitza1 = pasahitzaErabiltzaile.get()
            Pasahitza2 = ErabiltzailePasahitza2.get()
            if len(Pasahitza2)==0 or len(Pasahitza1)==0 :
                messagebox.showinfo(message="Pasahitza hau ez du balio", title="PasahitzaError")
                self.window.destroy()
                PasahitzaAldatu()
            else:
                self.PasahitzaSartu(Pasahitza1, Pasahitza2)

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        # pasahitza lehenengo aldia
        pasahitza = tk.StringVar()
        pasahitza.set("    PASAHITZA SARTU    ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3,relief="sunken",)
        pasahitzalabel.pack()

        pasahitzaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,show='*', borderwidth=3, relief="sunken",)
        pasahitzaErabiltzaile.pack()
        # pasahitza lehenengo aldia

        # pasahitza bigarren aldia
        pasahitza2 = tk.StringVar()
        pasahitza2.set(" BERRIRO ERREPIKATU ")

        pasahitza2label = tk.Label(self.window, textvariable=pasahitza2, borderwidth=3,relief="sunken",)
        pasahitza2label.pack()

        ErabiltzailePasahitza2 = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,show='*', borderwidth=3,relief="sunken",)
        ErabiltzailePasahitza2.pack()

        #botoia ALDATU
        button = tk.Button(self.window, text="ALDATU",command=(datuakJaso))
        button.pack()
        #botoia ALDATU

        # botoia atzera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELTATU", command=(self.atzerabueltatu))
        button.pack()
        # botoia atzera bueltatu

        self.window.mainloop()

    def PasahitzaSartu(self,P1,P2):
        if(P1 == P2):
            db.pasahitzaAldatu(Izena,P1)
            ap.Izena = Izena
            self.window.destroy()
            ap.aukerenPantaila()
        else:
            messagebox.showinfo(message="Pasahitzak ez dira berdinak", title="PasahitzaError")
            self.window.destroy()
            PasahitzaAldatu()

    def atzerabueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()