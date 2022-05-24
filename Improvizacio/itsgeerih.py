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

    def __str__(self) -> str:
        return "Márka = {a}; Szín = {b}; Nagysága = {c}; Darabszám = {d}; Replika = {e}".format(a=self.marka, b=self.szin, c=self.nagysaga, d=self.darabszam, e=self.replika)

ruha = Ruhaa()
ruha.marka = "adidas"
ruha.szin = "fekete"
ruha.nagysaga = 3
ruha.darabszam = 34
ruha.replika = True

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
ruha4.replika = False

ruha.marka = input("Adja meg a ruha márkáját: ")
ruha.szin = input("Adja meg a ruha színét: ")
ruha.nagysaga = input("Adja meg a ruha nagyságát [1: S; 2: M; 3: L]: ")
ruha.darabszam = input("Adja meg a ruha darabszámát: ")
ruha.replika = input("Adja meg, hogy a ruha replika vagy sem (Igen/Nem): ")

if ruha.replika == "Igen":
    ruha.replika = True
if ruha.replika == "Nem":
    ruha.replika = False

print(ruha)
print(ruha2)
print(ruha3)
print(ruha4)

Ruhaa()