from typing import TextIO
from typing import List

class egercucc:
    def __init__(self):
        super().__init__()
        self.ar: str
        self.marka: str
        self.szallitasiido: str
        self.szallitasiar: str
        self.ertekeles: int
        self.garancia: bool
        self.gombokszama: int

    def __str__(self) -> str:
        return "Ár:{a} Márka:{s} Szállítási idő:{d} Szállítási ár{f} Értékelés:{g} Garancia:{h} Gombok száma:{j}".format(a=self.ar, s=self.marka, d=self.szallitasiido, f=self.szallitasiar, g=self.ertekeles, h=self.garancia, j=self.gombokszama)


eger = egercucc()
eger.ar = "11383 Ft"
eger.marka = "razer"
eger.szallitasiido = "Max 7 nap"
eger.szallitasiar = "Ingyé"
eger.ertekeles = 4.8
eger.garancia = True
eger.gombokszama = 5
#print(eger)


list: egercucc()
lista: List = []
lista.append(eger)

for i in lista:
    print(i)
