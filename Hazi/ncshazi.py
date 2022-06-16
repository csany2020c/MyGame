import random


def szamok():
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    if a > b and a > c:
        print("1. feladat: " + str(a))
    if b > a and b > c:
        print("1. feladat: " + str(b))
    if c > a and c > b:
        print("1. feladat: " + str(c))
    if a == b == c:
        print("1. feladat: " + str(a))


# szamok()


def atlagk(lista: list[int]):
    a: int = 0
    for i in range(0, len(lista)):
        a += lista[i]
        if lista[i] < a / 8:
            print("2. feladat: " + str(lista[i]))


# atlagk([1, 3, 2, 4, 6, 5, 7, 8])


def hueg(a: int = int(input())):
    while a % 21 != 0:
        a = int(input())
    else:
        print("4. feladat: " + str(a))


# hueg()


def kitalal():
    a: int = int(input())
    b: int = random.randint(0, 127)
    if a < b:
        print("5. feladat: nagyobb")
        a = int(input())
    if a > b:
        print("5. feladat: kisebb")
        a = int(input())
    if a == b:
        print("5. feladat: A megoldás valóban a " + str(a))


# kitalal()
