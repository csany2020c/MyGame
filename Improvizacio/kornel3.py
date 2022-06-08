

def szamolas(pontszam:int, maxpont:int) -> int:
    return pontszam / maxpont * 100

print(szamolas(int(input("Elért pontszám: ")), int(input("Maximális pontszám: "))))