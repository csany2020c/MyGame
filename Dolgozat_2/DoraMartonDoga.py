from typing import *

def elso():
    szam1 = int(input())
    szam2 = int(input())
    if min(szam1, szam2) > 0 or min(szam1, szam2) == 0:
        for i in range(0, min(szam1, szam2) + 1):
            print(i)
    if min(szam1, szam2) < 0:
        for a in range(min(szam1, szam2), 1):
            print(a)

#elso()

def masodik():
    while True:
        bemenet = int(input())
        lista: List['int'] = list()
        if bemenet > 0 or bemenet == 0:
            print("Adjon meg új számot!")
            lista.append(bemenet)
            pass
        if bemenet < 0:
            for h in lista:
                print(h)
            break

masodik()

class bevasarlas:
    def __init__(self) -> None:
        super().__init__()
        self.nev = str
        self.ar = int
        self.tomeg = str

    def __str__(self) -> str:
        return "Áru neve: {a} Ár: {s} Tömeg: {d}".format(a=self.nev, s=self.ar, d=self.tomeg)

termek1 = bevasarlas()
termek1.nev = "alma"
termek1.ar = 100
termek1.tomeg = "50 gram"

termek2 = bevasarlas()
termek2.nev = "banán"
termek2.ar = 200
termek2.tomeg = "100 gram"

termek3 = bevasarlas()
termek3.nev = "kóla"
termek3.ar = 300
termek3.tomeg = "250 gram"

bevasarlolista = list()
bevasarlolista.append(termek1)
bevasarlolista.append(termek2)
bevasarlolista.append(termek3)

osszar: int = 0

for i in bevasarlolista:
    osszar = termek1.ar + termek2.ar + termek3.ar

#print(osszar)