import model.datuBase as db

Izena = ""
res = ()

class Pieza:
	def __init__(self, forma, kolorea):
		self.forma = forma
		self.kolorea = kolorea

	def get_kolorea(self):
		return self.kolorea
	def get_x(self, i):
		return self.forma[i][0]
	def get_y(self, i):
		return self.forma[i][1]

	def set_x(self, i,b):
		self.forma[i][0] = b
	def set_y(self, i,b):
		self.forma[i][1] = b

	def biratuEzkerrera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, aurr_y)
			self.set_y(i, -aurr_x)

	def biratuEskuinera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, -aurr_y)
			self.set_y(i, aurr_x)

	def min_x(self):
		return min([x[0] for x in self.forma])
	def min_y(self):
		return min([x[1] for x in self.forma])


class Laukia(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		super(Laukia, self).__init__([[0,0],[0,1],[1,0],[1,1]], kolorea=res[10])

class Zutabea(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[11])
		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea=res[11])

class Lforma(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[12])
		super(Lforma, self).__init__([[-1,-1],[0,-1],[0,0],[0,1]], kolorea=res[12])

class LformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[13])
		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea=res[13])


class Zforma(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[14])
		super(Zforma, self).__init__([[0,-1],[0,0],[-1,0],[-1,1]], kolorea=res[14])

class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[15])
		super(ZformaAlderantzizko, self).__init__([[0,-1],[0,0],[1,0],[1,1]], kolorea=res[15])

class Tforma(Pieza):
	def __init__(self, kolorea=None):
		res = db.kolorea_lortu(Izena)
		print(res[16])
		super(Tforma, self).__init__([[-1,0],[0,0],[1,0],[0,1]], kolorea=res[16])