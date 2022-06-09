from typing import List
import random

def max(asd: list) -> int:
    b: int = asd[0]
    for i in asd:
        if b < i:
            b = i
    return b

def atlag(asd: list) -> int:
    c = 0
    d = 0
    for i in asd:
        c += i
        d += 1
    return c / d

#print("Feladat 1:")
#lista: List['int'] = list()
#a: int = 0
##for i in range(3):
##    a = int(input())
##    lista.append(a)
##
##print(max(lista))
#
#print("Feladat 2:")
#lista1: List['int'] = [10,30,20,40,50,2,8,1]
#lista2: List['int'] = list()
#for i in lista1:
#    if atlag(lista1) > i:
#        lista2.append(i)
#print(lista2)
#
#print("Feladat 3:")
#lista3: List['int'] = list()
#lista4: List['int'] = list()
#for i in range(1, 91):
#    lista3.append(i)
#
#for i in range(200):
#    x: int = random.randint(0, len(lista3) - 1)
#    y: int = random.randint(0, len(lista3) - 1)
#    lista3[x] = int(lista3[y])
#    lista3[y] = int(lista3[x])
#for i in range(5):
#    lista4.append(lista3[i])
#print(lista4)
#
#print("Feladat 4:")
#e: int = 1
#while e % 21:
#    e = int(input())
#
#print("Feladat 5:")
#f:int = random.randint(0, 127)
#print(f)
#g = int(input())
#while g != f:
#    if g >= f:
#        print("Nagyobra tippeltél")
#        g = int(input())
#    if g <= f:
#        print("Kisebbre tippeltél")
#        g = int(input())

print("Dolgozat feladat 1:")
lista: List['int'] = list()
a: int = int(input("Kérek egy számot? "))
b: int = int(input("Hánnyal szorozzam? "))
for i in range(1, b + 1):
    c = a * i
    lista.append(c)
print(lista)

print("Dolgozat feladat 2:")
lista2: List['str'] = list()
d: str = "asd"
e:int = 0
while d != "":
    d = input("Kérek egy szavat:")
    lista2.append(d)
else:
    f = random.randint(0, len(lista2) - 1)
    print(lista2[f])




