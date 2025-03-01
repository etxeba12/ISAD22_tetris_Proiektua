import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import model.datuBase as db
import view.PasahitzaAldatu as pa
import view.erabiltzaileaEzabatu as ez
import view.JokatuLeioa as jl
import view.Identifikatu as Id
import view.Pertsonalizatu as pp
import model.Piezak as pi
import view.rankingIkusi as ri
import view.sariakIkusi as si
Izena = " "
listaDatuak = ""
Maila = 1

class aukerenPantaila():

    def __init__(self):
        super(aukerenPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x600')
        self.window.title("Aukeren pantaila")
        self.window.configure(bg='white')
        pi.Izena = Izena
        pp.Izena = Izena

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img, bg='white')
        panel.pack(side="top", fill="both", expand="no")

        listaDatuak = db.datuakLortu(Izena)

        def datuakJaso():
            Maila = maila.get()
            self.jokatuleioa(Maila)

        #izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken",width=25,height=2)
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(value=listaDatuak[0]), state=tk.DISABLED,borderwidth=3, relief="sunken", width=29, )
        izenaErabiltzaile.pack()
        #izena

        # Puntuazioa
        puntuazioa = tk.StringVar()
        puntuazioa.set("        PUNTUAZIOA        ")

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, borderwidth=3, relief="sunken",width=25,height=2 )
        puntuazioalabel.pack()

        puntuazioErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(value=listaDatuak[2]), state=tk.DISABLED,borderwidth=3, relief="sunken", width=29, )
        puntuazioErabiltzaile.pack()
        #Puntuazioa

        # maila aukeratu
        aukeratumaila = tk.StringVar()
        aukeratumaila.set("    MAILA AUKERATU    ")

        aukeratumailalabel = tk.Label(self.window, textvariable=aukeratumaila, borderwidth=3, relief="sunken",width=25,height=2)
        aukeratumailalabel.pack()

        maila = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(),state=tk.NORMAL, borderwidth=3, relief="sunken", width=29, )
        maila.pack()

        buttonMaila = tk.Button(self.window, text="   MAILA AUKERATU   ", command=(datuakJaso),width=25,height=2)
        buttonMaila.pack()
        # maila aukeratu

        # raking aukeratu
        rankingIkusi = tk.Button(self.window, text="   RANKING   ", command=(self.rankingIkusi),width=25,height=2)
        rankingIkusi.pack()
        # raking aukeratu

        # botoia partida jarraitu
        if  (db.jarraituPartida(Izena)):
            buttonJarraituPa = tk.Button(self.window, text=" PARTIDA JARRAITU ", command=(self.partidaJarraitu),width=25,height=2)
            buttonJarraituPa.pack()
        # botoia partida jarraitu

        # botoia sariak
        buttonSariak = tk.Button(self.window, text=" SARIAK IKUSI ", command=(self.sariakIkusiJoan),
                                             width=25, height=2)
        buttonSariak.pack()
        # botoia sariak

        #botoia pertsonalizatu
        buttonPertsonalizatu = tk.Button(self.window, text=" PERTSONALIZATU ", command=(self.pertsonalizatu),width=25,height=2)
        buttonPertsonalizatu.pack()
        #botoia pertsonalizatu

        # botoia pasahitza
        buttonPasahitza = tk.Button(self.window, text=" PASAHITZA ALDATU ", command=(self.PasahitzaLehioa),width=25,height=2)
        buttonPasahitza.pack()
        # botoia pasahitza

        # botoia admin
        if (db.admin_da(Izena)):
            buttonAdmin = tk.Button(self.window, text=" EZABATU JOKALARI ", command=(self.ErabiltzaileEzabatu),width=25,height=2)
            buttonAdmin.pack()
        # botoia admin

        # botoia atzera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELTATU", command=(self.atzerabueltatu),width=25,height=2)
        button.pack()
        # botoia atzera bueltatu


        self.window.mainloop()

    def PasahitzaLehioa(self):
        self.window.destroy()
        pa.PasahitzaAldatu(False)

    def ErabiltzaileEzabatu(self):
        if db.admin_da(Izena):
            self.window.destroy()
            ez.erabiltzaileaEzabatu()
        else:
            messagebox.showinfo(message="Ez duzu hau egiteko baimena", title="BaimenikEz")
            self.window.destroy()
            aukerenPantaila()
    def rankingIkusi(self):
        self.window.destroy()
        ri.rankingIkusi("absolutua")

    def jokatuleioa(self,Maila):
        jl.partidaJarraitu=False
        tamaina = []
        jl.Izena = Izena
        jl.Kolorea= db.pantailaKolEman(Izena)
        jl.Musika=db.musEman(Izena)
        if(Maila == "1" or Maila == "2" or Maila == "3"):
            jl.Maila = Maila
            if(Maila == "1"):
                tamaina = [20,25]
                abiadura = int(400)
            elif(Maila == "2"):
                tamaina = [14, 22]
                abiadura = int(300)
            elif(Maila == "3"):
                tamaina = [10, 20]
                abiadura = int(200)
            self.window.destroy()
            jl.JokatuLeioa(tamaina,abiadura)
        else:
            messagebox.showinfo(message="Maila 1, 2 edo 3 izan behar da", title="Mailaerror")
            self.window.destroy()
            aukerenPantaila()

    def atzerabueltatu(self):
        self.window.destroy()
        Id.Identifikatu()

    def partidaJarraitu(self):
        self.window.destroy()
        jl.Izena = Izena
        jl.Kolorea = db.pantailaKolEman(Izena)
        jl.partidaJarraitu = True
        jl.JokatuLeioa.partida_jarraitu(self)

    def sariakIkusiJoan(self):
        si.Izena = Izena
        self.window.destroy()
        si.sariakIkusi()

    def pertsonalizatu(self):
        self.window.destroy()
        pp.Izena = Izena
        pp.Pertsonalizatu()