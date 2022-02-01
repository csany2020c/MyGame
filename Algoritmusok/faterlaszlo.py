from typing import List
from time import time

# def faktoralis(asd: int) -> int:
#     szorzat = 1
#     for i in range(2, asd + 1):
#         szorzat *= i
#     return szorzat


# print(faktoralis(6))

# 2. feladat
# print(8 % 3)

# primszam fuggveny
def fuggveny(n: int) -> list[int]:
    lista: List['int'] = list()
    # bemenet: int = int(input())
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista

# for i in fuggveny(26):
#     print(i)

# print(fuggveny(26))

# 3.feladat
# ts1 = time()
# def fuggveny1(n: int) -> bool:
#     return len(fuggveny(n)) == 2
#
# for i in range(0, 126):
#      print("{szam} {primszam}".format(szam=i, primszam=fuggveny1(i)))

#új számolás
# ts1 = time()
# for i in range(100000, 1000000):
#     primszame = fuggveny(i)  # Prímszám eldöntő függvény helye
#     if primszame:
#         print(i)
# ts2 = time()
# print("Az algoritmus {mp} másodpercig futott.".format(mp=(ts2 - ts1)))

def binaris() -> int:
    a = bin(237)
    # for i in range(8):
    #     >>>a<<2
    print(a)
binaris()