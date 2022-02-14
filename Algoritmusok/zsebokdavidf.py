import math
from typing import List

"""valtozo = int(input())
eredmeny = 1
szorzas = 1
for i in range(valtozo):
    eredmeny = eredmeny * szorzas
    szorzas = szorzas + 1
print(eredmeny)"""

"""szam = int(input())
oszto = 1
while(oszto <= szam):
    if szam % oszto == 0:
        print(oszto)
    oszto = oszto + 1"""


def prime(input):
    osztas = 1
    osztva = 0
    while osztas <= input:
        if input % osztas == 0:
            osztva = osztva + 1
        osztas = osztas + 1
    if osztva == 2:
        print("A(z) " + str(input) + " egy prímszám")
    else:
        print("A(z) " + str(input) + " nem prímszám")


def parose(intup: List) -> List:
    szamoklist: List = list()
    for i in range(len(intup)):
        if i % 2 == 0:
            szamoklist.append(intup[i])
    return szamoklist


valtozo = 500
inputszamok: List = list()
for i in range(1000):
    inputszamok.append(valtozo)
    valtozo += 1


def szaminputig(intup: int) -> List['int']:
    output: List = list()
    for i in range(abs(intup) + 1):
        if intup < 0:
            output.append(-i)
        else:
            output.append(i)
    return output


def vegyes(intup: int) -> List['int']:
    return parose(szaminputig(intup))


def oszthatoe(lista: List['int'], oszto: int) -> List['int']:
    output: List['int'] = list()
    for i in range(len(lista)):
        if lista[i] % oszto == 0:
            output.append(lista[i])
    return output


def vanenulla(lista: List['int']) -> bool:
    for i in range(len(lista)):
        if lista[i] == 0:
            return True
    return False


def min(szam1: int, szam2: int) -> int:
    if szam1 < szam2:
        return szam1
    else:
        return szam2


def minlist(lista: List['int']) -> int:
    smallest: int = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < smallest:
            smallest = lista[i]
    return smallest


def mertan(firstnumber: int, kvociens: int, length: int) -> List['int']:
    output: List['int'] = list()
    output.append(firstnumber)
    for i in range(length - 1):
        output.append(firstnumber * kvociens)
        firstnumber *= kvociens
    return output


def osszeadas(lista: List['int']) -> int:
    output = lista[0]
    for i in range(1, len(lista)):
        output += lista[i]
    return output


def mertaniosszege(firstnumber: int, kvociens: int, length: int) -> int:
    return osszeadas(mertan(firstnumber=firstnumber, kvociens=kvociens, length=length))


def masodfoku(a: float, b: float, c: float) -> List['float']:
    output: List['float'] = list()
    if b*b - 4*a*c < 0:
        return output
    felsoresz = math.sqrt(b*b - 4*a*c)
    eredmeny1 = (-b + felsoresz) / 2 * a
    eredmeny2 = (-b - felsoresz) / 2 * a
    output.append(eredmeny1)
    if eredmeny1 != eredmeny2:
        output.append(eredmeny2)
    return output




print(masodfoku(9, 3, -7))
print(masodfoku(9, 6, 1))
print(masodfoku(9, 6, 2))







