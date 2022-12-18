import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import model.datuBase as db
import view.aukerenPantaila as ap


class rankingIkusi():

    def __init__(self,maila):
        super(rankingIkusi, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x600')
        self.window.title("Ranking pantaila")
        self.window.configure(bg='white')

        izena = tk.StringVar()
        izena.set("  RANKING  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", width=15,height=2)
        izenalabel.pack(pady=4)

        if(maila == "absolutua"):
            zer = db.erabiltzaileGuztiakLortu()
        else:
            zer = db.erabiltzaileMailakaLortu(maila)
            print(zer)
        zerOrdenatu = sorted(zer, key=lambda zer: zer[1],reverse=True)
        i = 0
        if(len(zerOrdenatu)< 5):
            luzera = len(zerOrdenatu)
        else:
            luzera = 5
        while i < luzera:
            bat = tk.StringVar()
            bat.set("  ERABILTZAILE IZENA  ")

            Infolabel = tk.Label(self.window, textvariable=tk.StringVar(value=str(zerOrdenatu[i][0]) + " → Puntuazioa: " + str(zerOrdenatu[i][1])), borderwidth=3, relief="sunken", width=25,height=2)
            Infolabel.pack(pady=2)
            i = i + 1

        rankingaukeratu = tk.StringVar()
        rankingaukeratu.set("  LAUKI BAT AUKERATU  ")

        rankingaukeratulabel = tk.Label(self.window, textvariable=rankingaukeratu, borderwidth=3, relief="sunken", width=25, height=2 )
        rankingaukeratulabel.pack(pady=2)

        # combobox ranking
        comboranking = ttk.Combobox(self.window, width=27, state="readonly",)
        opciones = ["1", "2" ,"3", "absolutua"]
        comboranking['values'] = opciones
        comboranking.current(3)
        comboranking.pack(pady=2)

        buttonGorde = tk.Button(self.window, text="ONARTU",command=lambda: self.rankingEguneratu(comboranking), width=25, height=2)
        buttonGorde.pack(pady=2)

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu, width=25, height=2)
        buttonBueltatu.pack()

    def rankingEguneratu(self,comboranking):
        ik = comboranking.get()
        self.window.destroy()
        rankingIkusi(str(ik))

    def bueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()