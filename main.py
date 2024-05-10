from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_szoba_tipus(self):
        pass

    @abstractmethod
    def kiiras(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, kilatas, tv):
        super().__init__(ar=10000, szobaszam=szobaszam)
        self.kilatas = kilatas
        self.tv = tv

    def get_szoba_tipus(self):
        return "Egyágyas"

    def kiiras(self):
        print(f"Egyágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}, Kilátás: {self.kilatas}, TV: {self.tv}")

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, erkely, minihuto):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.erkely = erkely
        self.minihuto = minihuto

    def get_szoba_tipus(self):
        return "Kétágyas"

    def kiiras(self):
        print(f"Kétágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}, Erkély: {self.erkely}, Minihűtő: {self.minihuto}")

class Szalloda:
    def __init__(self, nev, csillag, ertekeles):
        self.nev = nev
        self.csillagszam = csillag
        self.ertekelesszam = ertekeles
        self.szobak = []
        self.foglalasok = []

    def plusz_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        try:
            foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
            if foglalas_datum < datetime.now():
                print("Nem tudsz foglalni múltbeli dátumra.")
                return None
        except ValueError:
            print("Hibás dátum formátum. Kérlek, add meg a dátumot az 'ÉÉÉÉ-HH-NN' formátumban.")
            return None

        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                print("A megadott szoba már foglalt ezen a dátumon.")
                return None
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas
        print("Nem található a megadott szobaszám.")
        return None

    def foglalas_ara(self, foglalas):
        return foglalas.szoba.ar

    def foglalas_lemondasa(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def foglalasok_listazasa(self):
        print(f"{self.nev} Szálloda foglalásai: ")
        for foglalas in self.foglalasok:
            foglalas.kiiras()

    def listaz_szobak(self):
        print(f"{self.nev} Szálloda szobái ({self.csillagszam} csillagos szálloda, {self.ertekelesszam}-es értékelésű az interneten):")
        for szoba in self.szobak:
            szoba.kiiras()

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def kiiras(self):
        print(f"Foglalás - Szobaszám: {self.szoba.szobaszam}, Ár: {self.szoba.ar}, Dátum: {self.datum}")

class bomba:
    def __init__(self, szalloda):
        self.szalloda = szalloda
    def main(self):
        while True:
            print("\nVálasszon egy műveletet:")
            print("1. Foglalás")
            print("2. Lemondás")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Adja meg a választott művelet számát: ")

            if valasztas == "1":
                self.lefoglalas()
            elif valasztas == "2":
                self.lemondas()
            elif valasztas == "3":
                self.foglalasok_listazasa()
            elif valasztas == "4":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás. Kérem, válasszon újra.")

    def lefoglalas(self):
        szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
        datum = input("Adja meg a foglalás dátumát (pl. 2024-05-15): ")
        foglalas = self.szalloda.foglal(szobaszam, datum)
        if foglalas:
            print("Sikeres foglalás!")
        else:
            print("Nem sikerült foglalni.")
            self.main()

    def lemondas(self):
        szobaszam = int(input("Adja meg a lemondani kívánt foglalás szobaszámát: "))
        datum = input("Adja meg a foglalás dátumát (pl. 2024-05-15): ")
        for foglalas in self.szalloda.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.szalloda.foglalas_lemondasa(foglalas)
                print("Sikeres lemondás!")
                return
        print("Nem sikerült lemondani. A megadott foglalás nem található.")

    def foglalasok_listazasa(self):
        foglalasok = self.szalloda.foglalasok_listazasa()
        if foglalasok:
            print("Foglalások:")
            for foglalas in foglalasok:
                foglalas.kiiras()

szalloda = Szalloda("A Legkomolyabb", 5, 4.7, )
szalloda.plusz_szoba(EgyagyasSzoba(101, "Városra", "Van"))
szalloda.plusz_szoba(KetagyasSzoba(201, "Van", "Van"))
szalloda.plusz_szoba(KetagyasSzoba(203, "Nincs", "Van"))
szalloda.listaz_szobak()

szalloda.foglal(101, "2024-05-25")
szalloda.foglal(101, "2024-05-26")
szalloda.foglal(201, "2024-05-27")
szalloda.foglal(203, "2024-05-28")
szalloda.foglal(203, "2024-05-29")

futas = bomba(szalloda)
futas.main()
