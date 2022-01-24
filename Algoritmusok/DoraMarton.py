from typing import List

def szamolas():
    for i in range(1, 16):
       print(i)

def beolvasasvegjelig():
    while True:
        valami: int = int(input())
        if valami == 0:
            break

def szamok():
    szam: int = 1
    osszeg: int = 0
    szorzat: int = 1
    db: int = 0
    while szam != 0:
        szam = int(input())
        if szam != 0:
            osszeg += szam
            szorzat = szorzat * szam
            db += 1

    print(osszeg)
    print(szorzat)
    print(db)

def woohoo():
    list: List['int'] = (4, 2, 3)
    szorzat: int = 1
    for i in list:
        szorzat *= i
    print(szorzat)

def asdf():
    

asdf()