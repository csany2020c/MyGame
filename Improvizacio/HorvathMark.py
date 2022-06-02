from typing import List
import os

class Kerekpar():
    def __init__(self):
        super().__init__()
        self.elsovalto: int = 3
        self.hatsovalto: int = 7
        self.szin: str = "piros"
        self.szin2: str = "kék"
        self.fajta: str = "terep"
        self.kulacstarto: int = 1
        self.csengo: bool = False

    def __str__(self) -> str:
        return str(self.elsovalto) + "\n" + str(self.hatsovalto) + "\n" + self.szin + "\n" + self.szin2 + "\n" + self.fajta + "\n" + str(self.kulacstarto) + "\n" + str(self.csengo)

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

def boololvasas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + "(I/N):")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def intbeolvasas(prompt = str, min:int = 0, max:int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
        except:
            pass


enkerekpar = Kerekpar()
enkerekpar.hatsovalto = 6
enkerekpar.szin = "fekete"
enkerekpar.szin2 = "narancs"


randomkerekpar = Kerekpar()
randomkerekpar.kulacstarto = 5
randomkerekpar.hatsovalto = 8
randomkerekpar.szin = "zöld"
randomkerekpar.szin2 = "narancs"
randomkerekpar.fajta = "országúti"


#print(felhasznalokerekpar)
#print(Kerekpar())
#print(enkerekpar)
#print(randomkerekpar)
#HF még 2 osztály, példányok belőlük

feladat = "HorvathMark.txt"
feladatr = open(feladat, mode="r", encoding="utf-8")
lines = feladatr.read().strip().split("\n")
l: List['Kerekpar()'] = list()
i: int = 0
while i < len(lines):
    a = Kerekpar()
    a.elsovalto = int(lines[i])
    i += 1
    a.hatsovalto = int(lines[i])
    i += 1
    a.szin = lines[i]
    i += 1
    a.szin2 = lines[i]
    i += 1
    a.fajta = lines[i]
    i += 1
    a.kulacstarto = int(lines[i])
    i += 1
    a.csengo = strtobool(lines[i])
    i += 1
    l.append(a)
feladatr.close()

os.remove(feladat)
f = open(feladat, mode="w", encoding="utf-8")
for i in l:
    f.write(i.__str__() + "\n")
f.close()

while boololvasas("Akar felvinni adatot?"):
    felhasznalokerekpar = Kerekpar()
    felhasznalokerekpar.elsovalto = intbeolvasas("Hány fokozatú az első váltó? ", 1, 3)
    felhasznalokerekpar.hatsovalto = intbeolvasas("Hány fokozatú a hátsó váltó? ", 1, 8)
    felhasznalokerekpar.szin = input("Milyen színű?(1. szín) ")
    felhasznalokerekpar.szin2 = input("Milyen színű?(2. szín) ")
    felhasznalokerekpar.fajta = input("Milyen fajtájú a kerékpár? ")
    felhasznalokerekpar.kulacstarto = intbeolvasas("Mennyi kulacstartója van? ", 0, 5)
    felhasznalokerekpar.csengo = boololvasas("Van rajta csengő?")
    l.append(felhasznalokerekpar)

for i in l:
    print(i)

class Telefon():
    def __init__(self):
        super().__init__()
        self._5G: bool = True
        self.keret: bool = False
        self.szin: str = "fekete"
        self.ram_GB: int = 4

    def __str__(self) -> str:
        return "5G = {g}; Keret = {h}; Szín = {i}; Ram GB-ban = {j}".format(g = self._5G, h = self.keret, i = self.szin, j = self.ram_GB)


entelefon = Telefon()
entelefon.szin = "white"
entelefon.keret = True

#print(Telefon())
#print(entelefon)

class TV():
    def __init__(self):
        super().__init__()
        self.smartTV: bool = False
        self.radio: bool = True
        self.ID_channel: bool = False
        self.szin: str = "gray"

    def __str__(self) -> str:
        return "SmartTV = {k}; Radio = {l}; ID channel = {m}; Szín = {n}".format(k = self.smartTV, l = self.radio, m = self.ID_channel, n = self.szin)


enTV = TV()
enTV.smartTV = True
enTV.ID_channel = True
enTV.szin = "black"

#print(enTV)
#print(TV())

