from typing import List
from time import time
import math


#1. feladat 42-ig szamok egyesevel kiiaratasa
# a: int = 0
# for c in range(42):
#     a = a + 1
#     print(a)

#2. feladat szamok beolvasasa ameddig a bemenet nem lesz 0
#3. feladat a 2. feladat alapján szamolja ossze a bemeneteket, ameddig nem 0 a bement
# asd = 0
# while(True):
#     a: int = int(input())
#     asd = asd + a
#     if a == 0:
#         # print(asd)
#         print("A beirt szamok osszege:" + " " + str(asd))
#         break

#4. feladat
# def osszeglistaban():
#     lista: List['int'] = (6, 1, 1, 1, 1, 1, 1)
#     ad: int = 0
#     for i in range(0, len(lista)):
#         ad += lista[i]
#     print("Az összeg: {sum}".format(sum=ad))
#
# osszeglistaban()
# lista: List['int'] = (6, 1, 1, 1, 1, 1, 1)
# def osszegzes(lista: List['int']) -> int:
#     szam: int = 0
#     for i in range(0, len(lista)):
#         szam += lista[i]
#     return szam
#
#
# print(osszegzes(lista))

#5. feladat: faktorialis szamolas
# def faktoralis(asd: int) -> int:
#     szorzat = 1
#     for i in range(2, asd + 1):
#         szorzat *= i
#     return szorzat


# print(faktoralis(6))

# 2. feladat
# print(8 % 3)

#6. feladat: primszam fuggveny, break
def osztok(n: int) -> list[int]:
    lista: List['int'] = list()
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista

# for i in osztok(26):
#     print(i)
#
# print(osztok(26))

#7.feladat: primszam eldonto fuggveny, bemenet egy szam- kimenet igaz vagy hamis
# def primszam(a: int) -> bool:
#     if len(osztok(a)) == 2:
#         return True
#     else:
#         return False
#
# print(primszam(16))

#8. feladat: gyakorlas primszam fuggveny(lassu a szamolas 100000 felett)
# def primszam_sajat(a: int) -> bool:
#     erkezo = a
#     random = 0
#     onmaga = 1
#     if erkezo > 250:
#         return "Keress kisebb szamot!"
#     if erkezo > 0:
#         for i in range(erkezo):
#             if erkezo % onmaga == 0:
#                 random = random + 1
#             onmaga = onmaga + 1
#     else:
#         return "Nem lehet ilyet :)"
#
#     if random == 2:
#         return True
#     else:
#         return False

#print(primszam_sajat(250))

# *.feladat, felesleges, mert mar feljebb van erre fuggveny
# def fuggveny1(n: int) -> bool:
#     return len(primszam(n)) == 2
#
# for i in range(0, 126):
#      print("{szam} {primszam}".format(szam=i, primszam=fuggveny1(i)))

#új számolás-gyakorlas
# ts1 = time()
# for i in range(100000, 1000000):
#     primszame = primszam_sajat(i)  # Prímszám eldöntő függvény helye
#     if primszame:
#         print(i)
# ts2 = time()
# print("Az algoritmus {mp} másodpercig futott.".format(mp=(ts2 - ts1)))

#9. feladat: binaris szamok
# def binaris_ketto(a: int) -> int:
#     w: str = ""
#     erkezo = a
#     while erkezo > 0:
#         if erkezo % 2 == 0:
#             w = w + "0"
#         else:
#             w = w + "1"
#         erkezo = erkezo // 2
#     return w
#
# bejovo: int = int(input("Írj be egy számot: "))
# print("Az eredmény:" + " " + binaris_ketto(bejovo))

#erdekesseg
# print(6 / 2)
# print(6 // 2)

#10.feladat: parosszamok, bemenet lista, kimenete lista a paros szamokkal
def parosfuggveny(a: List['int']) -> List['int']:
    lista: List['int'] = list()
    for i in a:
        if i % 2 == 0:
            lista.append(i)
    return lista

# bemenetelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -2, -3, -11]
# print(parosfuggveny(bemenetelist))

#11.feladat:szamolas 6-ig
def szamolas(a: int) -> List['int']:
    lista: List['int'] = list()
    # if a < 0:
    #     return "Sajnos ilyen számot jelenleg nem lehet számolni!"
    if a < 0:
        for i in range(0, a - 1, -1):
            lista.append(i)
    else:
        for i in range(0, a + 1):
            lista.append(i)
    return lista

# print(szamolas(66))
# print(szamolas(-66))

# . feladat: az elozo fuggvenyek hasznalta
# def osszeshasznalata(a: int) -> List['int']:
#     return parosfuggveny(szamolas(a))
#
# print(osszeshasznalata(7))

#házi feladat
#0.0 feladat
def maradeknelkuliosztok(a: List['int'], b: int) -> List['int']:
    uj: List['int'] = list()
    for i in a:
        if i % b == 0:
            uj.append(i)
    return uj

listacska = [1, 5 , 8, 9 , 150, 60, 44, 3, 0, 7]
# print(maradeknelkuliosztok(listacska, 6))

#
def logikaifuggveny(a: List['int']) -> bool:
    almagyar = 0
    for i in a:
        if i == 0:
            almagyar = almagyar + 1
    if almagyar >= 1:
        return True
    else:
        return False

alma = [20, 60, 70, 5, 6, 3, 7, 32]
alma1 = [12, 0, 6, 20, 7]
# print(logikaifuggveny(alma))
# print(logikaifuggveny(alma1))

#1. feladat
def min(a: int, b: int) -> int:
    if a > b:
        return b
    elif a == b:
        return a, b
    else:
        return a

# print(min(9, 8))

#2, feladat
def minilist(a: List['int']) -> int:
    szam = 0
    for i in a:
        if szam < i:
            szam = i
        break
    for i in a:
        if szam > i:
            szam = i
    return szam

minilistam = [5, 6, 8, 88, 2, 66, 30]
# print(minilist(minilistam))

#3.feladat
def mertanisorozat(a1: float, q: float, n: float) -> List['int']:
    uj: List['float'] = [a1]
    szam: int = a1
    while n > 1:
        szam = szam * q
        n = n - 1
        uj.append(szam)
    return uj

# print(mertanisorozat(7, 10, 5))
# print(mertanisorozat(1, 1.3, 15))

#4. feladat
def osszeglista(a: List['int']) -> int:
    szam = 0
    for i in a:
        szam = szam + i
    return szam

osszeglistam = [1, 8, 16, 32, 88, 789]
# print(osszeglista(osszeglistam))

#5. feladat
def osszesegyfuggvenyben(a1: int, q: int, n: int) -> int:
    return osszeglista(mertanisorozat(a1, q, n))

# print(osszesegyfuggvenyben(5, 8, 2))

#6. feladat-nincs kész, majd egyszer...
def masodfoku(a: float, b: float, c: float) -> List['float']:
    listam: List['float'] = list()
    d = b**2 - 4*a*c
    if d < 0:
        return listam
    else:
        diszkriminansa = math.sqrt(d)
        mo1: float = -b + diszkriminansa / 2 * a
        mo2: float = -b - diszkriminansa / 2 * a
        listam.append(mo1)
        listam.append(mo2)
    return listam

# print(masodfoku(8, 20, 3))

#orai munka-jo megoldas
def relativ_primek(a: int, b: int) -> bool:
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
    # lista: List['int'] = list()
    # lista2 : List['int'] = list()
    # lista3: List['int'] = list()
    # szam = 1
    # google: 0
    # if a > b:
    #     nagyobbik = a
    # else:
    #     nagyobbik = b
    # for i in range(nagyobbik):
    #     if a % szam == 0:
    #         lista.append(i)
    #     if b % szam == 0:
    #         lista2.append(i)
    #     szam = szam + 1
    # # return lista, "a", lista2
    #
    # gyors = len(lista)
    # gyors2 = len(lista2)

# print(relativ_primek(8, 21))

#masik megoldasa
def reletivprim2(a: int, b: int) -> bool:
    lista: List['int'] = list()
    lista2 : List['int'] = list()
    lista3: List['int'] = list()
    google: 0
    for i in range(2, a + 1):
        if a % i == 0:
            lista.append(i)
    for i in range(2, b + 1):
        if b % i == 0:
            lista2.append(i)
    # return lista, "a", lista2


#hazi feladat

#1. feladat
def tokeletesszamok(a: int) -> bool:
    osszead: int = 0
    for i in range(1, a):
        if a % i == 0:
            osszead = osszead + i
            # print(i)
    if osszead == a:
        return True
    else:
        return False


# print(tokeletesszamok(27)) #false
# print(tokeletesszamok(28)) #true
# print(tokeletesszamok(6)) #true
# print(tokeletesszamok(4)) #false

#2. feladat
def tokeletesellenorzo(a: int, b: int) -> List['int']:
    lista: List['int'] = list()
    for i in range(a, b + 1):
        alma = tokeletesszamok(i)
        # print(i)
        if alma == True:
            lista.append(i)
    return lista

# print(tokeletesellenorzo(6, 496))
# print(tokeletesellenorzo(4, 88))

#3. feladat
def tizesszamrendszer(a: int) -> List['int']:
    lista: List['int'] = list()
    for i in str(a):
       lista.append(int(i))
    return lista

# print(tizesszamrendszer(230))

#4. feladat
def osszegfuggveny(a: int) -> bool:
    szam = 0
    for i in str(a):
        szam = szam + int(i)
    return szam

# print(osszegfuggveny(4))
# print(osszegfuggveny(856))


#5. feladat
def szamjegyszorzat(a: int) -> bool:
    szam = 1
    for i in str(a):
        szam = szam * int(i)
        if szam == a:
            return True
        else:
            return False

# print(szamjegyszorzat(56))
# print(szamjegyszorzat(8))
# print(szamjegyszorzat(15))

#6. feladat
def haromjegyu() -> int:
    lista: List['int'] = list()
    lista2: List['int'] = list()
    for i in range(100, 999):
        if i % 15 == 0:
            lista.append(i)
    for i in lista:
        if osszegfuggveny(i) == 15:
            lista2.append(i)
    return len(lista2)


# print(haromjegyu())

def armstongszamok() -> int:
    szam = 0
    lista: List['int'] = list()
    lista2: List['int'] = list()
    for i in range(100, 999):
        while i > 0:
            lista.append(i % 10)
            i = i // 10
            lista.reverse()
        return lista


# print(armstongszamok())

def armstrongszamok2() -> bool:
    szam = 0
    for i in range(1000, 9999):
        eredeti = i
        for o in str(i):
            szam = szam * math.pow(int(o), 3)
            if szam == eredeti:
                return False
    return True

# print(armstrongszamok2())

#hazi feladat_hf3

#1.a feladat
def mersseneprim(a: int) -> bool:
    db = 0
    szam = 1
    szamolas: float = math.pow(2, a) - 1
    while szamolas > 1:
        if szamolas % szam == 0:
            db += 1
            # print("db=" + str(db))
            if db > 3:
                break
            if szam == szamolas:
                break
        szam += 1
    return db == 2


# print(mersseneprim(3)) #true
# print(mersseneprim(4)) #false
# print(mersseneprim(5)) #true

#1.b feladat
def mersenneprimkereses(a: int) -> bool:
    szam = 1
    db = 0
    for i in range(a):
        if a % szam == 0:
            db += 1
        szam += 1
    return db == 2, mersseneprim(a)

# print(mersenneprimkereses(79))
# print(mersenneprimkereses(7))
