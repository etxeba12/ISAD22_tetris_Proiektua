import random
import multiprocessing
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
import model.datuBase as db
import view.aukerenPantaila as ap
import pickle
from playsound import playsound
from pygame import mixer

Izena = " "
Maila = " "
puntuazioa = " "
partidaJarraitu = False
tablerogordeta = []
bostenMultiploak = [5, 15, 25, 35,45]  # jarraian 5 partida (5000 puntu irabazteagatik) pasatzeagatik, premio hobea
Kolorea = " "


class JokatuLeioa(object):
	"""docstring for JokatuLeioa"""
	def __init__(self,tamaina,abiadura):

		global abi, musikaHasi

		abi = abiadura
		self.musikaHasi = False

		super(JokatuLeioa, self).__init__()
		self.window = tk.Tk()
		self.window.geometry('500x900')
		if db.kolBera(Izena,Kolorea):
			kolorea=db.pantailaKolEman(Izena)

		self.window.configure(bg=kolorea)
		self.window.title("Tetris jokoa")

		button = tk.Button(self.window, text="PARTIDA HASI")
		button.pack()

		# botoia pasahitza
		buttonAtzera=tk.Button (self.window, text=" ATZERA BUELTATU ", command=self.aukerenPantailaraJoan)
		buttonAtzera.pack()
		# botoia pasahitza

		puntuazioa = tk.StringVar()
		puntuazioa.set("Puntuazioa: 0")

		puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa)
		puntuazioalabel.pack()

		self.canvas = TableroaPanela(master=self.window,Tamaina=tamaina, puntuazioalabel=puntuazioa, master2=self)
		button.configure(command=lambda: self.canvas.jolastu(button, self.window))
		self.canvas.pack()
		self.window.bind("<Up>", self.canvas.joku_kontrola)
		self.window.bind("<Down>", self.canvas.joku_kontrola)
		self.window.bind("<Right>", self.canvas.joku_kontrola)
		self.window.bind("<Left>", self.canvas.joku_kontrola)

		self.window.mainloop()


	def partida_jarraitu(self):
		global tablerogordeta
		global puntu
		partidaDatuak = db.partidaBerreskuratu(Izena)
		partida = pickle.loads(partidaDatuak[0])
		tablerogordeta = partida
		tamaina = [partidaDatuak[3],partidaDatuak[4]]
		abiadura = partidaDatuak[1]
		puntu = partidaDatuak[2]
		JokatuLeioa(tamaina,abiadura)

	def aukerenPantailaraJoan(self):
		self.window.destroy()
		self.musikaGelditu()
		ap.aukerenPantaila()


	def musikaEntzun(self):
		Musika=db.musEman(Izena)
		mus = str(Musika)
		musika = mus[2:len(Musika) - 4]
		mus = musika
		erag = f"{mus}.mp3"
		mixer.init()  # Initialzing pyamge mixer
		mixer.music.load(erag)  # Loading Music File
		self.musikaHasi=True
		mixer.music.play()  # Playing Music with Pygame

	def musikaGelditu(self):
		if self.musikaHasi:
			mixer.music.stop()

class TableroaPanela(tk.Frame):

	def __init__(self, Tamaina, gelazka_tamaina=20,puntuazioalabel=None, master=None, master2=None):
		tk.Frame.__init__(self, master)

		self.puntuazio_panela = puntuazioalabel
		self.tamaina = Tamaina
		self.gelazka_tamaina = gelazka_tamaina
		self.master_ = master2

		self.canvas = tk.Canvas(
			width=self.tamaina[0]  * self.gelazka_tamaina+1,
			height=self.tamaina[1] * self.gelazka_tamaina+1,
			bg='#eee', borderwidth=0, highlightthickness=0
		)
		self.canvas.pack(expand=tk.YES, fill=None)

		self.tab = Tableroa(Tamaina)
		self.jokatzen = None
		self.tableroa_ezabatu()


	def marratu_gelazka(self, x,y,color):
		self.canvas.create_rectangle(x*self.gelazka_tamaina, y*self.gelazka_tamaina,(x+1)*self.gelazka_tamaina, (y+1)*self.gelazka_tamaina, fill=color)

	def tableroa_ezabatu(self):
		self.canvas.delete("all")
		self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina, self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

	def marraztu_tableroa(self):
		self.tableroa_ezabatu()
		for i in range(self.tab.tamaina[1]):
			for j in range(self.tab.tamaina[0]):
				if self.tab.tab[i][j]:
					self.marratu_gelazka(j,i,self.tab.tab[i][j])
		if self.tab.pieza:
			for i in range(4):
				x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
				y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
				self.marratu_gelazka(y,x,self.tab.pieza.get_kolorea())
		self.puntuazioa_eguneratu()

	def pausu_bat(self):
		try:
			self.tab.betetako_lerroak_ezabatu()
			self.tab.mugitu_behera()
			partidaIrabaziak = self.tab.puntuazioa // 100  # 1000 puntu heltzerakoan, partida bat irabazten duzula suposatu dugu
			print(partidaIrabaziak)
			print(partidaIrabaziak in bostenMultiploak)
			if (partidaIrabaziak in bostenMultiploak):
				bostenMultiploak.pop(0)
				db.sariaSartu(Izena, "Handiak")
		except Exception as error:
			try:
				self.tab.pieza_finkotu(self.tab.posizioa)
				pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
				self.tab.sartu_pieza(random.choice(pieza_posibleak)())
			except Exception as e:
				print("GAMEOVER")
				self.tab.hasieratu_tableroa()
				return
		self.jokatzen = self.after(abi, self.pausu_bat)
		self.marraztu_tableroa()

	def puntuazioa_eguneratu(self):
		if self.puntuazio_panela:
			self.puntuazio_panela.set(f"Puntuazioa: {(self.tab.puntuazioa)}")

	def joku_kontrola(self, event):
		try:
			if event.keysym == 'Up':
				self.tab.biratu_pieza()
			if event.keysym == 'Down':
				self.tab.pieza_kokatu_behean()
			if event.keysym == 'Right':
				self.tab.mugitu_eskumara()
			if event.keysym == 'Left':
				self.tab.mugitu_ezkerrera()
		except Exception as error:
			pass
		finally:
			self.marraztu_tableroa()

	def partida_gorde(self):
		self.after_cancel(self.jokatzen)
		Gordetakopartida = [[ None for x in range(self.tamaina[0])]for y in range(self.tamaina[1])]
		for i in range(self.tab.tamaina[1]):
			for t in range(self.tab.tamaina[0]):
				if (self.tab.tab[i][t] != None):
					Gordetakopartida[i][t] = self.tab.tab[i][t]
		db.puntuazioGordeMailaka(Izena,self.tab.puntuazioa,Maila)
		serializatua = pickle.dumps(Gordetakopartida)
		puntuazioapartida = self.tab.puntuazioa
		db.partidaGorde(Izena,serializatua,abi,puntuazioapartida,self.tab.tamaina[0],self.tab.tamaina[1])
		JokatuLeioa.aukerenPantailaraJoan(self.master_)


	def jolastu(self, button, window):

		button.configure(text=" PARTIDA GORDE ", command=self.partida_gorde)
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
		if not partidaJarraitu:
			self.tab.hasieratu_tableroa()
		else:
			self.tab.kopiatu_tableroa(tablerogordeta,puntu)
		pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
		self.tab.sartu_pieza(random.choice(pieza_posibleak)())
		self.marraztu_tableroa()
		self.jokatzen = self.after(400, self.pausu_bat)
		JokatuLeioa.musikaEntzun(self.master_)


