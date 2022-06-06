from typing import List
from random import randint

def elsofeladat() -> int:
    elso: int = int(input("írjon be egy számot: "))
    masodik: int = int(input("írjon be egy számot: "))
    harmadik: int = int(input("írjon be egy számot: "))
    a = elso
    for i in range(2):
        if a < masodik:
            a = masodik
        if a < harmadik:
            a = harmadik
    print(a)

elsofeladat()

def masodikfeladat() -> int:
    lista = [5, 7, 5, 4, 15, 5, 20, 45]
    a: int = 0
    for i in lista:
        a += i
    a = a / 8
    for i in lista:
        if a > i:
            print(i)

masodikfeladat()


def harmadikfeladat() -> int:
    lista: List['int'] = list()
    for i in range(1, 91):
        lista.append(i)
    # print(lista)

    for i in range(200):
        csere = randint(0, 9)
        csere2 = randint(0, 9)
        if csere == csere2:
            csere2 = randint(0, 9)
        elso = lista[csere]
        masodik = lista[csere2]
        lista[csere] = masodik
        lista[csere2] = elso
    for i in range(0, 4):
        print(lista[i])

harmadikfeladat()

def negyedik():
    while True:
        a: int = int(input("Írjon be egy számot: "))
        if a % 21 == 0:
            return False
        else:
            pass

negyedik()

def szamkitalalos() -> int:
    a = randint(0, 127)
    # print(a)
    while True:
        bejovo: int = int(input("Írjon be egy számot: "))
        if bejovo == a:
            return False
        if bejovo > a:
            print("Kisebb számot írjon be!")
        if bejovo < a:
            print("Nagyobb számot írjon be!")

szamkitalalos()
