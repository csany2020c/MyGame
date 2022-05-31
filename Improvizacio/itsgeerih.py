from typing import List
import os

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

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def intbeolvas(prompt: str, min: int = 1, max: int = 3) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

ruhalista: List['Ruhaa'] = list()

fn = "itsgeerih.txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    ruha = Ruhaa()
    ruha.marka = sorok[i]
    i += 1
    ruha.szin = sorok[i]
    i += 1
    ruha.nagysaga = int(sorok[i])
    i += 1
    ruha.darabszam = int(sorok[i])
    i += 1
    ruha.replika = strtobool(sorok[i])
    i += 1
    ruhalista.append(ruha)
fr.close()

while boolbeolvas("Szeretne autót felvinni a billentyűzetről?"):
    ruha = Ruhaa()
    ruha.marka = str(input("Adja meg a ruha márkáját: "))
    ruha.szin = str(input("Adja meg a ruha színét: "))
    ruha.nagysaga = intbeolvas("Adja meg a ruha nagyságát [1: S; 2: M; 3: L]")
    ruha.darabszam = intbeolvas("Adja meg a ruha mennyiségét")
    ruha.replika = boolbeolvas("Adja meg, hogy a ruha replika vagy sem")
    ruhalista.append(ruha)

print("-------")
for i in ruhalista:
    print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in ruhalista:
    f.write(i.__str__() + "\n")
f.close()

# ruha2 = Ruhaa()
# ruha2.marka = "nike"
# ruha2.szin = "feher"
# ruha2.nagysaga = 1
# ruha2.darabszam = 48
# ruha2.replika = False
#
# ruha3 = Ruhaa()
#
# ruha3.marka = "offwhite"
# ruha3.szin = "feketefeher"
# ruha3.nagysaga = 2
# ruha3.darabszam = 15
# ruha3.replika = False
#
# ruha4 = Ruhaa()
# ruha4.marka = "kancsalstaff"
# ruha4.szin = "rozsaszin"
# ruha4.nagysaga = 2
# ruha4.darabszam = 15
# ruha4.replika = True
#
# ruha5 = Ruhaa()
# ruha5.marka = "adidas"
# ruha5.szin = "fekete"
# ruha5.nagysaga = 3
# ruha5.darabszam = 34
# ruha5.replika = True
#
# ruhalista.append(ruha)
# ruhalista.append(ruha2)
# ruhalista.append(ruha3)
# ruhalista.append(ruha4)
# ruhalista.append(ruha5)
#
# for i in range(len(ruhalista)):
#     print(ruhalista[i])
#
#
# Ruhaa()

# class telefon:
#
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.telomarka: str = str(input("Írja be a telefon márkáját: "))
#         self.teloszin: str = str(input("Írja be a telefon színét: "))
#         self.telotarhely: int = int(input("Írja be a telefon tárhely mennyiségét: "))
#         self.telominoseg: str = str(input("Használt telefont szeretne? "))
#         self.all = f"{self.telomarka, self.teloszin, self.telotarhely, self.telominoseg}"
#         self.mentes: str = str("Szeretné elmenteni az adatokat? (Igen/Nem) ")
#         if self.mentes == "Igen":
#             lista.append(self.all)
#             print(lista)
#         if self.mentes == "Nem":
#             print("Az adatok nem kerültek elmentésre!")
#         self.ujra: str = str(input("Szeretne még egy adatok bekérni? (Igen/Nem) "))
#         if self.ujra == "Igen":
#             telefon()
#         if self.ujra == "Nem":
#             self.elment
#             print("Nem.")
#
#     def elment(self):
#         with open('telefonsave.txt', 'w') as file:
#             file.write(str(lista))
#
# lista: List['telefon'] = list()
#
# telefon()