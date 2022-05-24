from typing import List
from typing import TextIO

# ruha, milyen marka, mekkora a ruha (S/M/L/XL), hany darab van a raktaron belole, stb
# 4-5 szempont

class Ruhaa:
    def __init__(self):
        super().__init__()

        self.marka: str = ""
        self.szin: str = ""
        self.nagysaga: int = 1
        self.darabszam: int = 1
        self.replika: bool

    List
    def __str__(self) -> str:
        return "Márka = {a}; Szín = {b}; Nagysága = {c}; Darabszám = {d}; Replika = {e}".format(a=self.marka, b=self.szin, c=self.nagysaga, d=self.darabszam, e=self.replika)

ruhalista: List['str'] = list()

ruha = Ruhaa()
ruha.marka = str(input("Adja meg a ruha márkáját: "))
ruha.szin = str(input("Adja meg a ruha színét: "))
ruha.nagysaga = int(input("Adja meg a ruha nagyságát [1: S; 2: M; 3: L]: "))
ruha.darabszam = int(input("Adja meg a ruha mennyiségét: "))
ruha.replika = str(input("Adja meg, hogy a ruha replika vagy sem (Igen/Nem): "))

while(ruha.nagysaga > 3):
    if ruha.nagysaga > 3:
        print("Túl nagy számot adtál meg! Elérhető választások: [1 / 2 / 3]")
        exit()

if ruha.replika == "Igen":
    ruha.replika = True

if ruha.replika == "Nem":
    ruha.replika = False

ruhalista.append(ruha.marka)
ruhalista.append(ruha.szin)
ruhalista.append(ruha.nagysaga)
ruhalista.append(ruha.darabszam)
ruhalista.append(ruha.replika)

ruha2 = Ruhaa()
ruha2.marka = "nike"
ruha2.szin = "feher"
ruha2.nagysaga = 1
ruha2.darabszam = 48
ruha2.replika = False
ruhalista.append(ruha2.marka)
ruhalista.append(ruha2.szin)
ruhalista.append(ruha2.nagysaga)
ruhalista.append(ruha2.darabszam)
ruhalista.append(ruha2.replika)

ruha3 = Ruhaa()
ruha3.marka = "offwhite"
ruha3.szin = "feketefeher"
ruha3.nagysaga = 2
ruha3.darabszam = 15
ruha3.replika = False
ruhalista.append(ruha3.marka)
ruhalista.append(ruha3.szin)
ruhalista.append(ruha3.nagysaga)
ruhalista.append(ruha3.darabszam)
ruhalista.append(ruha3.replika)

ruha4 = Ruhaa()
ruha4.marka = "kancsalstaff"
ruha4.szin = "rozsaszin"
ruha4.nagysaga = 2
ruha4.darabszam = 15
ruha4.replika = True
ruhalista.append(ruha4.marka)
ruhalista.append(ruha4.szin)
ruhalista.append(ruha4.nagysaga)
ruhalista.append(ruha4.darabszam)
ruhalista.append(ruha4.replika)

ruha5 = Ruhaa()
ruha5.marka = "adidas"
ruha5.szin = "fekete"
ruha5.nagysaga = 3
ruha5.darabszam = 34
ruha5.replika = True
ruhalista.append(ruha5.marka)
ruhalista.append(ruha5.szin)
ruhalista.append(ruha5.nagysaga)
ruhalista.append(ruha5.darabszam)
ruhalista.append(ruha5.replika)

# print(ruha)
# print(ruha2)
# print(ruha3)
# print(ruha4)
# print(ruha5)
print(ruhalista)

Ruhaa()