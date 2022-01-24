class Film:

    def __init__(self, parse: str):
        # print(parse)
        darabolt: list[str] = parse.strip().split("\t")
        # print(darabolt)
        self.cim: str = darabolt[1]
        self.ev: int = int(darabolt[2])
        self.hossz: int = int(darabolt[3])

    def __str__(self) -> str:
        return "{cim}\t{ev}\t{hossz}".format(cim=self.cim, ev=self.ev, hossz = self.hossz)

    def is_long(self) -> bool:
        # if self.hossz > 90:
        #     return True
        # else:
        #     return False
        return self.hossz > 90

def main():
    # f = open("film.txt", mode = "r", encoding="windows-1250")
    # s = f.read().strip()
    # sorok: list[str] = s.split("\n")
    # print(sorok)
    adatok: list[Film] = []
    sorok: list[str] = open("film.txt", mode="r", encoding="windows-1250").read().strip().split("\n")
    for i in range(1, len(sorok)):
        adatok.append(Film(sorok[i]))
        # f1: Film = Film(sorok[i])
        # adatok.append(f1)
        # print(f1)

    osszeg: int = 0
    for i in adatok:
        osszeg += i.hossz
    print("3. feladat: Az összes film hossza {hossz}".format(hossz=osszeg))

    print("4. feladat: Kérek egy évszámot:")
    evszam: int = int(input())
    for i in adatok:
        if evszam == i.ev:
            print(i.cim)
    print("5. feladat:")
    for i in adatok:
        if not i.is_long():
            print(i.cim)


main()