import math
from typing import List
from time import time
from math import *



def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

# print(osztoosszeg(int(input())))

def baratiszamoke(a: int, b: int) -> bool:
    return a != b and osztoosszeg(a) == b and osztoosszeg(b) == a

def baratitesztlassu(eddigkeres: int):
    for x in range(1, eddigkeres + 1):
        for y in range(1, eddigkeres + 1):
            if baratiszamoke(x, y):
                print("{x} {y}".format(x=x, y=y))

def baratitesztgyors(eddigkeres: int):
    for x in range(1, eddigkeres + 1):
        if baratiszamoke(x, osztoosszeg(x)):
            print("{x} {y}".format(x=x, y=osztoosszeg(x)))
























































