#ar, szallitasi koltseg, szallitasi ido, tulajdonsag, termek neve
from typing import List

class Hangszoro:
    def __init__(self):
        self.ar: int = 5000
        self.szallitasikoltseg:int
        self.szallitasiido:str
        self.tudnivalok:str
        self.termeknev:str

    def __str__(self) -> str:
        return "Termék neve: {x}, Ára: {a}, Szállításiköltség: {b}, Szállításiidő: {c}, Tudnivalók: {d}".format(x=self.termeknev,a=self.ar, b=self.szallitasiido, c=self.szallitasikoltseg, d=self.tudnivalok)

JBL = Hangszoro()
JBL.ar = 30000
JBL.szallitasikoltseg = 1500
JBL.szallitasiido = "15 munkanap"
JBL.tudnivalok = "a termék kék színű 5000 mA akkumlátorral"
JBL.termeknev = "JBL XTREME"
print(JBL)