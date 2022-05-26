# 2het-2honap
# ar szallitasikoltseg ido termek neve egykettulajdonsag
from typing import List


class laptop:
    def __init__(self) -> None:
        self.ar: int = 0
        self.szallitasikoltseg: int = 0
        self.szallitasiido: int = 0
        self.szin: str = str()
        self.ram: int = 0
        self.rom: int = 0

    def __str__(self) -> str:
        return "Ár = {a}; Szálltási költség = {s}; Szálltási idő = {d}; Szín = {f}; RAM = {g}; ROM = {h}".format(a=self.ar, s=self.szallitasikoltseg, d=self.szallitasiido, f=self.szin, g=self.ram, h=self.rom)


A = laptop()

A.ar = 110126
A.szallitasikoltseg = 5722
A.szallitasiido = 7
A.szin = "ezüst"
A.ram = 16
A.rom = 1024


B = laptop()

B.ar = 73077
B.szallitasikoltseg = 5954
B.szallitasiido = 15
B.szin = "fekete"
B.ram = 4
B.rom = 128


C = laptop()

C.ar = 76943
C.szallitasikoltseg = 5954
C.szallitasiido = 15
C.szin = "fekete"
C.ram = 4
C.rom = 640


D = laptop()

D.ar = 163204
D.szallitasikoltseg = 0
D.szallitasiido = 7
D.szin = "fekete"
D.ram = 16
D.rom = 512


E = laptop()

E.ar = 177014
E.szallitasikoltseg = 505
E.szallitasiido = 30
E.szin = "ezüst"
E.ram = 4
E.rom = 128

print(A)
print(B)
print(C)
print(D)
print(E)

laptoplista = laptop

lista: List['laptoplista'] = list()

lista.append(A)
lista.append(B)
lista.append(C)
lista.append(D)
lista.append(E)

for i in range(len(lista)):
    print(lista[i])

laptoplista()
