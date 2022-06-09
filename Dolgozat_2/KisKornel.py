from typing import List


def feladat1():
    elso:int = int(input())
    masodik:int = int(input())
    legkisebbik: int = min(elso, masodik)
    if legkisebbik > 0:
        for i in range(0, legkisebbik + 1):
            print(i)

    if legkisebbik <= -1:
        for x in range(0, legkisebbik - 1):

            print(x)

#print(feladat1())


def feladat2():
    valami:int = int(input())
    lista:List[valami] = list()


#print(feladat2())







class Termek:
    def __init__(self) -> None:
        self.nev:str = ""
        self.ar:int = 0
        self.tomeg:int = 0

    def __str__(self) -> str:
        return "A Termék neve: {a}, Ára {b} Ft, Tömege: {c} kg".format(a=self.nev, b=self.ar, c=self.tomeg)

Elsotermek = Termek()
Elsotermek.nev = "Szeletelt kenyér"
Elsotermek.ar = 1000
Elsotermek.tomeg = 1
#print(Elsotermek)
Masodiktermek = Termek()
Masodiktermek.nev = "Tojás"
Masodiktermek.ar = 1200
Masodiktermek.tomeg = 2
#print(Masodiktermek)
Harmadiktermek = Termek()
Harmadiktermek.nev = "Csirkemell"
Harmadiktermek.ar = 9000
Harmadiktermek.tomeg = 3
#print(Harmadiktermek)
lista: List[Termek] = list()
lista.append(Elsotermek)
lista.append(Masodiktermek)
lista.append(Harmadiktermek)
lista.append(Elsotermek.ar + Masodiktermek.ar + Harmadiktermek.ar)
for i in lista:
    print(i)


