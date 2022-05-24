from typing import TextIO, List

class cipo:
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = " "
        self.meret: int = 0
        self.szin: str = " "
        self.stopli: bool = False
        self.anyag: str = " "

    def __str__(self) -> str:
        return "Gyártó: {a}, Méret: {b}, Szín: {c}, FG stoplis?: {d}, Anyaga: {e}".format(a=self.gyarto, b=self.meret, c=self.szin, d=self.stopli, e=self.anyag)

l: List['cipo'] = list()

csuka = cipo()
csuka.gyarto = "Nike"
csuka.meret = 41
csuka.szin = "Fekete"
csuka.stopli = False
csuka.anyag = "Bőr"
print(csuka)

csuka2 = cipo()
csuka2.gyarto = "Adidas"
csuka2.meret = 40
csuka2.szin = "Fehér"
csuka2.stopli = True
csuka2.anyag = "Műanyag"
print(csuka2)

csuka3 = cipo()
csuka3.gyarto = "Puma"
csuka3.meret = 42
csuka3.szin = "Neonzöld, Neonsárga"
csuka3.stopli = False
csuka3.anyag = "Műbőr"
print(csuka3)

cipok = cipo()
cipok.gyarto = str(input("gyarto:"))
cipok.meret = int(input("meret:"))
cipok.szin = str(input("szin:"))
cipok.stopli = str(input("stopli:(igen/nem):"))
if cipok.stopli == "Igen":
    cipok.stopli = True
else:
    cipok.stopli = False
cipok.anyag = str(input("anyag:"))
print(cipok)

l.append(csuka)
l.append(csuka2)
l.append(csuka3)
l.append(cipok)
for i in l:
    print(i)

cipo()