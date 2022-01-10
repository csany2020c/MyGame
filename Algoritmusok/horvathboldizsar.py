# from typing import *

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
def nyolcadik():
    inputxd = int(input("Kérlek adj meg egy számot: "))
    idk = 0
    osztodarab = 0
    for i in range(inputxd):
        idk = idk + 1
        eredmeny = inputxd % idk
        print(eredmeny)
        if eredmeny == 0:
            osztodarab = osztodarab + 1
    if osztodarab == 2:
        print("Prímszám!")
    else:
        print("Ez nem prímszám")


nyolcadik()