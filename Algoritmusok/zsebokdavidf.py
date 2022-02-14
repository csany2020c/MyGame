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


valtozo = -500
inputszamok: List = list()
for i in range(1000):
    inputszamok.append(valtozo)
    valtozo = valtozo + 1


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

print(vegyes(-100))
