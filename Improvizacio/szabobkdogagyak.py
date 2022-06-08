from typing import *
from random import randint

#print("Feladat1: ")
#print('\n')

#szam1 : int = int(input("A szorzó: "))
#szam2 : int = int(input("Hányas számig szeretné? "))

#lista = list()
#lista = []

#for i in range(szam2):
#    x = szam1 * (i + 1)
#    lista.append(x)

#print(lista)


print("Feladat2: ")
print('\n')

nevlist = list()


while True:
    nev: str = str(input("Kérek egy nevet: "))
    try:
        if nev != "" or nev != " ":
            nevlist.append(nev)

        if nev == "" or nev == " ":
            break

    except:
        pass

print(nevlist.index(randint(1, len(nevlist))))



