from typing import List

# Írasssa ki a számokat 1-től 15-ig.
def Szamok1tol15ig():
    for i in range(1, 16):
        print(i)

# Olvasson be a billentyűzetről számokat addig, amíg 0-át nem írunk be.

def beolvasasvegjelig():
    # Fusson "örökkés" a ciklus.
    while True:
        # Olvassunk be egy stringet a billentyűzetről, majd alakítsuk át egész számmá.
        # Az átalakított értéket tároljuk el a VALAMI változóban.
        valami: int = int(input())
        # Ha VALAMI értéke 0 lesz, akkor szakítsa meg a ciklust.
        if valami == 0:
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

# Olvasson be számokat 0 végjelig (amikor 0 a bevitt adat)
# és a végjel után írja ki az
# szorzatukat, összegüket és darabszámukat.
# A végjel értéke ne számíton bele az eredménybe.
def szamok():
    beolvasas: int = 1
    # Definiálunk változókat az összegnek, szorzatnak
    # és darabnak.
    # A szorzatnál fontos, hogy 1 legyen, mert 0-val nem
    # jó szorozni kezdetben
    osszeg: int = 0
    szorzat: int = 1
    darab: int = 0
    while (beolvasas != 0):
        beolvasas = int(input())
        # Ha a beolvasott érték nem a végjel...
        if beolvasas != 0:
            # Növelje az összeg változó értékét
            osszeg += beolvasas
            # Szorozza meg az eddigi szorzatot
            szorzat *= beolvasas
            # Növelje a darabot 1-el
            darab += 1
    # A ciklus után kiírás.
    print(osszeg)
    print(szorzat)
    print(darab)

# Készítsen függvényt, amelynek bemenete egy lista, kimenete
# egy szám. A lista elemeinek a szorzatát adja eredményül.

# A függvény bemenete a LISTA, kimenete INT
def szorzat(lista: List['int']) -> int:
    sz: int = 1
    for i in lista:
        sz *= i
    # A hívás helyén a return után írt érték jelenik meg.
    return sz


# Készítsen függvényt, amely a 0 végjelig beolvasott számok
# listáját adja eredményül.


def listababeolvas() -> List['int']:
    visszaadottlista = list()
    szam: int = 1
    while (szam != 0):
        szam = int(input())
        if szam != 0:
            visszaadottlista.append(szam)
    return visszaadottlista



l: List['int'] = (4, 2, 3)
print(l)
print(szorzat(l))

l2 = listababeolvas()
print(l2)
print(szorzat(l2))

