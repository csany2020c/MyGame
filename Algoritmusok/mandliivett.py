from typing import List
import math


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


def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

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
    kilista: list = []
    for i in a:
        if i % b == 0:
            kilista.append(i)
    return kilista


# print(nullapontnulla((1,4,3,6,8,5,17,34,67,56), 6))


# 0.1
# Készítsen függvényt amelynek bemenete egy lista, kimenete pedig logikai típus.
# A visszaadott érték legyen igaz, ha a listában van 0. Ha nincs, akkor hamis.


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
    return negy(harom(a1, q, n))

#print(ot(4, 5, 9))


# 6.
# Készítsen függvényt, amelynek bemenete 3 szám, amely egy másodfokú a,b,c paraméterei (float). ax^2 + bx + c
# https://hu.wikipedia.org/wiki/M%C3%A1sodfok%C3%BA_egyenlet
# A visszaadott érték egy lista legyen, amely az egyenlet megoldásait tartalmazza.
# Amennyiben az egyenletnek nincs megoldása a valós számok halmazán, üres listával térjen vissza.


def hat(a: float, b: float, c: float) -> List['float']:
    # ax^2 + bx + c
    megoldas: list =[]
    # megoldas: ax^2 + bx + c
    diszkriminans: b**2-4*a*c
    if diszkriminans < 0:
        print("Nincs megoldás.")
    if megoldas >= 0:
        x: int = (-b + math.sqrt(diszkriminans))/2*a
        megoldas.append(x)
        y: int = (-b - math.sqrt(diszkriminans))/2*a
    return megoldas


# print(hat(4, 21, 54))


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


def tokeletesszame2(a: int, b: int) -> List['int']:
    lista: List['int'] = list()
    for i in range(a, b + 1):
        szam = tokeletesszame(i)
        if szam == True:
            lista.append(i)
    return lista


#print(tokeletesszame2(1, 50))


# 3. Készítsen függvényt, amely egy bemeneti számot 10-es számrendszerben felbont helyiértékeire,
# és egy listával tér vissza.
# Pl: be: 623; ki: [6, 2, 3]


def helyiertekrebontas(szam: int) -> List['float']:
    megoldas: List['float'] = []
    while szam > 0:
        megoldas.append(szam % 10)
        szam = szam // 10
    megoldas.reverse()
    return megoldas


#print(helyiertekrebontas(754))


# 4. Készítsen függvényt, amely egy bemeneti számból kiszámolja a számjegyeinek az összegét.


def szamjegyekosszege(szam: int) -> int:
    osszeg = 0
    for i in (helyiertekrebontas(szam)):
        osszeg += i
    return osszeg


#print(szamjegyekosszege(856))


# 5. Keressen olyan számokat, amelyeknek a számjegyeinek a szorzata megegyezik a számmal.


def szamjegyekszorzata(a: int) -> bool:
    szam = 1
    for i in str(a):
        szam = szam * int(i)
        if szam == a:
            return True
        else:
            return False


# print(szamjegyekszorzata(1))


# 6. Hány olyan háromjegyű szám van, melyben a számjegyek összege 15, és a szám osztható 15-tel?


def haromjegyu15() -> int:
    darab = 0
    for i in range(100, 1000):
        if i % 15 == 0 and szamjegyekosszege(i) == 15:
            darab += 1
    return darab


#print(haromjegyu15())


# 7. Armstrong-számok
#     Melyek azok a háromjegyű számok, amelyeknek a jegyeit külön-külön a harmadikra hatványozva
#     és ezeket összeadva az eredeti számot kapjuk vissza?
#     Létezik négyjegyű szám is olyan, ahol az egyes számjegyek negyedik hatványának összege visszaadja
#     az eredeti számot?


def Armstrong() -> List['int']:
    list: List = []
    osszeg = 0
    for x in range(100, 1000):
        for i in (helyiertekrebontas(x)):
            osszeg += i ** 3
        if osszeg != x:
            osszeg = 0
        else:
            list.append(osszeg)
            osszeg = 0
    return list

# print(Armstrong())



# HF3-------------------------------------------------------------------------------------------------------

#https://hu.wikipedia.org/wiki/Mersenne-pr%C3%ADmek
# A matematikában Mersenne-prímeknek nevezzük a kettő-hatványnál eggyel kisebb, azaz a 2n ‒ 1 alakban
# felírható prímszámokat, ahol n szintén prímszám.

# 1.a Készítsen függvényt, amelynek a bemenete a hatványkitevő. Visszaadott értéke igaz vagy hamis az alapján,
# hogy Mersenne pím-e.
# A 2^n-1 alakban felírt számok nagy valószínűséggel prímek, főleg ha n is prím. De nem biztos,
# tehát meg kell vizsgálni.


def prim0(szam: int) -> bool:
    if szam == 1: return False
    gyokpluszegy = int(math.sqrt(szam)) + 1
    for i in range(2, gyokpluszegy):
        if szam % i == 0:
            return False
    return True


def prim1(szam: int):
    if szam == 1: return False
    return osztoosszeg(szam) == 1


def mersenneszam(n: int):
    return 2**n - 1


def mersenneprime(a: int):
    return prim0(a) and prim0(mersenneszam(a))

#print(mersenneprime())


# 1.b Keressen Mersenne prímeket. Az előző függvényt felhasználva keresse őket úgy, hogy a fenti függvény
# hatványkitevő bemenete prímszám legyen,
# A 2^n-1 alakban felírt számokra, ahol n prím minden esetben írja ki, hogy prím-e vagy nem.


def Mersenne2(n: int) -> bool:
    asd: int = 0
    #for i in (mersenneprime(a)):
        #return
    for i in (mersenneszam(n)):
        if n == asd:
            return True
        else:
            return False


# print(Mersenne2(7))


# https://hu.wikipedia.org/wiki/Fibonacci-sz%C3%A1mok
# 2. Készítsen függvényt, amely listában adja vissza az első n darab Fibonacci számot. Az n a függvény bemenete.


def Fibonacci(n: int) -> List['float']:
    list: List['int'] = [0, 1]
    for i in range(1, n):
        list.append(list[i - 1] + list[i - 2])
    return list


# print(Fibonacci(50))


# https://hu.wikipedia.org/wiki/Legkisebb_k%C3%B6z%C3%B6s_t%C3%B6bbsz%C3%B6r%C3%B6s
# 3. Készítsen függvényt, amely két szám legkisebb közös többszörösét adja eredményül.


def legkisebbkozostobbszoros(a: int, b: int)-> int:
    eredmeny: int = 0
    if a % b == 0:
        eredmeny = a
    if b % a == 0:
        eredmeny = b
    if a % b and b % a > 0:
        eredmeny = a * b
    return eredmeny


# print(legkisebbkozostobbszoros(9, 63))


# https://hu.wikipedia.org/wiki/Legnagyobb_k%C3%B6z%C3%B6s_oszt%C3%B3
# 4. Készítsen függvényt, amely két szám legnagyobb közös osztóját adja eredményül.


def legnagyobbkozososzto(a: int, b: int)-> int:
    eredmeny: int = 0
    for x in range(1, a + 1):
        if a % x == 0 and b % x == 0:
            if eredmeny < x:
                eredmeny = x
    return eredmeny


#print(legnagyobbkozososzto(5, 500))


# https://hu.wikipedia.org/wiki/Szfenikus_sz%C3%A1mok
# Szfenikus számok
# 5. Függvénnyel döntse el egy számról szfenikus szám-e.


def szfenikusszame(a: int) -> bool:
    szam = 0
    list: List['int'] = []
    for i in range(1, a):
        if prim0(i) and szam % i == 0:
            list.append(i)
            #
            #
    if szam == a:
        return True
    else:
        return False


# print(szfenikusszame(30))



# HF4-------------------------------------------------------------------------------------------------------

# https://hu.wikipedia.org/wiki/Boldog_sz%C3%A1m
# Boldog szám az a pozitív egész szám, amelyre igaz, hogy ha kiszámítjuk számjegyeinek négyzetösszegét,
# majd ezt az így kapott számmal szükség szerint addig ismételjük, amíg egyjegyű számot nem kapunk,
# akkor az eredmény 1 lesz.
# Például boldog szám a 23, mert 2²+3²=4+9=13, 1²+3²=1+9=10, 1²+0²=1+0=1.
# Azt a számot, amelynél a folyamat végeredménye nem 1, boldogtalan számnak nevezzük.

# 1. Döntse el egy számról, hogy boldog-e. Bemenet a szám, kimenet pedig logikai érték.


def boldoge(szam: int) -> bool:
    szamm: int = 0
    #for i in range():

    if szamm == szam:
        return True
    else:
        return False


#print(boldoge(31))


# 2. Keresse boldog számokat egy paraméterként megadott tartományban.


def kettoo()-> List['int']:
    list: List = []
    osszeg = 0
#    for x in range(1, 200):
#        for i in (boldoge(x)):

    return list


# print(kettoo(30))


# 3. Minden boldog szám esetében a számítás eredményeként megkapott összes szám boldog, amíg el nem érjük az 1-et.
#    Készítsen adatszerkezetet a boldog számok gráfjának a tárolására, és fűzze fel a keresett számokat.


def haromm() -> List['int']:
    eredmeny: int = 0
    return eredmeny


# print(haromm(30))


# 4. A boldog számok keresését gyorsítsa meg úgy, hogy a korábbi keresési eredményeket felhasználja.


def negyy():
    #for i in range(1, 20000):
    return


# print(negyy(30))
