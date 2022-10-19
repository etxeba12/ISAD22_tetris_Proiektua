import sqlite3

con = sqlite3.connect("datuBase.db")
cur = con.cursor()

def taulaSortu():
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='erabiltzaileak'")
    if(res.fetchone() is None):
        cur.execute("CREATE TABLE erabiltzaileak(izena VARCHAR(50) PRIMARY KEY, pasahitza VARCHAR(50), puntuazioa INT(10),galdera1 VARCHAR(50),galdera2 VARCHAR(50))")

def identifikatu(Izena,Pasahitza):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=? AND pasahitza=?",(Izena,Pasahitza))
    if(res.fetchone() is None):
        return False
    else:
        return True

def erregistratu(Izena,Pasahitza,Galdera1,Galdera2):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?",[Izena])
    if(res.fetchone() is None):
        cur.execute("INSERT INTO erabiltzaileak VALUES(?,?,0,?,?)",(Izena,Pasahitza,Galdera1,Galdera2))
        con.commit()
        return False
    else:
        return True



