from typing import List

class Ali:
    def __init__(self) -> None:
        self.ar = 0
        self.kiszalitasiar: int = 0
        self.learazas: bool = False
        self.kiszalitasido: str = ""
        self.szarmazas: str = "transparent"

    def __str__(self) -> str:
        return "Ára = {a} Kiszálítás ára = {b} Megérkezési időpontja = {c} Le van Árazva? = {d} Származás = {f} Összár = {g}".format(a= self.ar, b= self.kiszalitasiar, c= self.kiszalitasido, d=self.learazas ,f=self.szarmazas,g=self.osszar)

    def osszar(self) -> int:
        return self.ar + self.kiszalitasiar

def boololvas(elem: str) -> bool:
    be: str = input(elem + "i/n:")
    if be == "i" or be == "y":
        return True
    if be == "n":
        return False

def intolvas(elem:str, min: int = 0, max: int = 100) -> int:
    be: str = input(elem +" (" + str(min) + " - " + str(max) + "): ")
    try:
        j: int = int(be)
        if j >= min and j <= max:
            return j
        else:
            print("Nem jó értéket adtál meg! Nem tartozik az intervallumban a szám!")
    except:
        print("Nem jó értéket adtál meg! Próbáld újra!")


def strbool(érték: str) -> bool:
    if érték == "i" or érték == "y" or érték == "true":
        return True
    if érték == "n" or érték == "true":
        return False
    return None




adat = Ali()
adat.ar = 3.77 #HUF
adat.kiszalitasiar = 3256.02 #HUF
adat.kiszalitasido = 'Június 29.-én várható'
adat.szarmazas = 'Kína'
adat.learazas = True
print(adat)


adat2 = Ali()
adat2.ar = 3.77 #HUF
adat2.kiszalitasiar = 0 #HUF
adat2.kiszalitasido = 'Július 1.-én várható'
adat2.szarmazas = 'Kína'
adat2.learazas = True
print(adat2)

adat3 = Ali()
adat3.ar = 18712.41#HUF
adat3.kiszalitasiar = 0 #HUF
adat3.kiszalitasido = 'Július 31.-én várható'
adat3.szarmazas = 'Kína'
adat3.learazas = True
print(adat3)

adat4 = Ali()
adat4.ar = 78690.63 #HUF
adat4.kiszalitasiar = 0 #HUF
adat4.kiszalitasido = 'Június 25.-én várható'
adat4.szarmazas = 'Törökország'
adat4.learazas = False
print(adat4)

adat5 = Ali()
adat5.ar = 3.77 #HUF
adat5.kiszalitasiar = 0 #HUF
adat5.kiszalitasido = 'Június 29.-én várható'
adat5.szarmazas = 'Kína'
adat5.learazas = True
print(adat5)

list = Ali()
lista:list = []
lista.append(adat)
lista.append(adat2)
lista.append(adat3)
lista.append(adat4)
lista.append(adat5)

for i in lista:
    print(i)

a = Ali()
a.ar = intolvas("Kérem az árát:", 1, 9999999)
a.kiszalitasiar = intolvas("Kérem az kiszálítás árát:", 0, 9999999)
a.learazas = boololvas("Le van árazva?")
lista.append(a)
