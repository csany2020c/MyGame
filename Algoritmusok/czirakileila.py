from typing import List

#class egytoltizenotig:
    #for i in range(1, 16):
#print(i)

class beolvasas:
    while(True):
        szam: int == int(input())

        if szam == 0:
            break

#def osztoparok(szam: int) -> int:
    #szamfele: int = szam // 2 + 1
    #osszeg: int = 0
    #for x in range(1, szamfele):
        #if szam % x == 0:
            #osszeg = osszeg + x
        #return osszeg
    #while(True):


#print(osztoparok(int(input())))

#def feladat00(lista: List) -> int:
 #   for i in range:






# 1. Készítsen függvényt, amely eldönti egy számról, hogy "tökéletes"-e.
def tokeletesszam(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
        if szam == osszeg:
            return


# A matematikában Mersenne-prímeknek nevezzük a kettő-hatványnál eggyel kisebb, azaz a 2n ‒ 1 alakban felírható prímszámokat, ahol n szintén prímszám.

def mersenne(a: float, b: float, c:float) -> List['float']:
    kilista: List['float'] = list()
    D: float
    return



# 2. Készítsen függvényt, amely listában adja vissza az első n darab Fibonacci számot. Az n a függvény bemenete.





# 3. Készítsen függvényt, amely két szám legkisebb közös többszörösét adja eredményül.

#def kicsitöbb(a: float, b:float) -> List['float']:


# 4. Készítsen függvényt, amely két szám legnagyobb közös osztóját adja eredményül.

def legnagyobbkoz(a: float, b: float) -> List['float']:
    kilista = List['float'] = list()
    if a == b:
        return a
    if a < b:
        return legnagyobbkoz(a, b - a)
    if a > b:
        return legnagyobbkoz(b, a - b)

print(legnagyobbkoz(21, 33))

