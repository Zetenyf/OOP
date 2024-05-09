from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

class Szalloda:
    def __init__(self, nev, egyagyas_szobak_szama, ketagyas_szobak_szama):
        self.nev = nev
        self.szobak = []
        for i in range(egyagyas_szobak_szama):
            self.szobak.append(EgyagyasSzoba(i+1))
        for i in range(ketagyas_szobak_szama):
            self.szobak.append(KetagyasSzoba(i+1))

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                print("Ez a szoba már foglalt ezen a napon!")
                return
        foglalhato_szobak = [szoba for szoba in self.szalloda.szobak if szoba.szobaszam == szobaszam]
        if foglalhato_szobak:
            foglalas_szoba = foglalhato_szobak[0]
            self.foglalasok.append(Foglalas(foglalas_szoba, datum))
            print("Foglalás sikeres!")
        else:
            print("Nincs ilyen szobaszám a szállodában vagy már foglalt!")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Lemondás sikeres!")
                return
        print("Nincs ilyen foglalás!")

    def listazas(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"Szoba száma: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")
        else:
            print("Nincs foglalás a rendszerben.")

def main():
    szalloda = Szalloda("Példa Szálloda", 3, 2)  
    foglalaskezelo = FoglalasKezelo(szalloda)  

    # Példa foglalások hozzáadása a rendszerhez
    foglalaskezelo.foglalas(1, datetime.now() + timedelta(days=1))
    foglalaskezelo.foglalas(2, datetime.now() + timedelta(days=2))
    foglalaskezelo.foglalas(3, datetime.now() + timedelta(days=3))
    foglalaskezelo.foglalas(1, datetime.now() + timedelta(days=4))
    foglalaskezelo.foglalas(2, datetime.now() + timedelta(days=5))

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Választás (1/2/3/4): ")

        if valasztas == "1":
            print("Foglalható szobák:")
            for szoba in szalloda.szobak:
                print(f"Szoba száma: {szoba.szobaszam}, Ár: {szoba.ar}")
            szobaszam = int(input("Add meg a foglalni kívánt szoba számát: "))
            datum_str = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            foglalaskezelo.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = int(input("Add meg a lemondani kívánt foglalás szoba számát: "))
            datum_str = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            foglalaskezelo.lemondas(szobaszam, datum)
        elif valasztas == "3":
            foglalaskezelo.listazas()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
