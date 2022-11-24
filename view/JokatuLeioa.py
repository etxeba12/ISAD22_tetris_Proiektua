import random
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
import model.datuBase as db
import view.aukerenPantaila as ap
import pickle

Izena = " "
puntuazioa = " "
partidaJarraitu = False
tablerogordeta = []

class JokatuLeioa(object):
	"""docstring for JokatuLeioa"""
	def __init__(self,tamaina,abiadura):

		global abi

		abi = abiadura

		super(JokatuLeioa, self).__init__()
		self.window = tk.Tk()
		self.window.geometry('500x900')
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
		print(puntu)
		JokatuLeioa(tamaina,abiadura)

	def aukerenPantailaraJoan(self):
		self.window.destroy()
		ap.aukerenPantaila()

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
			print("i",i)
			for t in range(self.tab.tamaina[0]):
				print("t",t)
				if (self.tab.tab[i][t] != None):
					Gordetakopartida[i][t] = self.tab.tab[i][t]
		serializatua = pickle.dumps(Gordetakopartida)
		puntuazioapartida = self.tab.puntuazioa
		db.partidaGorde(Izena,serializatua,abi,puntuazioapartida,self.tab.tamaina[0],self.tab.tamaina[1])
		JokatuLeioa.aukerenPantailaraJoan(self.master_)

	def jolastu(self, button, window):
		button.pack_forget()
		buttonGorde = tk.Button(window, text=" PARTIDA GORDE ", command=self.partida_gorde)
		buttonGorde.pack()
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

