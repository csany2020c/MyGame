from typing import TextIO, List
import os

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


def strtobool(ar: str) -> bool:
    if ar.upper() == "I" or ar.upper() == "Y" or ar.upper() == "TRUE":
        return True
    if ar.upper() == "N" or ar.upper() == "FALSE":
        return False
    return None

def boolbeolvas(prompt: str) -> bool:
    while True:
        stopli: str = input(prompt + " (I/N): ")
        if stopli.upper() == "I" or stopli.upper() == "Y":
            return True
        if stopli.upper() == "N":
            return False

def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

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

while boolbeolvas("Szeretne cipőt felvinni a billentyűzetről?"):
    cipok = cipo()
    cipok.gyarto = str(input("gyarto:"))
    cipok.meret = int(input("meret:"))
    cipok.szin = str(input("szin:"))
    cipok.stopli = boolbeolvas("fémstoplis?:")
    cipok.anyag = str(input("anyag:"))

l.append(csuka)
l.append(csuka2)
l.append(csuka3)
l.append(cipok)


fn = "zsupp.txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    c = cipo()
    c.gyarto = sorok[i]
    i += 1
    c.szin = sorok[i]
    i += 1
    c.stopli = strtobool(sorok[i])
    i += 1
    c.meret = int(sorok[i])
    i += 1
    c.anyag = sorok[i]
    i += 1
    l.append(c)
fr.close()

for i in l:
    print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in l:
    f.write(i.__str__() + "\n")
f.close()