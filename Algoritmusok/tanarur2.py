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



