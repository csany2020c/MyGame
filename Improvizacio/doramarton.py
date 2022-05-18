from typing import TextIO
from typing import List

class madar:
    def __init__(self):
        super().__init__()
        self.sebesseg: int
        self.enekes: bool
        self.ropkepes: bool
        self.ragadozo: bool


solyom = madar
solyom.sebesseg = 360
solyom.enekes = True
solyom.ropkepes = True
solyom.ragadozo = True

print(solyom.enekes)


class idojaras:
    def __init__(self):
        super().__init__()
        self.esos: bool
        self.napos: bool
        self.felhos: bool
        self.tornado: bool


ido = idojaras
ido.esos = True
ido.napos = False
ido.felhos = False
ido.tornado = True
print(ido.esos, ido.napos, ido.felhos, ido.tornado)


class fa:
    def __init__(self):
        super().__init__()
        self.fajta: str
        self.szelesseg: int
        self.magassag: int
        self.rohade: bool

fasize = fa
fasize.fajta = "bukk"
fasize.szelesseg = 50
fasize.magassag = 500
fasize.rohade = True
print(fasize.fajta, fasize.szelesseg, fasize.magassag, fasize.rohade)