from typing import List
import os


class laptop:
    def __init__(self) -> None:
        self.ar: int = 0
        self.szallitasikoltseg: int = 0
        self.szallitasiido: int = 0
        self.szin: str = str()
        self.ram: int = 0
        self.rom: int = 0
        self.vankamera: bool

    def __str__(self) -> str:
        return "Ár = {a}; Szálltási költség = {s}; Szálltási idő = {d}; Szín = {f}; RAM = {g}; ROM = {h}; Van kamera = {j}".format(a=self.ar, s=self.szallitasikoltseg, d=self.szallitasiido, f=self.szin, g=self.ram, h=self.rom, j=self.vankamera)

    def teljesar(self) -> int:
        return self.ar + self.szallitasikoltseg


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


def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
            else:
                print("Hibás érték! Nem az intervallumba tartozó szám!")
        except:
            print("Hibás érték! Számot kérek!")


A: laptop = laptop()

A.ar = 110126
A.szallitasikoltseg = 5722
A.szallitasiido = 7
A.szin = "ezüst"
A.ram = 16
A.rom = 1024
A.vankamera = True


B: laptop = laptop()

B.ar = 73077
B.szallitasikoltseg = 5954
B.szallitasiido = 15
B.szin = "fekete"
B.ram = 4
B.rom = 128
B.vankamera = False


C: laptop = laptop()

C.ar = 76943
C.szallitasikoltseg = 5954
C.szallitasiido = 15
C.szin = "fekete"
C.ram = 4
C.rom = 640
C.vankamera = False


D: laptop = laptop()

D.ar = 163204
D.szallitasikoltseg = 0
D.szallitasiido = 7
D.szin = "fekete"
D.ram = 16
D.rom = 512
D.vankamera = False


E: laptop = laptop()

E.ar = 177014
E.szallitasikoltseg = 505
E.szallitasiido = 30
E.szin = "ezüst"
E.ram = 4
E.rom = 128
E.vankamera = True


#print(A)
#print(B)
#print(C)
#print(D)
#print(E)

laptoplista = laptop

lista: List['laptoplista'] = list()

lista.append(A)
lista.append(B)
lista.append(C)
lista.append(D)
lista.append(E)


for i in lista:
    print(i)
    print("Teljes ár:", i.teljesar(), "Forint")

while boolbeolvas("Akar felvinni adatot?"):
    F = laptop()
    F.ar = intbeolvas("Kérem a laptop árát: ", 73077, 177014)
    F.szallitasikoltseg = intbeolvas("Kérem a szállítási költséget: ", 0, 5954)
    F.szallitasiido = intbeolvas("Kérem a szállítási időt: ", 7, 30)
    F.ram = intbeolvas("RAM: ", 4, 16)
    F.rom = intbeolvas("ROM: ", 128, 1024)
    F.szin = input("Kérem a laptop színét: ")
    F.vankamera = boolbeolvas("Van kamera a laptopon?")
    lista.append(F)

for i in lista:
    print(i)

exit()


fn = ".......txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    F = laptop()
    F.ar = int(sorok[i])
    i += 1
    F.szallitasikoltseg = int(sorok[i])
    i += 1
    F.szallitasiido = int(sorok[i])
    i += 1
    F.ram = int(sorok[i])
    i += 1
    F.rom = int(sorok[i])
    i += 1
    F.szin = sorok[i]
    i += 1
    F.vankamera = strtobool(sorok[i])
    i += 1
    lista.append(F)

fr.close()


print("-------")
for i in lista:
    print(i)


os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in lista:
    f.write(i.__str__() + ";")
f.close()
