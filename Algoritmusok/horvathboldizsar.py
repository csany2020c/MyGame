from builtins import list
from typing import *
from math import sqrt

# def elso():
#     szam = 1
#     for i in range(42):
#         print(szam)
#         szam = szam + 1
# def masodik():
#     while (True):
#         idk: int = int(input())
#         if idk == 0:
#             break
#
# def harmadik():
#     osszeg: int = 0
#     szam: int = 1
#     while(szam != 0):
#         szam = int(input())
#         if szam != 0:
#             osszeg += szam
#             print("Az eddigi összeg {cmi}".format(cmi= osszeg))
#     print("Az összeg {cmi}".format(cmi=osszeg))
#
#
# def negyedik():
#     lista: List['int'] = (5, 2, 3, 7, 8, 1, 5)
#     teljes = 0
#     for i in lista:
#         teljes +=i
#     print("Az összeg {asd}".format(asd=teljes))
#
# def otodik(lista: List['int'])-> int:
#     osszeg: int = int(0)
#     for x in lista:
#         osszeg += int
#     return

# def hatodik():
#     alap: int = 1
#     monki = int(input("monki adj meg egy számot: "))
#     teszt: int = 1
#     for i in range(monki):
#         teszt: int = teszt * alap
#         print("Alapja: {alap}".format(alap=str(alap)))
#         alap: int = alap + 1
#         print("Szorzat: {teszt}".format(teszt=str(teszt)))
#     print("A(z) {szam} faktoriálisa: {eredmeny}".format(szam=monki, eredmeny=str(teszt)))
#
# def hetedik():
#     inputyin = int(input("Számot pls: "))
#     teszt = 0
#     eredmeny = 0
#     print("A(z) {szam} osztói.".format(szam=inputyin))
#     for y in range(inputyin):
#         teszt = teszt + 1
#         eredmeny = inputyin % teszt
#
#         if eredmeny == 0:
#             print(teszt)
#
# def nyolcadik():
#     inputxd = int(input("Kérlek adj meg egy számot: "))
#     idk = 0
#     osztodarab = 0
#     for i in range(inputxd):
#         idk = idk + 1
#         eredmeny = inputxd % idk
#         # print(eredmeny)
#         if eredmeny == 0:
#             osztodarab = osztodarab + 1
#         if osztodarab > 2:
#             print("Ez nem prímszám")
#             break
#     if osztodarab == 2:
#         print("Prímszám")

# def binaris():
#
#     bemenet = int(input("Adj meg egy számot: "))
#     idk = 1
#     bit = 1
#     bit2 = 1
#     while bemenet > idk:
#         print(idk)
#         idk = idk * 2
#         bit += 1
#         bit2 = bit
#     if bemenet >= 3:
#         bit2 -= 1
#     print("{bit} bit".format(bit=bit2))
#     for i in range(bit):
#         if bemenet - idk >= 0:
#             print("1", end="")
#             bemenet -= idk
#             idk = idk / 2
#
#         else:
#             print("0", end="")
#             idk = idk / 2
#
# def paroslista(belista: List['int']) -> List['int']:
#
#    kilista: List['int'] = list()
#    for i in belista:
#        if i % 2 == 0:
#            kilista.append(i)
#    return kilista
asd = [1, 2, 5, 8, 9, 10, 50, 44, 60, 71]
# print(paroslista(asd))

# def nemtudom(szam: int) -> List['int']:
#     lista: List['int'] = list()
#
#
#     if szam > 0:
#         for i in range(0, szam + 1):
#             lista.append(i)
#     else:
#         szam = -szam
#         for i in range(0, szam + 1):
#             lista.append(-i)
#
#     print(lista)
#     return lista

# def nulla(szam: int, bemenetl: List['int']) -> List['int']:
#     kimenetl: List['int'] = list()
#
#     for i in bemenetl:
#         if i % szam == 0:
#             kimenetl.append(i)
#
#     print(kimenetl)
#
#     return kimenetl
#
# szam = 5
# bemenetl = [1, 2, 5, 8, 9, 10, 50, 44, 60, 71]
#
# def nullaegy(beml: List['list']) -> bool:
#     Logic = False
#
#     for i in beml:
#         if i == 0:
#             Logic = True
#
#     print(Logic)
#     return Logic
#
#
#
# beml = [1, 2, 5, 8, 0, 9, 10, 50, 44, 60, 71]
#
# def egy(szam1: int, szam2: int) -> int:
#     if szam1 > szam2:
#         print(szam2)
#         return szam2
#     else:
#         print(szam1)
#         return szam1
#
# def minlist(bemenetlista: List['int']) -> int:
#     legkisebb = bemenetlista[1]
#     for i in bemenetlista:
#         print(i)
#         if legkisebb > i:
#             legkisebb = i
#     print(legkisebb)
#     return legkisebb
# bemenetlista = [32,5, 2, 5, 8, 6, 9, 10, 50, 44, 60, 71]
#
# def harom(a1: int, q: int, n: int) -> List['int']:
#     fuggvenylist: List['int'] = list()
#     for i in range(n):
#         fuggvenylist.append(a1)
#         a1 = a1 * q
#     return fuggvenylist
#
# print(harom(7, 10, 100))
#
# def negy(belist: List['int']) -> int:
#     osszeg = belist[1]
#     for i in belist:
#         osszeg += i
#     return osszeg
# belist = [32,5, 2, 5, 8, 6, 9, 10, 50, 44, 60, 71]
# print(negy(belist))
#
# def ot()
#
# def hat(a: float, b: float, c: float) -> List['float']:
#     megoldas: List['float'] = list()
#
#     d: float = pow(b, 2) - (4 * a * c)
#
#     if d < 0:
#         print("Hiba! A diszkrimináns kisebb mint 0.")
#     else:
#         x1: float = (-b + sqrt(d)) / 2 * a
#         x2: float = (-b - sqrt(d)) / 2 * a
#         megoldas.append(x1)
#         megoldas.append(x2)
#
#     return megoldas
# print(hat(8, -25, 3))
#
def relativpar(szam1: int, szam2: int) -> bool:
    osztok1: List['int'] = list()
    osztok2: List['int'] = list()
    kozososztok: List['int'] = list()

    if szam1 > szam2:
        hossz = szam1
    else:
        hossz = szam2

    for i in range(hossz):
        a = i + 1
        if szam1 % int(a) == 0:
            osztok1.append(a)
        if szam2 % int(a) == 0:
            osztok2.append(a)

    for x in range(len(osztok1)):
        for y in range(len(osztok2)):
            if osztok1[x] == osztok2[y]:
                kozososztok.append(osztok1[x])

    print(osztok1)
    print(osztok2)
    print(kozososztok)

    if len(kozososztok) == 1:
        return True
    else:
        return False

print(relativpar(130, 991))