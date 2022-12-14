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
        hiztegia_kol = {
            "horia": "yellow",
            "zian": "cyan",
            "urdina": "blue",
            "laranja": "orange",
            'berdea': "green",
            'gorria': "red",
            'morea': "purple",
            'zuria':"white",
        }
        kolorea = hiztegia_kol[comboKoloreak.get()]
        db.kolore_Pertsonalizatu(Izena, forma, kolorea)
        self.apBueltatu()

    def adreiluAldatu(self, comboKoloreak):
        laukia = tk.StringVar()
        laukia.set("  LAUKI BAT AUKERATU  ")

        laukialabel = tk.Label(self.window, textvariable=laukia, borderwidth=3, relief="sunken",width=25,height=2 )
        laukialabel.pack()

        #combobox laukiak
        comboLaukiak = ttk.Combobox(self.window, width=26,state="readonly")
        opciones = ["laukia", "zutabea", "lforma", "lformaAlderantzizko", "zforma", "zformaAlderantzizko", "tforma"]
        comboLaukiak['values'] = opciones
        comboLaukiak.current(0)
        comboLaukiak.pack()

        #botoia gorde

        buttonGorde = tk.Button(self.window, text="ONARTU",command=lambda:self.pertsonalizazioGorde(comboLaukiak,comboKoloreak),width=25,height=2)
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="BUELTATU", command=self.bueltatu,width=25,height=2)
        buttonBueltatu.pack()


    def koloreaAldatu(self, pantaila):
        kolorea = tk.StringVar()
        kolorea.set("  KOLORE BAT AUKERATU  ")

        kolorelabel = tk.Label(self.window, textvariable=kolorea, borderwidth=3, relief="sunken",width=25,height=2 )
        kolorelabel.pack()

        # combobox Koloreak
        comboKoloreak = ttk.Combobox(self.window, width=26,state="readonly")
        opcionesEus=['horia','zian','urdina','laranja','berdea','gorria','morea','zuria']
        comboKoloreak['values'] = opcionesEus
        comboKoloreak.pack()
        hiztegia_kol = {
            "yellow": "horia",
            "cyan": "zian",
            "blue": "urdina",
            "orange": "laranja",
            'green': "berdea",
            'red': "gorria",
            'purple': "morea",
            'white':"zuria",
        }
        if pantaila:
            kolor = db.pantailaKolEman(Izena)
            ema = hiztegia_kol.get(str(kolor[0]))
            comboKoloreak.current(opcionesEus.index(str(ema)))
            # botoia gorde
            buttonGorde = tk.Button(self.window, text="ONARTU", command=lambda:self.pantailaKolAld(comboKoloreak),width=25,height=2 )
            buttonGorde.pack()

            buttonBueltatu = tk.Button(self.window, text="BUELTATU", command=self.bueltatu,width=25,height=2)
            buttonBueltatu.pack()

        else:
            comboKoloreak.current(0)
            self.adreiluAldatu(comboKoloreak)

    def pantailaKolAld(self, comboKolorea):
        hiztegia_kol = {
            "horia": "yellow",
            "zian": "cyan",
            "urdina": "blue",
            "laranja": "orange",
            'berdea': "green",
            'gorria': "red",
            'morea': "purple",
            'zuria':"white",
        }
        print(comboKolorea.get())
        db.pantailaKolEguneratu(Izena,hiztegia_kol[comboKolorea.get()])
        if db.kolBera(Izena, comboKolorea.get()):
            messagebox.showinfo(message="Kolore horrekin dago jada pamtaila", title="KoloreBera")
        self.apBueltatu()

    def musikaAukeratu(self):
        musika = tk.StringVar()
        musika.set("  MUSIKA BAT AUKERATU  ")

        musikalabel = tk.Label(self.window, textvariable=musika, borderwidth=3, relief="sunken",width=25,height=2 )
        musikalabel.pack()

        # combobox Koloreak
        comboMusikak = ttk.Combobox(self.window, width=26,state="readonly")
        opciones = ["Help", "LaFlaca", "Tetris", "Thunderstruck"]
        comboMusikak['values'] = opciones
        musi = db.musEman(Izena)
        comboMusikak.current(opciones.index(str(musi[0])))
        comboMusikak.pack()

         # botoia gorde
        buttonGorde = tk.Button(self.window, text="ONARTU", command=lambda:self.musikaAldatu(comboMusikak),width=25,height=2 )
        buttonGorde.pack()

        buttonBueltatu = tk.Button(self.window, text="BUELTATU", command=self.bueltatu,width=25,height=2)
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