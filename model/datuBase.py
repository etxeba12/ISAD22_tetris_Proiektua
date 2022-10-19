import sqlite3
import view.Identifikatu as id

con = sqlite3.connect("datuBase.db")
cur = con.cursor()

def taulaSortu():
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='erabiltzaileak'")
    if(res.fetchone() is None):
        cur.execute("CREATE TABLE erabiltzaileak(izena VARCHAR(50), pasahitza VARCHAR(50), puntuazioa INT(10),galdera1 VARCHAR(50),galdera2 VARCHAR(50))")

def identifikatu(Izena,Pasahitza):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena = Izena AND pasahitza=Pasahitza")
    print(res.fetchone())
    if(res.fetchone() is None):
        return False
    else:
        return True