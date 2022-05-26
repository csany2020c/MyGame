from typing import TextIO
from typing import List

class egercucc:
    def __init__(self):
        super().__init__()
        self.ar: str = "11383 Ft"
        self.marka: str = "razer"
        self.szallitasiido: str = "Max 7 nap"
        self.szallitasiar: str = "Ingyé"
        self.ertekeles: int = 4.8
        self.garancia: bool = True
        self.gombokszama: int = 5

    def __str__(self) -> str:
        return "Ár:{a} Márka:{s} Szállítási idő:{d} Szállítási ár{f} Értékelés:{g} Garancia:{h} Gombok száma:{j}".format(a=self.ar, s=self.marka, d=self.szallitasiido, f=self.szallitasiar, g=self.ertekeles, h=self.garancia, j=self.gombokszama)


eger = egercucc()
print(eger)