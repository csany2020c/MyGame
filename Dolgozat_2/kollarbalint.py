from typing import List
def feladat1():
    szam1 = int(input())
    szam2 = int(input())
    kisebb: int = 0
    lista = list()

    if szam1 < szam2:
        kisebb = szam1
    if szam2 < szam1:
        kisebb = szam2
    if kisebb > -1:
        for i in range(-1, kisebb):
            lista.append(i + 1)
    else:
        for b in range(0, kisebb, -1):
            lista.append(b)

    print(lista)
feladat1()

def feladat2():
    lista = list()

    while True:
        szam = int(input())
        try:
            if szam <= -1:
                break
            if szam >= 0:
                lista.append(szam)
        except:
            pass
    print(lista[0])
    print(lista[len(lista) -1])

feladat2()

class Kosar:

    def __init__(self) -> None:
        super().__init__()
        self.nev: str
        self.ar: int
        self.tomeg: int

lista: List['Kosar'] = list()

termek1 = Kosar()
termek1.nev = "Dob"
termek1.ar = 5000
termek1.tomeg = 2

termek2 = Kosar()
termek2.nev = "Laptop"
termek2.ar = 150000
termek2.tomeg = 3

termek3 = Kosar()
termek3.nev = "Könyv"
termek3.ar = 1500
termek3.tomeg = 1

lista.append(termek1)
lista.append(termek2)
lista.append(termek3)
osszeg: int = 0
for i in lista:
    osszeg += i.ar
print(osszeg)



