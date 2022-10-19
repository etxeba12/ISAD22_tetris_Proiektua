import sqlite3

def datuBase():
    con = sqlite3.connect("erabiltzaile.db")

    try:
        con.execute("CREATE TABLE erabiltzaile(Izena, Pasahitza, Admin, Galdera1, Galdera2, Puntuazioa)")

        cur = con.cursor()
        cur.execute("""
                INSERT INTO erabiltzaile VALUES
                    ('Ipolla', 123, true, '12345678f', 'paco')
                """)
        con.commit()
    except sqlite3.OperationalError:
        print("La tabla articulos ya existe")
    con.close()
