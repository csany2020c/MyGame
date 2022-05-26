#ar, szallitasi koltseg, szallitasi ido, tulajdonsag, termek neve
from typing import List

class Hangszoro:
    def __init__(self) -> None:
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
MP3 = Hangszoro()
MP3.ar = 1300
MP3.szallitasikoltseg = 0
MP3.szallitasiido = "30 nap"
MP3.tudnivalok = "A termék világos kék, 80 mA akkumlátor, 48 órés készenléti idő"
MP3.termeknev = "USB in-line card MP3 player"
#print(MP3)
BoomBox = Hangszoro()
BoomBox.ar = 3500
BoomBox.szallitasikoltseg = 0
BoomBox.szallitasiido = "31 nap"
BoomBox.tudnivalok = "teljesitmény 60W, vízálló"
BoomBox.termeknev = "JBL Boombox Boom Box 3 2"
#print(BoomBox)
#print(JBL, MP3, BoomBox)
lista: List[Hangszoro] = list()
lista.append(JBL)
lista.append(BoomBox)
lista.append(MP3)
for i in lista:
    print(i)

print(lista)

#print(JBL)