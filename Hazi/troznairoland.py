import random
from typing import List
from random import randint

def __init__(self) -> None:
    super().__init__()

# def egyesfeladat() -> int:
#     eredmeny = 0
#     elsoszam: int = int(input("Kérem adja meg az első számot!: "))
#     masodikszam: int = int(input("Kérem adja meg a második számot!: "))
#     harmadikszam: int = int(input("Kérem adja meg a harmadik számot!: "))
#     eredmeny = max(elsoszam, masodikszam, harmadikszam)
#     print(f"A legnagyobb szám: {eredmeny}")
#
# egyesfeladat()

# def kettesfeladat(l: list[int]):
#     osszeguk = 0
#     atlag = 0
#     for i in range(len(l)):
#         osszeguk += l[i]
#     atlag = osszeguk / 8
#     for i in range(len(l)):
#         if l[i] < atlag:
#             kissebb.append(l[i])
#     print(atlag)
#     print(kissebb)
#
# kissebb: List['int'] = list()
# kettesfeladat([1, 2, 3, 4, 5, 6, 7, 8])

# def negyesfeladat():
#     while True:
#         szam: int = int(input("Kérem adjon meg egy számot: "))
#         if szam % 21 == 0:
#             print("A beírt szám osztható 21-el.")
#             break
#         else:
#             pass
#             print("A szám nem osztható 21-el!")
#
# negyesfeladat()

def otosfeladat():
    szam = random.randint(0, 127)
    while True:
        be: int = int(input("Kérem adjon meg egy számot 0 és 127 között!: "))
        if szam < be:
            print("Sajnálom, a gondolt szám ennél kissebb lesz :(")
        if szam > be:
            print("Sajnálom, a gondolt szám ennél nagyobb lesz :(")
        if szam == be:
            print("Gratulálok eltalálta a számot! :)")
            break

otosfeladat()