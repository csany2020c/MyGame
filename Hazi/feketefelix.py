from typing import List
from random import randint
#1.feladat
#class szamok:
#    def __init__(self) -> None:
#       self.egy: int = input("Kérek egy számot:")
#       self.ketto: int = input("Kérek egy számot:")
#       self.harom: int = input("Kérek egy számot:")
#       self.g: int = 0
#       self.h: int = 0
#       self.atlag: int = 0
#
#
#a = szamok()
#f = a.egy
#if f < a.ketto:
#    f = a.ketto
#if f < a.harom:
#    f = a.harom
#print(f)

#2.feladat
#lista = list()
#lista = [1, 5, 6, 7, 8, 9, 10, 11]
#
#for i in lista:
#    a.g += 1
#for q in lista:
#    a.h = a.h + q
#
#a.atlag = a.h / a.g
#print(a.atlag)
#for l in range(5, 12):
#    if l < a.atlag:
#        print(l)

#3.feladat

#lista2 = list()
#lista2 = []
#
#for i in range(1, 90):
#    lista2.append(i)
#
#for i in range(200):
#    csere = randint(1, 2)
#    csere2 = randint(1, 2)
#    if csere == csere2:
#        csere2 = randint(1, 2)
#        t = lista2[csere]
#        z = lista2[csere2]
#        lista2[csere] = z
#        lista2[csere2] = t
#    for i in range(0, 5):
#        print(lista2[i])
#4.feladat
#while True:
#        asd: int = int(input("Adj meg egy számot:"))
#        if asd % 21 < 1:
#            break
#        else:
#            pass


#5.feladat
d = randint(0, 127)
while True:
    asd: int = int(input("Adj meg egy számot:"))
    if asd == d:
        break
    if asd > d:
        print("Kissebb!")
    if asd < d:
        print("Nagyobb!")
