import sqlite3

con = sqlite3.connect("datuBase.db")
cur = con.cursor()

def taulaSortu():
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='erabiltzaileak'")
    if(res.fetchone() is None):
        cur.execute("CREATE TABLE erabiltzaileak(izena VARCHAR(15) PRIMARY KEY, pasahitza VARCHAR(15), puntuazioa INT,"
                    "galdera1 VARCHAR(7),galdera2 VARCHAR(15),gordeta ," #TODO: GORDETA ZEIN MOTAKOA?
                    "puntupartida INT, abiadura INT, x int, y int, laukia VARCHAR(15), "
                    "zutabea VARCHAR(15), lforma VARCHAR(15), lforma VARCHAR(15),zforma VARCHAR(15),"
                    "tforma VARCHAR(15), admin BOOLEAN )")
        #TODO: CREATE TABLE BUKATU EGITEN
def insertZutabe():
     cur.execute("ALTER TABLE erabiltzaileak ADD pantaila VARCHAR(15)")
     cur.execute("ALTER TABLE erabiltzaileak ADD musika VARCHAR(15)")
def pantailaKolEguneratu(izena, kol):
    if not kolBera(izena, kol):
        erag = f"UPDATE erabiltzaileak SET pantaila='{kol}' WHERE izena='{izena}'"
        cur.execute(erag)
        con.commit()
def kolBera(izena, kol):
    erag = f"SELECT pantaila FROM erabiltzaileak WHERE izena='{izena}'"
    res = cur.execute(erag)
    ema = res.fetchone()
    # Ez bada gorde (None) orduan ez da jarraitu aukerarik
    return ema == kol

def pantailaKolEman(izena):
    erag = f"SELECT pantaila FROM erabiltzaileak WHERE izena='{izena}'"
    res = cur.execute(erag)
    ema = res.fetchone()
    return ema

def musikaEguneratu(izena, mus):
    if not musBera(izena, mus):
        erag = f"UPDATE erabiltzaileak SET musika='{mus}' WHERE izena='{izena}'"
        cur.execute(erag)
        con.commit()
def musBera(izena, mus):
    erag = f"SELECT musika FROM erabiltzaileak WHERE izena='{izena}'"
    res = cur.execute(erag)
    ema = res.fetchone()
    # Ez bada gorde (None) orduan ez da jarraitu aukerarik
    return ema == mus

def musEman(izena):
    erag = f"SELECT musika FROM erabiltzaileak WHERE izena='{izena}'"
    res = cur.execute(erag)
    ema = res.fetchone()
    return ema

def identifikatu(Izena,Pasahitza):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=? AND pasahitza=?",(Izena,Pasahitza))
    if(res.fetchone() is None):
        return False
    else:
        return True

def admin_eg(izena):
    if (izena == "Iker" or izena == "Miriam" or izena == "Imanol"):
        erag=f"UPDATE erabiltzaileak SET admin=True WHERE izena='{izena}'"
        cur.execute(erag)
        con.commit()


def erregistratu(izena,pasahitza,gald1,gald2):
    #erabiltzaile izena badago komprobatzen dugu
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?",[izena])
    badagoIzenBera=True
    if(res.fetchone() is None):
        #Erabiltzaile izena sartuta ez badago, sartzen dugu
        erag = f"INSERT INTO erabiltzaileak (izena, pasahitza, puntuazioa, galdera1, galdera2, admin, pantaila, musika) " \
               f"VALUES ('{izena}','{pasahitza}',0,'{gald1}','{gald2}', False, 'white', 'Tetris')"
        cur.execute(erag)
        con.commit()
        admin_eg(izena)
        badagoIzenBera= False
    return badagoIzenBera
def datuakLortu(Izena):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?", [Izena])
    return res.fetchone()

def jarraituPartida (izena):
    erag=f"SELECT gordeta FROM erabiltzaileak WHERE izena='{izena}'"
    res= cur.execute(erag)
    ema=res.fetchone()
    #Ez bada gorde (None) orduan ez da jarraitu aukerarik
    return not( ema[0] is None)

def admin_da(izena):
    erag=f"SELECT admin FROM erabiltzaileak WHERE izena='{izena}'"
    res = cur.execute(erag)
    ema= res.fetchone()
    return ema[0]

def pasahitzaAldatu(izena,P1):
    res = cur.execute("UPDATE erabiltzaileak SET pasahitza=? WHERE izena=?",(P1,izena))
    con.commit()

def erabiltzaileGuztiakLortu():
    res = cur.execute("SELECT izena,puntuazioa FROM erabiltzaileak")
    return res.fetchall()

def erabiltzaileMailakaLortu(maila):
    print(maila)
    res = cur.execute(f"SELECT izena,{maila} FROM erabiltzaileak")
    return res.fetchall()



def erabiltzaileEzabatu(Izena):
    res = cur.execute("DELETE FROM erabiltzaileak WHERE izena=?",[Izena])
    con.commit()

def pasahitzaBerreskuratu(izena):
    res = cur.execute("SELECT izena,galdera1,galdera2 FROM erabiltzaileak WHERE izena=?", [izena])
    return res.fetchone()

def partidaGorde(Izena,partida,abi,puntuazioapartida,x,y):
    res = cur.execute("UPDATE erabiltzaileak SET gordeta=?,puntupartida=?,abiadura=?,x=?,y=? WHERE izena=?",(partida,puntuazioapartida,abi,x,y,Izena))
    con.commit()

def partidaBerreskuratu(Izena):
    res = cur.execute("SELECT gordeta,abiadura,puntupartida,x,y FROM erabiltzaileak WHERE izena=?", [Izena])
    return res.fetchone()

def kolorea_lortu(Izena):
    res = cur.execute("SELECT * FROM erabiltzaileak WHERE izena=?", [Izena])
    return res.fetchone()

def kolore_Pertsonalizatu(Izena,forma,kolorea):
    if forma == "laukia":
        res = cur.execute("UPDATE erabiltzaileak SET laukia=? WHERE izena=?", (kolorea, Izena))
    elif forma == "zutabea":
        res = cur.execute("UPDATE erabiltzaileak SET zutabea=? WHERE izena=?", (kolorea, Izena))
    elif forma == "lforma":
        res = cur.execute("UPDATE erabiltzaileak SET lforma=? WHERE izena=?", (kolorea, Izena))
    elif forma == "lformaAlderantzizko":
        res = cur.execute("UPDATE erabiltzaileak SET lformaAlderantzizko=? WHERE izena=?", (kolorea, Izena))
    elif forma == "zforma":
        res = cur.execute("UPDATE erabiltzaileak SET zforma=? WHERE izena=?", (kolorea, Izena))
    elif forma == "zformaAlderantzizko":
        res = cur.execute("UPDATE erabiltzaileak SET zformaAlderantzizko=? WHERE izena=?", (kolorea, Izena))
    elif forma == "tforma":
        res = cur.execute("UPDATE erabiltzaileak SET tforma=? WHERE izena=?", (kolorea, Izena))
    con.commit()

def puntuazioGordeMailaka(Izena,puntuazioa,maila):
    puntuTotal = cur.execute("SELECT puntuazioa FROM erabiltzaileak WHERE izena=?", [Izena])
    ema1 = puntuTotal.fetchone()
    puntuTotala = ema1[0] + puntuazioa
    mailaOna = "maila" + str(maila)
    puntuMaila = cur.execute(f"SELECT {mailaOna} FROM erabiltzaileak WHERE izena=?", [Izena])
    ema2 = puntuMaila.fetchone()
    puntuMail = ema2[0] + puntuazioa
    res = cur.execute(f"UPDATE erabiltzaileak SET {mailaOna}=?,puntuazioa=? WHERE izena=?",
                      (puntuMail,puntuTotala,Izena))
    con.commit()

def sariaSartu(Izena,saria):
    sari = "sari" + str(saria)
    print(sari)
    sariKantitate= cur.execute(f"SELECT {sari} FROM erabiltzaileak WHERE izena=?", [Izena])
    ema1 = sariKantitate.fetchone()
    sariBerri = ema1[0] + 1
    res = cur.execute(f"UPDATE erabiltzaileak SET {sari}=? WHERE izena=?",
                      (sariBerri,Izena))
    con.commit()