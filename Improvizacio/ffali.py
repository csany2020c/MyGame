

class Ali:
    def __init__(self):
        self.ar: int = 0
        self.kiszalitasiar: int = 0
        self.learazas: bool (True)
        self.kiszalitasido: int = 0
        self.szarmazas: str = "transparent"

    def __str__(self) -> str:
        return "Ára = {a} Kiszálítás ára = {b} Megérkezési időpontja = {c} Származás = {f}".format(a= self.ar, b= self.kiszalitasiar, c= self.kiszalitasido, f=self.szarmazas)


adat = Ali()
adat.ar = 3.77 #HUF
adat.kiszalitasiar = 3256.02 #HUF
adat.kiszalitasido = 'Június 29.-én várható'
adat.szarmazas = 'Kína'
adat.learazas = bool
print(adat)

adat2 = Ali()
adat2.ar = 3.77 #HUF
adat2.kiszalitasiar = 0 #HUF
adat2.kiszalitasido = 'Július 1.-én várható'
adat2.szarmazas = 'Kína'
print(adat2)

adat3 = Ali()
adat3.ar = 18712.41#HUF
adat3.kiszalitasiar = 0 #HUF
adat3.kiszalitasido = 'Július 31.-én várható'
adat3.szarmazas = 'Kína'
print(adat3)

adat4 = Ali()
adat4.ar = 78690.63 #HUF
adat4.kiszalitasiar = 0 #HUF
adat4.kiszalitasido = 'Június 25.-én várható'
adat4.szarmazas = 'Törökország'
print(adat4)

adat5 = Ali()
adat5.ar = 3.77 #HUF
adat5.kiszalitasiar = 0 #HUF
adat5.kiszalitasido = 'Június 29.-én várható'
adat5.szarmazas = 'Kína'
print(adat5)

