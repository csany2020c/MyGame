from typing import List

class Ali:
    def __init__(self) -> None:
        self.ar: int = 0
        self.kiszalitasiar: int = 0
        self.learazas: str
        self.kiszalitasido: str
        self.szarmazas: str = "transparent"

    def __str__(self) -> str:
        return "Ára = {a} Kiszálítás ára = {b} Megérkezési időpontja = {c} Le van Árazva? = {d} Származás = {f} Összár = {g}".format(a= self.ar, b= self.kiszalitasiar, c= self.kiszalitasido, d=self.learazas ,f=self.szarmazas,g=self.osszar)

    def osszar(self) -> int:
        return self.ar + self.kiszalitasiar

adat = Ali()
adat.ar = 3.77 #HUF
adat.kiszalitasiar = 3256.02 #HUF
adat.kiszalitasido = 'Június 29.-én várható'
adat.szarmazas = 'Kína'
adat.learazas = 'Igen'
print(adat)


adat2 = Ali()
adat2.ar = 3.77 #HUF
adat2.kiszalitasiar = 0 #HUF
adat2.kiszalitasido = 'Július 1.-én várható'
adat2.szarmazas = 'Kína'
adat2.learazas = 'Igen'
print(adat2)

adat3 = Ali()
adat3.ar = 18712.41#HUF
adat3.kiszalitasiar = 0 #HUF
adat3.kiszalitasido = 'Július 31.-én várható'
adat3.szarmazas = 'Kína'
adat3.learazas = 'Igen'
print(adat3)

adat4 = Ali()
adat4.ar = 78690.63 #HUF
adat4.kiszalitasiar = 0 #HUF
adat4.kiszalitasido = 'Június 25.-én várható'
adat4.szarmazas = 'Törökország'
adat4.learazas = 'Igen'
print(adat4)

adat5 = Ali()
adat5.ar = 3.77 #HUF
adat5.kiszalitasiar = 0 #HUF
adat5.kiszalitasido = 'Június 29.-én várható'
adat5.szarmazas = 'Kína'
adat5.learazas = 'Igen'
print(adat5)

list = Ali()
lista:list = []
lista.append(adat)
lista.append(adat2)
lista.append(adat3)
lista.append(adat4)
lista.append(adat5)
print(lista)

