from typing import List

# Írassa ki a számokat 1-től 42-ig egyesével növekvően.
def egytolnegyvenkettoig():
    for i in range(1, 43):
        print(i)


# Olvasson be a billentyűzetről számokat addig, amíg 0-át nem írunk be.

def beolvasasvegjelig():
    # Fusson "örökkés" a ciklus.
    while (True):
        # Olvassunk be egy stringet a billentyűzetről, majd alakítsuk át egész számmá.
        # Az átalakított értéket tároljuk el a SZAM változóban.
        szam: int = int(input())

        if szam == 0:
            break


# Olvasson be a billentyűzetről számokat addig, amíg 0-át nem írunk be.

def beolvasasvegjelig2():
    # A SZAM vátozóban tároljuk a beolvasott értéket. Kezdetben egy olyan értéket kap
    # amivel a ciklusba beugrik. (Ha 0 lenne soha nem lépne be.)
    szam: int = 1
    while (szam != 0):
        # Beolvassa az értéket. Először stringként, majd int-re konvertálja.
        szam = int(input())
        # A ciklusmag végén visszadobja a feltételhez, amennyiben a beírt érték 0,
        # nem fut le újra a ciklus


# Olvasson be számokat 0 végjelig és a végjel után írja ki az összegüket.
def osszegzesvegjelig():
    # Létre kell hozni egy változót, amelynek az értéke kezdetben 0,
    # majd a későbbiekben ezt fogjuk növelni a beírt számokkal.
    osszeg: int = 0
    szam: int = 1
    while (szam != 0):
        szam = int(input())
        # Amennyiben a beírt szám nem 0, növeljük az összeg értékét a számmal.
        if szam != 0:
            osszeg += szam
            print("Az eddigi összeg: {sum}".format(sum=osszeg))
    print("Az összeg: {sum}".format(sum=osszeg))


# Készítsen egy listát, amelyben egész számokat tárol. Ennek a listának az
# elemeinek az összegét számolja ki, majd írja ki.

def osszegzeslistaban():
    lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
    osszeg: int = 0
    for i in lista: # Az i értékei: 6,5,9,3,1,2,3 (lista elemek)
        #print(i)
        osszeg += i
    print("Az összeg: {sum}".format(sum=osszeg))

# Készítsen egy listát, amelyben egész számokat tárol. Ennek a listának az
# elemeinek az összegét számolja ki, majd írja ki.

def osszegzeslistaban2():
    lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
    osszeg: int = 0
    for i in range(0, len(lista)): # Az i értékei: 0,1,2,3,4,5,6 (lista indexek)
        #print(i)
        osszeg += lista[i]
    print("Az összeg: {sum}".format(sum=osszeg))

# Készítsen függvényt, amelynek bemenete egy számokat tartalmazó lista,
# és a visszaadott értéke pedig a számok összege.
# Készítsen tesztet is.

# A függvény bemenetei a zárójelbe kerülnek. A kimenetének a típusát a -> után kell definiálni.
# A return után olyan típus jön, amit itt meghatároztunk.
def osszegzes(lista: List['int']) -> int:
    osszeg: int = 0
    for i in lista:  # Az i értékei: 6,5,9,3,1,2,3 (lista elemek)
        osszeg += i
    # A visszatérési értéket a függvény hívásának a helyén tudjuk majd felhasználni.
    return osszeg
# Teszt:
#lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
# A függvény paraméterként kapja meg a listát, majd a visszaadott értékét a print kapja meg.
#print(osszegzes(lista))
# Ugyan az, csak a lista a függvény paraméterében van létrehozva.
#print(osszegzes((4, 7, 8, 4)))