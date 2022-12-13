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
        izenalabel.pack()

        if(maila == "absolutua"):
            zer = db.erabiltzaileGuztiakLortu()
        else:
            zer = db.erabiltzaileMailakaLortu(maila)
        zerOrdenatu = sorted(zer, key=lambda zer: zer[1],reverse=True)
        i = 0
        while i < 5:
            bat = tk.StringVar()
            bat.set("  ERABILTZAILE IZENA  ")

            Infolabel = tk.Label(self.window, textvariable=tk.StringVar(value=str(zerOrdenatu[i][0]) + " → Puntuazioa: " + str(zerOrdenatu[i][1])), borderwidth=3, relief="sunken", width=25,height=2)
            Infolabel.pack(pady=5)
            i = i + 1

        rankingaukeratu = tk.StringVar()
        rankingaukeratu.set("  LAUKI BAT AUKERATU  ")

        rankingaukeratulabel = tk.Label(self.window, textvariable=rankingaukeratu, borderwidth=3, relief="sunken", )
        rankingaukeratulabel.pack()

        # combobox ranking
        comboranking = ttk.Combobox(self.window, width=17, state="readonly")
        opciones = ["maila1", "maila2" ,"maila3", "absolutua"]
        comboranking['values'] = opciones
        comboranking.pack()

        buttonGorde = tk.Button(self.window, text="ONARTU",command=lambda: self.rankingEguneratu(comboranking))
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="Bueltatu", command=self.bueltatu)
        buttonBueltatu.pack()

    def rankingEguneratu(self,comboranking):
        ik = comboranking.get()
        self.window.destroy()
        rankingIkusi(str(ik))

    def bueltatu(self):
        self.window.destroy()
        ap.aukerenPantaila()