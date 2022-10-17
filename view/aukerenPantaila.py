import tkinter as tk
from PIL import ImageTk, Image

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

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, borderwidth=3, relief="sunken", )
        puntuazioalabel.pack()

        puntuazioErabiltzaile = tk.Entry(self.window, justify=tk.CENTER, textvariable=tk.StringVar(), state=tk.NORMAL,
                                     borderwidth=3, relief="sunken", )
        puntuazioErabiltzaile.pack()
        # Puntuazioa


        self.window.mainloop()