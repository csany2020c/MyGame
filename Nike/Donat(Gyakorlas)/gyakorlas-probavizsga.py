from typing import List
import random

print("1.feladat")

lista : List['int'] = list()
a: int = int(input())
b: int = int(input())
c: int = int(input())
lista.append(a)
lista.append(b)
lista.append(c)

print(max(lista))




print("2.feladat")

def atlag(elemek: list) -> int:
    osszeg = 0
    elemszama = 0
    for i in elemek:
        osszeg += i
        elemszama += 1
    return osszeg / elemszama

lista1: List['int'] = [1,35,78,4,2,8,2,72]
lista2: List['int'] = list()
for i in lista1:
    if atlag(lista1) >i:
        lista2.append(i)
    else:
        pass
print(lista2)

print("3.feladat")

lista3: List['int'] = list()
lista4: List['int'] = list()

for i in range(1,91):
    lista3.append(i)

#print(lista3)

for i in range(200):
    szam1: int = random.randint(0, len(lista3) - 1)
    szam2: int = random.randint(0, len(lista3) - 1)
    lista3[szam1] = int(lista3[szam2])
    lista3[szam2] = int(lista3[szam1])
for i in range(5):
    lista4.append(lista3[i])
print(lista4)

print("4.feladat")
while True:
    szamod: int = input("Adjon meg egy számot: ")
    if int(szamod) % 29 == 0:
        print("Helyes szám,osztahtó 29-el")
        break
    else:
        pass
        print("Helytelen szám.Nem oszható 29-el.Kérem irjon be egy újat!")


print("5.feladat")
alap : int = random.randint(0,127)
print(alap)
tipp = int(input())
while tipp != alap:
    if tipp >= alap:
        print("Nagyobra tippeltél")
        tipp = int(input())
    if tipp <= alap:
        print("Kisebbre tippeltél")
        tipp = int(input())









print("dogafeladat1")

int1: int = int(input())
int2: int = int(input())
for i in range(1, int2 + 1):
    eredmeny = int1 * i
    print(eredmeny)

print("dogafeladat2")

lista5: List['str'] = list()
while True:
    nev: str = str(input("Irjon be egy nevet:"))
    if nev == "":
        break
    else:
        lista5.append(nev)
randomnev = random.randint(0, len(lista5) - 1)
print(lista5[randomnev])

print("dogafeladat2")



class eger:
    def __init__(self) -> None:
        super().__init__()
        self.gombokszama: int = int
        self.vizszintesgorog: bool
        self.fuggolegesgorgo: bool
        self.gyartoneve: str = str

    def __str__(self):
        return "Gombokszáma: = {a};Vizszintes görgős e?: = {b};Függőleges görgös e?: = {c}; Gyártó: = {d} ".format(a=self.gombokszama, b=self.vizszintesgorgo, c=self.fuggolegesgorgo, d=self.gyartoneve)

eger1 = eger()
eger1.gombokszama = 2
eger1.vizszintesgorgo = False
eger1.fuggolegesgorgo = True
eger1.gyartoneve = "Ratyitallér"

eger2 = eger()
eger2.gombokszama = 4
eger2.vizszintesgorgo = True
eger2.fuggolegesgorgo = False
eger2.gyartoneve = "Vizdaak"

eger3 = eger()
eger3.gombokszama = 9
eger3.vizszintesgorgo = True
eger3.fuggolegesgorgo = True
eger3.gyartoneve = "Trászt"

listaeger: List[eger] = list()

listaeger.append(eger1)
listaeger.append(eger2)
listaeger.append(eger3)

for i in listaeger:
    print(i)