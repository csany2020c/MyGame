from typing import List
import math

def feladat(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

#print(feladat(int(input())))

def feladat2(a: int , b: int) -> bool:
    szamoszto1: int = a // 2 + 1
    osszeg1: int = 0
    szamoszto2: int = b // 2 + 1
    osszeg2: int = 0
    for x in range(1, szamoszto1):
        if a % x == 0:
            osszeg1 += x
    for y in range(1, szamoszto2):
        if b % y == 0:
            osszeg2 += y
    if osszeg1 != b and osszeg2 != a or a == b:
        return False
    else:
        return True


#print(feladat2(1184, 1210))


def baratiszam_kereso(szam: int) -> int:
    szam2: int = feladat(szam)
    if szam == feladat(szam2) and szam != szam2:
        return szam2



#print(baratiszam_kereso(int(input())))

def baratiszam_kereso_tanar(eddigkeres: int):
    for x in range(1, eddigkeres + 1):
        y = feladat(x)
        z = feladat(y)
        if x != y and z ==x:
            print("{x}, {y}".format(x = x, y = y))

#baratiszam_kereso_tanar(2000)

def hatvany(alap: int, kitevo: int) -> List['int']:
    lista: list = []
    x: int = 1
    for i in range(kitevo + 1):
        lista.append(x)
        x *= alap

    return lista


#print(hatvany(2, 32))

def feladat00(lista1: List['int'], oszto: int) -> List['int']:
    lista2: list = []
    for i in lista1:
        if i % oszto == 0:
            lista2.append(i)

    return lista2


#print(feladat00((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), 3))


def feladat01(lista: List['int']) -> bool:
    for i in lista:
        if i == 0:
            return True

#print(feladat01((0,1,2,3,4,5)))

def feladat1_min(szam1:int, szam2:int) -> int:
    if szam1 < szam2:
        return szam1
    else:
        return szam2

#print(feladat1_min(5,2))

def feladat2_minlist(lista: List['int']) -> int:
    x: int = lista[1]
    for i in lista:
        if x > i:
            x = i
    return x

#print(feladat2_minlist((100,600,20,1000,10340,1024)))

def feladat3_mertani_sorozat(a: int, q: int, n:int) -> List['int']:
    lista: list = []
    for i in range(1, n + 1):
        lista.append(a * q**(i-1))
    return lista

#print(feladat3_mertani_sorozat(1,2,10))

def feladat4_osszeg(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x

#print(feladat4_osszeg((1,2,4,8,16,32,64,128,256)))

def feladat5_F4_F3_osszeg(a: int, q: int, n: int) -> int:
    return feladat4_osszeg(feladat3_mertani_sorozat(a, q, n))

#print(feladat5_F4_F3_osszeg(1,2,10))

def feladat6_masodfokufugveny(a: float, b:float, c:float) -> List['float']:
    lista: list = []
    D = b*b - 4*a*c
    if D >= 0:
        x: int = (-b + math.sqrt(D)) / 2*a
        lista.append(x)
        y: int = (-b - math.sqrt(D)) / 2*a
        if x != y:
            lista.append(y)

    return lista

#print(feladat6_masodfokufugveny(1,3,-2))

def HF2feladat1_tökeletesszam(szam: int) -> bool:
    összeg: int = 0
    oszto: int = szam // 2
    for x in range(1, oszto + 1):
        if szam % x == 0:
            összeg += x
    if összeg == szam:
        return True
    else:
        return False

#print(HF2feladat1_tökeletesszam(28))

def HF2feladat2_tökeletesszam_lista(min: int, max: int) -> List['int']:
    lista: List['int'] = []
    for i in range(min, max):
        if HF2feladat1_tökeletesszam(i):
            lista.append(i)

    return lista

#print(HF2feladat2_tökeletesszam_lista(1, 10))


def HF2feladat3_szamfelbontas(szam: int) -> List['int']:
    lista: List['int'] = []
    for i in str(szam):
        lista.append(int(i))
    return lista

#print(HF2feladat3_szamfelbontas(123))

def HF2feladat4_szamjegyosszeg(szam: int) -> int:
    osszeg = 0
    for i in (HF2feladat3_szamfelbontas(szam)):
        osszeg += i
    return osszeg
#print(HF2feladat4_szamjegyosszeg(122))

def HF2feladat5_szamjegyszorzas(szam: int) -> bool:
    szorzat = 1
    for i in str(szam):
        szorzat *= int(i)
    if szorzat == szam:
        return True
    else:
        return False

#print(HF2feladat5_szamjegyszorzas(16))

def HF2feladat6_15szam() -> int:
    db = 0
    for i in range (100,1000):
        if i % 15 == 0 and HF2feladat4_szamjegyosszeg(i) == 15:
            db += 1
    return db

#print(HF2feladat6_15szam())

def HF2feladat7a_Armstrongszam() -> List['int']:
    lista: List = []
    összeg = 0
    for x in range(100, 1000):
        for i in (HF2feladat3_szamfelbontas(x)):
            összeg += i ** 3
        if összeg != x:
            összeg = 0
        else:
            lista.append(összeg)
            összeg = 0
    return lista

#print(HF2feladat7a_Armstrongszam())

def HF2feladat7b_Armstrongszam() -> List['int']:
    lista: List = []
    összeg = 0
    for x in range(1000, 10000):
        for i in (HF2feladat3_szamfelbontas(x)):
            összeg += i ** 4
        if összeg != x:
            összeg = 0
        else:
            lista.append(összeg)
            összeg = 0
    return lista


#print(HF2feladat7b_Armstrongszam())

def prim(szam: int) -> bool:
    if szam == 1: return False
    gyokpluszegy = int(math.sqrt(szam)) + 1
    for i in range(2, gyokpluszegy):
        if szam % i == 0:
            return False
    return True

#print(prim(1))

def Mersenszam(n: int):
    return 2**n - 1

def HF3feladat1a_Mersenneprim(hatvany: int) -> bool:
    return prim(hatvany) and prim(Mersenszam(hatvany))



#print(HF3feladat1a_Mersenneprim(6))

def HF3feladat1b_Mersenneprimkeres(a: int) -> List['int']:
    lista: List['int'] = []
    for i in range (2, a + 2):
        if HF3feladat1a_Mersenneprim(i):
            lista.append(i)
    return lista

print(HF3feladat1b_Mersenneprimkeres(50))

def HF3feladat2_Fibanacci(n: int) -> List['int']:
    lista: List['int'] = [0,1]
    for i in range (2, n):
        lista.append(lista[i-1] + lista[i-2])
    return lista

#print(HF3feladat2_Fibanacci(100))

def HF3feladat3_legkisebbtöbbszörös(a: int, b: int) -> int:
    szam = 0
    if a % b == 0:
        szam = a
    if b % a == 0:
        szam = b
    if b % a and a % b != 0:
        szam = a * b
    return szam

#print(HF3feladat3_legkisebbtöbbszörös(2, ))

def HF3feladat4_legnagyobb_köz_oszto(a: int, b:int) -> int:
    szam = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            if szam < i:
                szam = i
    return szam

#print(HF3feladat4_legnagyobb_köz_oszto(2,16))

def HF3feladat5_Szfenikus_szamok(szam:int) -> bool:
    x = 1
    lista: List['int'] = []
    for i in range(2, szam + 2):
        if prim(i) and szam % i == 0:
            lista.append(i)
    if len(lista) == 3:
        for y in lista:
            x *= y
    if x == szam:
        return True
    else:
        return False

#print(HF3feladat5_Szfenikus_szamok(130))

#def HF4feladat1_boldogszam(szam: int) -> bool: