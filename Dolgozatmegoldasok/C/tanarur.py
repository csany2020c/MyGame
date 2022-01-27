from typing import IO


class barlang:
    def __init__(self, parse: str = ""):
        l: list[str] = parse.split("\t")
        self.nev: str = l[0]
        self.hossz: float = float(l[1].replace(",", "."))
        self.kiterjedes: float = float(l[2].replace(",", "."))
        self.melyseg: float = float(l[3].replace(",", "."))
        self.magassag: float = float(l[4].replace(",", "."))
        self.telepules: str = l[5]

    def magasabb_mint_hosszabb(self) -> bool:
        return self.melyseg + self.magassag >= self.hossz

    def __str__(self):
        return "{n}, {h}, {k}, {m}, {a}, {t}".format(n=self.nev, h=self.hossz, m=self.melyseg, a=self.magassag, k=self.kiterjedes, t=self.telepules)


def main():
    #
    # r: IO = open("barlang.txt", encoding="UTF-8")
    # egesztartalom: str = r.read()
    # egesztartalom = egesztartalom.strip()
    # sorok = egesztartalom.split("\n")

    sorok: list[str] = open("barlang.txt", encoding="UTF-8").read().strip().split("\n")

    barlangok: list[barlang] = list()

    for i in range(1, len(sorok)):
        barlangok.append(barlang(sorok[i]))

    # for i in barlangok:
    #     print(i)
    #
    # for i in range(0, len(barlangok)):
    #     print(barlangok[i])

    hossz: float = 0
    for i in barlangok:
        hossz += i.hossz
    print(f"3. feladat: {hossz} m".format(hossz= hossz))

    print("4. feladat")
    telepulesnev: str = input()
    for i in barlangok:
        if telepulesnev == i.telepules:
            print(i.nev)

    print("6. feladat")
    db: int = 0
    for i in barlangok:
        if i.magasabb_mint_hosszabb():
            db+=1
            print(i.nev)
    print("{db} barlang van, ami magasabb, mint a milyen hosszú.".format(db=db))


    # depuletalagsor = barlang()
    # depuletalagsor.nev = "D"
    # depuletalagsor.melyseg = 8
    # depuletalagsor.telepules = "Zalaegerszeg"
    # print(depuletalagsor)
    # b = barlang("Mánfai-kőlyuk	310	12	4,3	7,7	Mánfa")
    # print(b)
    # b2 = barlang("Mészégető-források-barlangja	279	14,5	1,4	13,1	Orfű")
    # print(b2)


main()