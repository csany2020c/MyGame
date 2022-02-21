from typing import List
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


def szorzat(num: int) ->bool:
    num2 = 1
    for i in str(num):
        num2 *= int(i)
    if num2 == num:
        return True
    return False


# print(szorzat(6))
