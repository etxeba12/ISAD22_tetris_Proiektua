import tkinter as tk
from PIL import ImageTk, Image
import view.JokatuLeioa as jl

class aukerenPantaila():

    def __init__(self):
        super(aukerenPantaila, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x220')
        self.window.title("Aukeren pantaila")

        img = ImageTk.PhotoImage(Image.open("tetris.png").reduce(2))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="top", fill="both", expand="no")

        #izena
        izena = tk.StringVar()
        izena.set("  ERABILTZAILE IZENA  ")

        izenalabel = tk.Label(self.window, textvariable=izena, borderwidth=3, relief="sunken", )
        izenalabel.pack()

        izenaErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", )
        izenaErabiltzaile.pack()
        #izena

        # Puntuazioa
        puntuazioa = tk.StringVar()
        puntuazioa.set("        PUNTUAZIOA        ")

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, borderwidth=3, relief="sunken" )
        puntuazioalabel.pack()

        puntuazioErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", )
        puntuazioErabiltzaile.pack()
        # Puntuazioa

        # Joko maila aukeratu
        serialEntry = tk.Entry(self.window)
        serialEntry.pack()
        mailaAukeratu = tk.Label(self.window,borderwidth=3, relief="sunken")
        mailaAukeratu.config(text="El codigo de serie es: " + serialEntry.get())
        serialEntry.bind("<Return>",self.jokatu)
        # Joko maila aukeratu

        # Pasahitza aldatu

        #pasahitza aldatu
        self.window.mainloop()

    def jokatu(self,arg):
        self.window.destroy()
        jl.JokatuLeioa()