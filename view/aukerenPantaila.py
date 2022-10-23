import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import model.datuBase as db
import view.PasahitzaAldatu as pa
import view.erabiltzaileaEzabatu as ez
import view.JokatuLeioa as jl
import view.Identifikatu as Id

Izena = " "
listaDatuak = ""
Maila = 1

class aukerenPantaila():

    def __init__(self):
        super(aukerenPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x340')
        self.window.title("Aukeren pantaila")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        listaDatuak = db.datuakLortu(Izena)

        def datuakJaso():
            Maila = maila.get()
            self.jokatuleioa(Maila)

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

        # maila aukeratu
        aukeratumaila = tk.StringVar()
        aukeratumaila.set("    MAILA AUKERATU    ")

        aukeratumailalabel = tk.Label(self.window, textvariable=aukeratumaila, borderwidth=3, relief="sunken", )
        aukeratumailalabel.pack()

        maila = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(),state=tk.NORMAL, borderwidth=3, relief="sunken", )
        maila.pack()

        buttonMaila = tk.Button(self.window, text="   MAILA AUKERATU   ", command=(datuakJaso))
        buttonMaila.pack()
        # maila aukeratu

        # botoia pasahitza
        buttonPasahitza = tk.Button(self.window, text=" PASAHITZA ALDATU ", command=(self.PasahitzaLehioa))
        buttonPasahitza.pack()
        # botoia pasahitza

        # botoia admin
        buttonAdmin = tk.Button(self.window, text=" EZABATU JOKALARI ", command=(self.ErabiltzaileEzabatu))
        buttonAdmin.pack()
        # botoia admin

        # botoia atzera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELTATU", command=(self.atzerabueltatu))
        button.pack()
        # botoia atzera bueltatu


        self.window.mainloop()

    def PasahitzaLehioa(self):
        self.window.destroy()
        pa.PasahitzaAldatu()

    def ErabiltzaileEzabatu(self):
        if Izena == "iker" : #aplikazioaren administratzaile bakarra da
            self.window.destroy()
            ez.erabiltzaileaEzabatu()
        else:
            messagebox.showinfo(message="Ez duzu hau egiteko baimena", title="BaimenikEz")
            self.window.destroy()
            aukerenPantaila()

    def jokatuleioa(self,Maila):
        tamaina = []
        if(Maila == "1" or Maila == "2" or Maila == "3"):
            if(Maila == "1"):
                tamaina = [20,40]
                abiadura = int(400)
            elif(Maila == "2"):
                tamaina = [15, 30]
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