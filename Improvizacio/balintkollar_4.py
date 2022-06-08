from random import randint
from typing import List
def feladat1():
    print("1.Feladat")
    print("Vigyen be 2db számot: ")
    szam1 = int(input())
    szam2 = int(input())

    lista = list()
    lista2 = list()

    for i in range(1, szam2 + 1):
        lista.append(i)

    for i in lista:
        lista2.append(szam1 * i)

    print(lista2)

feladat1()

def feladat2():
    print("--------")
    print("2.Feladat")
    lista = list()

    while True:
        nevek = str(input("Adjon meg egy nevet: "))
        try:
            if nevek != "":
                lista.append(nevek)
            if nevek == "":
                break
        except:
            pass
    if len(lista) != 0:
        print(lista[randint(0, len(lista))])

feladat2()
