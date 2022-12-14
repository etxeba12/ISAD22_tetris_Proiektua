import tkinter as tk
from PIL import ImageTk, Image
import model.datuBase as db
import view.Identifikatu as Id
from tkinter import messagebox

class ErregistroPantaila():

    Izena = ""
    Pasahitza = ""
    Galdera1 = ""
    Galdera2 = ""

    def __init__(self):
        super(ErregistroPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x540')
        self.window.configure(bg='white')
        self.window.title("Erregistro pantaila")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img,  bg='white')
        panel.pack(side="top", fill="both", expand="no")

        def datuakJaso():
            Izena = izenaErabiltzaile.get()
            Pasahitza = ErabiltzailePasahitza.get()
            Galdera1 = galdera1erantzun.get()
            Galdera2 = galdera2erantzun.get()
            self.erregistratu(Izena,Pasahitza,Galdera1,Galdera2)

        #izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken",width=25,height=2 )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken",width=25 )
        izenaErabiltzaile.pack()
        #izena

        #pasahitza
        pasahitza = tk.StringVar()
        pasahitza.set("          PASAHITZA          ")

        pasahitzalabel = tk.Label(self.window, textvariable=pasahitza, borderwidth=3, relief="sunken", width=25,height=2)
        pasahitzalabel.pack()

        ErabiltzailePasahitza = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                         show='*', borderwidth=3, relief="sunken", width=25)
        ErabiltzailePasahitza.pack()
        #pasahitza

        #galdera 1 testua
        galdera1 = tk.StringVar()
        galdera1.set("   Zure NAN zenbakia   ")

        galdera1label = tk.Label(self.window, textvariable=galdera1, borderwidth=3, relief="sunken",width=25,height=2 )
        galdera1label.pack()

        galdera1erantzun = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", width=25)
        galdera1erantzun.pack()
        #galdera 1 testua

        #galdera 2 testua
        galdera2 = tk.StringVar()
        galdera2.set("   1.animaliaren izena   ")

        galdera2label = tk.Label(self.window, textvariable=galdera2, borderwidth=3, relief="sunken",width=25,height=2 )
        galdera2label.pack()

        galdera2erantzun = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                    borderwidth=3, relief="sunken",width=25)
        galdera2erantzun.pack()
        #galdera 2 testua

        # botoia erregistratu
        button = tk.Button(self.window, text="ERREGISTRATU", command=(datuakJaso),width=25,height=2)
        button.pack()
        # botoia erregistratu

        # botoia atrera bueltatu
        button = tk.Button(self.window, text="ATZERA BUELATU", command=(self.atzerabueltatu),width=25,height=2)
        button.pack()
        # botoia atzera bueltatu

        self.window.mainloop()

    def erregistratu(self,Izena,Pasahitza,Galdera1,Galdera2):

        datuOnak= self.datuakKonrobatu(Izena,Pasahitza,Galdera1,Galdera2)

        if(datuOnak):
            erabilsartutadago = db.erregistratu(Izena, Pasahitza, Galdera1, Galdera2)
            if(erabilsartutadago):
                messagebox.showinfo(message="Izena hau hartuta dago", title="ErregistroError")
                self.window.destroy()
                ErregistroPantaila()
            else:
                self.window.destroy()
                Id.Identifikatu()
        else:
            messagebox.showinfo(message="Datu guztiak bete behar dira", title="ErregistroError")
            self.window.destroy()
            ErregistroPantaila()

    def atzerabueltatu(self):
        self.window.destroy()
        Id.Identifikatu()

    def datuakKonrobatu(self,Izena,Pasahitza,Galdera1,Galdera2):
        if len(Izena)==0 or len(Pasahitza)==0 or len(Galdera1)==0 or len(Galdera2)==0:
            return False
        else:
            return True
