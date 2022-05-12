from typing import List
import math

#HF1-----------------------------------------------------------------------------------

def maradeknelkulilista (lista1: List['int'], a: int) -> List['int']:
    lista2: list = []
    for i in lista1:
        if i % a == 0:
            lista2.append(i)
    return lista2

#print(maradeknelkulilista((4,7,6,4,67), 4))

def min(a:int ,b:int) -> int:
    if a < b:
        return a
    if a > b:
        return b

#print(min(2,5))

def minlist(lista: List['int']) -> int:
    x: int = lista[1]
    for i in lista:
        if x > i:
            x = i
    return x

#print(minlist((3522,52525,777,43,56)))

def mertaniszorzat(a1:int, q:int, n:int) -> List['int']:
    lista: List = []
    for i in range(1,n + 1):
        lista.append(a1 * q**(i-1))
    return lista

#print(mertaniszorzat(2,6,8))

def listaosszeg(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x

#print(listaosszeg((363,63725,673,63,2)))

def mertaniszorzateslistaosszeg(a1:int, q:int, n:int) -> int:
    return listaosszeg(mertaniszorzat(a1, q, n))

#print(mertaniszorzateslistaosszeg(1,56,7))

#HF2-----------------------------------------------------------------------------------------

def szamfelbont(x:int) -> List['int']:
    lista: List['int'] = []
    for i in str(x):
        lista.append(int(i))
    return lista

#print(szamfelbont(352))

def szamjegyösszeg(x:int) -> int:
    osszeg = 0
    for i in (szamfelbont(x)):
        osszeg = osszeg + i
    return osszeg

#print(szamjegyösszeg(252))

def szamjegyszorzat(x:int) -> bool:
    szorzat = 1
    for i in (szamfelbont(x)):
        szorzat *= int(i)
    if szorzat == x:
        return True
    else:
        return False

#print(szamjegyszorzat(2))

def tizenot() -> int:
    db = 0
    for i in range(100,1000):
        if i % 15 == 0 and szamjegyösszeg(i) == 15:
            db += 1
    return db

print(tizenot())


