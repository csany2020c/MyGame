def binaris(bemenet: int) -> str:
    b: str = ''
    while bemenet > 0:
        if bemenet % 2 == 0:
            bemenet = bemenet // 2
            b = '0' + b
        else:
            bemenet = bemenet // 2
            b = '1' + b
    return b


szam = 20220208
print("A " + str(szam) + " bináris értéke " + str(binaris(szam) + "."))
