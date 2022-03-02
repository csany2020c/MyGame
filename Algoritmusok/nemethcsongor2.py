from typing import List
from time import time
import math

def perfect(num: int) ->bool:
    idk = 0
    mar = 0
    for i in range(num -1):
        idk += 1
        if num % idk == 0:
            mar += idk
    if mar == num:
        return True
    else:
        return False


# print(perfect(6))


def helyiertek(num: int) -> List:
    lista = [int(a) for a in str(num)]
    return lista


# print(helyiertek(668435188))


def szamjegy(num: int) -> int:
    num2 = 0
    for i in str(num):
        num2 += int(i)
    return num2


# print(szamjegy(521))


def szorzat(num: int) -> bool:
    num2 = 1
    for i in str(num):
        num2 *= int(i)
    if num2 == num:
        return True
    return False


# print(szorzat(6))


def boldog(a: int) -> int:
    num = 0
    for i in str(a):
        num += int(i) * int(i)
    return num


def boldoge(a: int) -> bool:
    aktu: int = a
    if a < 0:
        print("nem pozitív")
        return False
    else:
        while aktu != 1:
            aktu = boldog(aktu)
            print(aktu)
            if aktu == 4 or aktu == 16 or aktu == 37 or aktu == 58 or aktu == 89 or aktu == 145 or aktu == 42 or aktu == 20:
                return False
            else:
                return True


ts1 = time()
print(boldoge(133))
ts2 = time()
print("{mp}".format(mp=(ts2 - ts1)))
