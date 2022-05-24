from typing import List

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

    def __str__(self) -> str:
        return "Márka = {a}; Szín = {b}; Nagysága = {c}; Darabszám = {d}; Replika = {e}".format(a=self.marka, b=self.szin, c=self.nagysaga, d=self.darabszam, e=self.replika)

ruhalista: List['Ruhaa'] = list()

ruha = Ruhaa()
ruha.marka = str(input("Adja meg a ruha márkáját: "))
ruha.szin = str(input("Adja meg a ruha színét: "))
ruha.nagysaga = int(input("Adja meg a ruha nagyságát [1: S; 2: M; 3: L]: "))
while(ruha.nagysaga > 3):
    if ruha.nagysaga > 3:
        print("Túl nagy számot adtál meg! Elérhető választások: [1 / 2 / 3]")
        exit()

ruha.darabszam = int(input("Adja meg a ruha mennyiségét: "))
ruha.replika = str(input("Adja meg, hogy a ruha replika vagy sem (Igen/Nem): "))

if ruha.replika == "Igen":
    ruha.replika = True

if ruha.replika == "Nem":
    ruha.replika = False

ruha2 = Ruhaa()
ruha2.marka = "nike"
ruha2.szin = "feher"
ruha2.nagysaga = 1
ruha2.darabszam = 48
ruha2.replika = False

ruha3 = Ruhaa()
ruha3.marka = "offwhite"
ruha3.szin = "feketefeher"
ruha3.nagysaga = 2
ruha3.darabszam = 15
ruha3.replika = False

ruha4 = Ruhaa()
ruha4.marka = "kancsalstaff"
ruha4.szin = "rozsaszin"
ruha4.nagysaga = 2
ruha4.darabszam = 15
ruha4.replika = True

ruha5 = Ruhaa()
ruha5.marka = "adidas"
ruha5.szin = "fekete"
ruha5.nagysaga = 3
ruha5.darabszam = 34
ruha5.replika = True

ruhalista.append(ruha)
ruhalista.append(ruha2)
ruhalista.append(ruha3)
ruhalista.append(ruha4)
ruhalista.append(ruha5)

for i in range(len(ruhalista)):
    print(ruhalista[i])


Ruhaa()