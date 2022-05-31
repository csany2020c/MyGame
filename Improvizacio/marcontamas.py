from typing import List
import os

class versenyzo():
    def __init__(self):
        self.gyozelmek: int = 11
        self.veresegek: int = 0
        self.dontetlen: int = 0
        self.sulycsoport: str = "welterweight"
        self.cim: str = ""
        self.ko: bool

    def __str__(self) -> str:
        return  "gyozelmek = {a}; veresegek = {b}; dontetlen = {c}; sulycsoport = {d}; cim = {e}; ko = {f}".format(a = self.gyozelmek, b = self.veresegek, c = self.dontetlen, d = self.sulycsoport, e = self.cim, f = self.ko)

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

def intbeolvas(prompt: str, min: int = 0, max: int = 11) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

# khamzat = versenyzo()
# khamzat.gyozelmek = 11
# khamzat.veresegek = 0
# khamzat.dontetlen = 0
# khamzat.sulycsoport = "welterweight"
# khamzat.ko = False
#
# islam = versenyzo()
# islam.gyozelmek = 22
# islam.veresegek = 1
# islam.dontetlen = 0
# islam.sulycsoport = "lightweight"
# islam.ko = False
#
# glover = versenyzo()
# glover.gyozelmek = 33
# glover.veresegek = 7
# glover.dontetlen = 0
# glover.sulycsoport = "light heavyweight"
# glover.cim = "címvédő"
# glover.ko = False
#
# francis = versenyzo()
# francis.gyozelmek = 17
# francis.veresegek = 3
# francis.dontetlen = 0
# francis.sulycsoport = "heavyweight"
# francis.cim = "címvédő"
# francis.ko = False
#
lista:List['versenyzo'] = list()
# lista.append(islam)
# lista.append(glover)
# lista.append(francis)
# lista.append(khamzat)

fn = "igen.txt"

# fr = open(fn, mode='r', encoding='utf-8')
# sorok = fr.read().strip().split("\n")
# i: int = 0
# while i < len(sorok):
#     oliveira = versenyzo()
#     oliveira.gyozelmek = int(sorok[i])
#     i += 1
#     oliveira.veresegek = int(sorok[i])
#     i += 1
#     oliveira.dontetlen = int(sorok[i])
#     i += 1
#     oliveira.sulycsoport = int(sorok[i])
#     i += 1
#     oliveira.cim = sorok[i]
#     i += 1
#     oliveira.ko = strtobool(sorok[i])
#     i += 1
#     lista.append(oliveira)
# fr.close()

while boolbeolvas("Szeretne versenyzőt bevinni?"):
    oliveira = versenyzo()
    oliveira.gyozelmek = intbeolvas("Hány győzelme van:")
    oliveira.veresegek = intbeolvas("Hány veresége van:")
    oliveira.dontetlen = intbeolvas("Hány döntetlenje van:")
    oliveira.sulycsoport = input("Milyen súlycsoport:")
    oliveira.cim = input("Mi a címe:")
    oliveira.ko = boolbeolvas("Kapott-e ko-t?")
    lista.append(oliveira)

for i in lista:
    print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in lista:
    f.write(i.__str__() + "\n")
f.close()






