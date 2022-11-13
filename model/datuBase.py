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
    #erabiltzaile izena badago komprobatzen dugu
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?",[Izena])
    if(res.fetchone() is None):
        #Erabiltzaile izena sartuta ez badago, sartzen dugu
        cur.execute("INSERT INTO erabiltzaileak VALUES(?,?,0,?,?)",(Izena,Pasahitza,Galdera1,Galdera2))
        con.commit()
        return False
    else:
        #bestela ez dugu sartzen
        return True

def datuakLortu(Izena):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?", [Izena])
    return res.fetchone()

def pasahitzaAldatu(izena,P1):
    res = cur.execute("UPDATE erabiltzaileak SET pasahitza=? WHERE izena=?",(P1,izena))
    con.commit()

def erabiltzaileGuztiakLortu():
    res = cur.execute("SELECT izena,puntuazioa FROM erabiltzaileak")
    return res.fetchall()

def erabiltzaileEzabatu(Izena):
    res = cur.execute("DELETE FROM erabiltzaileak WHERE izena=?",[Izena])
    con.commit()

def pasahitzaBerreskuratu(izena):
    res = cur.execute("SELECT izena,galdera1,galdera2 FROM erabiltzaileak WHERE izena=?", [izena])
    return res.fetchone()

def partidaGorde(Izena,partida,abi,puntuazioapartida,x,y):
    print(Izena)
    res = cur.execute("UPDATE erabiltzaileak SET gordeta=?,puntupartida=?,abiadura=?,x=?,y=? WHERE izena=?",(partida,puntuazioapartida,abi,x,y,Izena))
    con.commit()

def partidaBerreskuratu(Izena):
    res = cur.execute("SELECT gordeta,abiadura,puntupartida,x,y FROM erabiltzaileak WHERE izena=?", [Izena])
    return res.fetchone()
