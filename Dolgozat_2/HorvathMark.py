from typing import List

print("Feladat1:")
lista: List['int'] = list()
szam1:int = int(input("Első szám: "))
szam2:int = int(input("Második szám: "))
a: int = 0
if szam1 > szam2:
    if szam2 < 0:
        for i in range(-szam2 + 1):
            lista.append(a)
            a -= 1
    if szam2 >= 0:
        for i in range(szam2 + 1):
            lista.append(a)
            a += 1

if szam1 < szam2:
    if szam1 < 0:
        for i in range(-szam1 + 1):
            lista.append(a)
            a -= 1
    if szam1 >= 0:
        for i in range(szam1 + 1):
            lista.append(a)
            a += 1

if szam1 == szam2:
    if szam1 < 0:
        for i in range(-szam1 + 1):
            lista.append(a)
            a -= 1
    if szam1 >= 0:
        for i in range(szam1 + 1):
            lista.append(a)
            a += 1
print(lista)

print("Feladat2:")
lista2: List['int'] = list()
szam3: int = 0
b: int = 0
while szam3 >= 0:
    szam3 = int(input("Kérek egy számot: "))
    lista2.append(szam3)

for i in lista2:
    b += 1
else:
    print("{e}; {f}".format(e = lista2[0], f = lista2[b - 2]))


print("Feladat3: ")
class bevasarlas():
    def __init__(self) -> None:
        super().__init__()
        self.Név: str = "asd"
        self.Ár: int = 0
        self.Tömeg: int = 0

    def __str__(self) -> str:
        return "{a}; {b} Ft; {c} kg".format(a = self.Név, b = self.Ár, c = self.Tömeg)


lista3: List['int'] = list()
összeg: int = 0

tej = bevasarlas()
tej.Név = "Tej"
tej.Ár = 200
tej.Tömeg = 1
print(tej)

eper = bevasarlas()
eper.Név = "Eper"
eper.Ár = 500
eper.Tömeg = 3
print(eper)

kenyér = bevasarlas()
kenyér.Név = "Kenyér"
kenyér.Ár = 300
kenyér.Tömeg = 2
print(kenyér)

lista3.append(tej)
lista3.append(eper)
lista3.append(kenyér)

for i in lista3:
    összeg += i.Ár
print("Az összeg: ",összeg, "Ft")

#5-ös