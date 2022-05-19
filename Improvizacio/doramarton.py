from typing import TextIO
from typing import List

class madar:
    def __init__(self):
        super().__init__()
        self.sebesseg: int = 360
        self.enekes: bool = True
        self.ropkepes: bool = True
        self.ragadozo: bool = True

    def __str__(self) -> str:
        return "sebesség:{a}\t énekes-e:{s}\t röpképes-e:{d}\t ragadozó-e:{f}".format(a=self.sebesseg, s=self.enekes, d=self.ropkepes, f=self.ragadozo)

solyom = madar()
#solyom.sebesseg = 360
#solyom.enekes = True
#solyom.ropkepes = True
#solyom.ragadozo = True

#print(solyom)

class fa:
    def __init__(self):
        super().__init__()
        self.fajta: str
        self.szelesseg: int
        self.magassag: int
        self.rohade: bool
    def __str__(self) -> str:
        return "fajta: {a}\t szelesség: {s}\t magasság: {d}\t rohad-e: {f}".format(a=self.fajta, s=self.szelesseg, d=self.magassag, f=self.rohade)


fasize1 = fa()
fasize1.fajta = "Bükkk"
fasize1.szelesseg = 50
fasize1.magassag = 500
fasize1.rohade = True
#print(fasize1)

fasize2 = fa()
fasize2.fajta = "Fenyő"
fasize2.szelesseg = 60
fasize2.magassag = 700
fasize2.rohade = False
#print(fasize2)

fasize3 = fa()
fasize3.fajta = "Tölgy"
fasize3.szelesseg = 40
fasize3.magassag = 400
fasize3.rohade = False
#print(fasize3)

class idojaras:
    def __init__(self):
        super().__init__()
        self.esos: bool
        self.napos: bool
        self.felhos: bool
        self.tornado: bool

    def __str__(self) -> str:
        return "asd: {a}\t asd: {s}\t asd: {d}\t asd: {f}".format(a=self.esos, s=self.napos, d=self.felhos, f=self.tornado)


ido = idojaras()
esos = input("Esős az idő(I/N)")
if esos == "I":
    ido.esos = True
print(ido)