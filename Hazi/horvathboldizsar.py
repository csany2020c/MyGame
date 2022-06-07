import random
from typing import *

# 1.feladat
def legnagyobb(a: int, b: int, c: int) -> int:
    return max(a, b, c)
print("1. feladat:")
print(legnagyobb(5, 15, 3))


# 2.feladat
def atlagkisebb(lista: list) -> list:
    atlagnalkisebb: List['int'] = list()
    idk = 0
    for i in range(len(lista)):
        idk += lista[i]

    atlag = idk / len(lista)
    for x in range(len(lista)):
        if lista[x] < atlag:
            atlagnalkisebb.append(lista[x])

    return atlagnalkisebb

print("2. feladat:")
print(atlagkisebb([1, 2, 5, 8, 9, 10, 50, 44, 60, 71]))


# 3.feladat
def kilencvenescucc():
    print("3. feladat:")
    egytolkilencven: List['int'] = list()
    for y in range(1, 91):
        egytolkilencven.append((y))

    for z in range(200):
        random1: int = random.randint(0, len(egytolkilencven) - 1)
        random2: int = random.randint(0, len(egytolkilencven) - 1)
        egytolkilencven[random1] = int(egytolkilencven[random2])
        egytolkilencven[random2] = int(egytolkilencven[random1])
    for q in range(5):
        print(egytolkilencven[q])

kilencvenescucc()

# 4.feladat
def huszon1():
    print("4. feladat:")
    while True:
        oszthato = int(input("Adj meg egy számot, ami osztható 21-el:  "))
        try:
            if oszthato % 21 == 0 and oszthato != 0:
                print("Osztható 21-el.")
                return True
        except:
            pass

huszon1()

# 5.feladat
def jatek():

    szam = random.randint(0, 127)
    while True:
        tipp = int(input("Tippej egy számot: "))
        try:
            if tipp < szam:
                print("Kisebb számot tippeltél. ")
                pass

            if tipp > szam:
                print("Nagyobb számot tippeltél.")
                pass

            if tipp == szam:
                print("Eltaláltad a számot!!!")
                return True
        except:
            pass


jatek()