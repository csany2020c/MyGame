from typing import List


#def egytizenot():
    #for i in range(1, 16):
        #print(i)


#def beolvasasnullaig():
    #while (True):
        #szam: int = int(input())
        #if szam == 0:
            #break


#def beolvasasnullaig2():
    #szam: int = 1
    #while (szam != 0):
        #szam = int(input())


#class osszegzesnullaig():
    #osszeg: int = 0
    #szam: int = 1
    #while (szam != 0):
    #    szam = int(input())
    #    if szam != 0:
    #        osszeg += szam
    #        print("Az eddigi összeg: {sum}".format(sum=osszeg))
    #print("Az összeg: {sum}".format(sum=osszeg))


#def szamok():
    #beolvasas: int = 1
#    osszeg: int = 0
#    szorzat: int = 1
#    darab: int = 0
    #while (beolvasas != 0):
    #   beolvasas = int(input())
    #    if beolvasas != 0:
    #       osszeg += beolvasas
    #        szorzat *= beolvasas
    #        darab += 1
    #print(osszeg)
    #print(szorzat)
    #print(darab)


#def szorzat(list: List['int']) -> int:
    #sz: int = 1
    #for i in list:
        #sz *= i
    #return sz

    # Készítsen függvényt, amely a 0 végjelig beolvasott számok
    # listáját adja eredményül.

#l: List['int'] = (4, 2, 3)
#print(l)
#print(szorzat(l))


    #szam = int(input("Szám: "))
    #print("Osztók: {eredmeny}".format())


#def osztoosszeg(szam: int) -> int:
    #szamfele: int = szam // 2 + 1
    #osszeg: int = 0
    #for x in range(1, szamfele):
        #if szam % x == 0:
            #osszeg = osszeg + x
    #return osszeg

# print(osztoosszeg(int(input())))


#def baratsagosszamoke(a: int, b: int) -> bool:
    #return a != b and osztoosszeg(a) == b and osztoosszeg(b) == a

#print(baratsagosszamoke(6, 6))
#print(baratsagosszamoke(220, 284))
#print(baratsagosszamoke(1184, 1210))
#print(baratsagosszamoke(5020, 5564))


#def hatvanyozas(a: int, b: int) -> List['int']:
    # l: List['int'] = (2, 8)
    #return


#print(hatvanyozas(2, 8))
#print(hatvanyozas(3, 4))


# HF-------------------------------------------------------------------------------------------------------

# 0.0
# Készítsen függvényt, amelynek bemenete egy lista és egy szám. Válogassa ki a kimenetre egy új listába
# azokat a számokat, amelyek a bemeneti listában a bemeneti számmal maradék nélkül oszthatók.


def nullapontnulla(a: List['int'], b: int) -> List['int']:
    return

nullapontnullalista = [3, 54, 32, 52, 11, 75]

#print(nullapontnulla(nullapontnullalista))


# 0.1
# Készítsen függvényt amelynek bemenete egy lista, kimenete pedig logikai típus.
# A visszaadott érték legyen igaz, ha a listában van 0. Ha nincs, akkor hamis.


# ezmukodik
def nullapontegy(list: List['int']) -> bool:
    ertek = 0
    for i in list:
        if i == 0:
            ertek = ertek + 1
    if ertek >= 1:
        return True
    if ertek <= 1:
        return False


nullapontegylista = [32, 53, 532, 213, 46, 3, 0]

#print(nullapontegy(nullapontegylista))


# 1.
# Készítsen függvényt, amelynek a bemenete 2 szám, a kimenete pedig a kisebb szám a kettő közül.
# A neve min legyen.


# ezmukodik
def egy(szam1: int, szam2: int) -> int:
    if szam1 > szam2:
        return szam2
    if szam1 == szam2:
        return szam1, szam2
    if szam1 < szam2:
        return szam1


#print(egy(97, 64))


# 2.
# Készítsen függvényt, amelynek a bemenete egy lista, a kimenete pedig a legkisebb szám a lista elemei közül.
# A neve minlist legyen.
# http://szit.hu/doku.php?id=oktatas:programozas:programozasi_tetelek:mondatszeru_leiras


def ketto(list: List['int']) -> int:
    szam = 0
    for i in list:
        if szam < i:
            szam = i
        break
    for i in list:
        if szam > i:
            szam = i
    return szam


kettolista = [5, 14, 35, 68, 358, 521, 671, 713, 999]

#print(ketto(kettolista))


# 3.
# Készítsen függvényt, amelynek 3 szám a bemenete.
#   a mértani sorozat első tagja (a1)
#   egy mértani sorozat kvóciense (q)
#   a legenerált sorozat hossza. (n)
# Generálja le az első n értéket egy listába. (mértani sorozatát)
# https://hu.wikipedia.org/wiki/M%C3%A9rtani_sorozat


def harom(a1: int, q: int, n: int):
    lista: list = []
    for i in range(1, n+1):
        lista.append(a1*q**(i-1))
    return lista

#print(harom(4, 5, 9))


# 4.
# Készítsen függvényt, amelynek bemenete egy lista, visszaadott értéke pedig a lista elemeinek az összege.

# ezmukodik
def negy(list: List['int']) -> int:
    szam = 0
    for i in list:
        szam = szam + i
    return szam


negylista = [5, 14, 35, 68, 358, 521, 671, 713, 999]

#print(negy(negylista))


# 5.
# Számítsa ki a 3-as és 4-es függvény felhasználásával egy mértani sorozat első n elemének az összegét.
# A függvény kimenete egy szám legyen, a bemenete pedig a mértani sorozat generálásához szükséges értékek.


def ot(a1: int, q: int, n: int) -> int:
    szam = 0

    return

#print(ot(4, 5, 9))


# 6.
# Készítsen függvényt, amelynek bemenete 3 szám, amely egy másodfokú a,b,c paraméterei (float). ax^2 + bx + c
# https://hu.wikipedia.org/wiki/M%C3%A1sodfok%C3%BA_egyenlet
# A visszaadott érték egy lista legyen, amely az egyenlet megoldásait tartalmazza.
# Amennyiben az egyenletnek nincs megoldása a valós számok halmazán, üres listával térjen vissza.


def hat(a: float, b: float, c: float) -> List['float']:
    # ax^2 + bx + c
    megoldas: List['float'] = list()
    # megoldas: ax^2 + bx + c
    diszkriminans: b**2-4*a*c
    if diszkriminans < 0:
        print("Nincs megoldás.")

    return megoldas


hatlista = [4, 21, 54]

#print(hat(hatlista))



# HF2-------------------------------------------------------------------------------------------------------

# https://hu.wikipedia.org/wiki/T%C3%B6k%C3%A9letes_sz%C3%A1mok
# 1. Készítsen függvényt, amely eldönti egy számról, hogy "tökéletes"-e.


def tokeletesszame(szam: int) -> int:
    osszeg: int = 0
    for x in range(1, szam):
        if szam % x == 0:
            osszeg = osszeg + x
    if osszeg == szam:
        return True
    else:
        return False


# print(tokeletesszame(6))


# 2. Készítsen függvényt, amely a paraméterként megadott határokon belül megnézi az összes egész számra,
# hogy tökéletes-e, és a tökéletes számok listájával tér vissza.


def tokeletesszame2() -> List['float']:
    return


# print(tokeletesszame2())


# 3. Készítsen függvényt, amely egy bemeneti számot 10-es számrendszerben felbont helyiértékeire,
# és egy listával tér vissza.
# Pl: be: 623; ki: [6, 2, 3]


def helyiertekrebontas(szam: int) -> List['float']:
    megoldas: List['float'] = list()

    return


# print(helyiertekrebontas(623))


# 4. Készítsen függvényt, amely egy bemeneti számból kiszámolja a számjegyeinek az összegét.


def szamjegyekosszege(szam: int) -> int:
    return

# print(szamjegyekosszege(856))


# 5. Keressen olyan számokat, amelyeknek a számjegyeinek a szorzata megegyezik a számmal.


def szamjegyekszorzata():
    return

# print(szamjegyekszorzata())


# 6. Hány olyan háromjegyű szám van, melyben a számjegyek összege 15, és a szám osztható 15-tel?


def haromjegyu15():
    return

# print(haromjegyu15())


# 7. Armstrong-számok
#     Melyek azok a háromjegyű számok, amelyeknek a jegyeit külön-külön a harmadikra hatványozva
#     és ezeket összeadva az eredeti számot kapjuk vissza?
#     Létezik négyjegyű szám is olyan, ahol az egyes számjegyek negyedik hatványának összege visszaadja
#     az eredeti számot?


def Armstrong():
    return

# print(Armstrong())



# HF3-------------------------------------------------------------------------------------------------------

#https://hu.wikipedia.org/wiki/Mersenne-pr%C3%ADmek
# A matematikában Mersenne-prímeknek nevezzük a kettő-hatványnál eggyel kisebb, azaz a 2n ‒ 1 alakban
# felírható prímszámokat, ahol n szintén prímszám.

# 1.a Készítsen függvényt, amelynek a bemenete a hatványkitevő. Visszaadott értéke igaz vagy hamis az alapján,
# hogy Mersenne pím-e.
# A 2^n-1 alakban felírt számok nagy valószínűséggel prímek, főleg ha n is prím. De nem biztos,
# tehát meg kell vizsgálni.


def Mersenne(n: int) -> int:
    osszeg: int = 0

    if osszeg == n:
        return True
    else:
        return False


print(Mersenne(31))


# 1.b Keressen Mersenne prímeket. Az előző függvényt felhasználva keresse őket úgy, hogy a fenti függvény
# hatványkitevő bemenete prímszám legyen,
# A 2^n-1 alakban felírt számokra, ahol n prím minden esetben írja ki, hogy prím-e vagy nem.


def Mersenne2():
    return


# print(Mersenne2())


# https://hu.wikipedia.org/wiki/Fibonacci-sz%C3%A1mok
# 2. Készítsen függvényt, amely listában adja vissza az első n darab Fibonacci számot. Az n a függvény bemenete.


def Fibonacci(n: int) -> List['float']:
    return


# print(Fibonacci(50))


# https://hu.wikipedia.org/wiki/Legkisebb_k%C3%B6z%C3%B6s_t%C3%B6bbsz%C3%B6r%C3%B6s
# 3. Készítsen függvényt, amely két szám legkisebb közös többszörösét adja eredményül.


def legkisebbkozostobbszoros(a: int, b: int)-> int:
    eredmeny: int = 0

    return eredmeny


#print(legkisebbkozostobbszoros(9, 63))


# https://hu.wikipedia.org/wiki/Legnagyobb_k%C3%B6z%C3%B6s_oszt%C3%B3
# 4. Készítsen függvényt, amely két szám legnagyobb közös osztóját adja eredményül.


def legnagyobbkozososzto(a: int, b: int)-> int:
    eredmeny: int = 0

    return eredmeny


# print(legnagyobbkozososzto(74, 38))


# https://hu.wikipedia.org/wiki/Szfenikus_sz%C3%A1mok
# Szfenikus számok
# 5. Függvénnyel döntse el egy számról szfenikus szám-e.


def szfenikusszame(szam: int):
    szam: int = 0

    if szam == szam:
        return True
    else:
        return False


# print(szfenikusszame(30))
