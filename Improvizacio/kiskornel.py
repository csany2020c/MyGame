from typing import TextIO
from typing import List

class Csuka:
    def __init__(self):
        super().__init__()
        self.meret:int = 42
        self.femstoplis:bool = True
        self.marka:str = "Nike"
        self.szin:str = "Fekete"

    def __str__(self) -> str:
        return "meret: {a}, fémstoplis-e? {b}, márka: {c}, szín: {d}".format(a=self.meret, b=self.femstoplis, c=self.marka, d=self.szin)

encsukam = Csuka()
encsukam.meret = 44
encsukam.femstoplis = False
encsukam.marka = "Adidas"
encsukam.szin = "Fehér"
valakicsukaja = Csuka()
valakicsukaja.meret = 39
valakicsukaja.femstoplis = True
valakicsukaja.marka = "Puma"
valakicsukaja.szin = "Kék"
print(encsukam)
print(valakicsukaja)
valakicsukaja2 = Csuka()
valakicsukaja2.meret = input("Méret:")
femstoplis = input("Fémstoplis-e?(I/N)")
if femstoplis == "I":
    valakicsukaja2.femstoplis = True
if femstoplis == "N":
    valakicsukaja2.femstoplis = False
valakicsukaja2.marka = input("Márka:")
valakicsukaja2.szin = input("Szín:")
print(valakicsukaja2)

class kutya:
    def __init__(self):
        super().__init__()
        self.eletkor:int = 2
        self.ivartalanitott:bool = True
        self.fajta:str = "Pitbull"
        self.nem:str = "Szuka"

    def __str__(self) -> str:
        return "{a} éves, ivartalanított? {b}, fajta: {c}, neme: {d}".format(a=self.eletkor, b=self.ivartalanitott, c=self.fajta, d=self.nem)


gugya = kutya()
gugya.eletkor = 2
gugya.ivartalanitott = True
gugya.fajta = "Rotweiler"
gugya.nem = "Hím"
print(gugya)


class ruha:
    def __init__(self):
        super().__init__()
        self.arforintban:int = 6000
        self.vaneraktaron:bool = True
        self.marka:str = "Nike"
        self.ruhadarab:str = "pullover"

    def __str__(self) -> str:
        return "Ára: {a} Ft, Van raktáron? {b}, márka: {c}, ruhadarab: {d}".format(a=self.arforintban, b=self.vaneraktaron, c=self.marka, d=self.ruhadarab)

egyikruha = ruha()
egyikruha.arforintban = 10000
egyikruha.vaneraktaron = True
egyikruha.marka = "Zara"
egyikruha.ruhadarab = "Póló"
print(egyikruha)

