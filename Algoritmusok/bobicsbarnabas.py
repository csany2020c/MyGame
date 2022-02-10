from typing import List

def osztoosszeg(szam: int, osszeg: int) -> int:
    szamfele: int = szam // 2 + 1
    szamfele2: int = osszeg // 2 + 1
    osszeg2: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    for o in range(1, szamfele2):
        if osszeg % o == 0:
            osszeg2 = osszeg2 + o
    if szam == osszeg2:
        print("True")
    else:
        print("False")
    print(osszeg2)
    return osszeg

print(osztoosszeg(6, 6))
print(osztoosszeg(326, 326))
print(osztoosszeg(220, 284))



