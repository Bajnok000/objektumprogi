from abc import ABC, abstractmethod

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

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        print(f"{self.nev} szálloda szobái ({self.csillagszam} csillagos szálloda, {self.ertekelesszam}-es értékelésű az interneten):")
        for szoba in self.szobak:
            szoba.kiiras()
            print()

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def kiiras(self):
        print(f"Foglalás - Szobaszám: {self.szoba.szobaszam}, Ár: {self.szoba.ar}, Dátum: {self.datum}")


# Példa használat:
szalloda = Szalloda("A Legkomolyabb", 5, 4.7,)
szalloda.add_szoba(EgyagyasSzoba("101", "Városra", "Van"))
szalloda.add_szoba(KetagyasSzoba("201", "Van", "Van"))
szalloda.listaz_szobak()
print("gitproba")
print("gitproba2")
print("gitproba3333")