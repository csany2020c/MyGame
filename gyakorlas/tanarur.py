from typing import List, TextIO


class Adatok:
    def __init__(self, Parsestring: str) -> None:
        super().__init__()
        fieldls: List['str'] = Parsestring.strip().split(" ")
        self.ev: int = int(fieldls[0])
        self.het: int = int(fieldls[1])
        self.fordulo: int = int(fieldls[2])
        self.T13p1: int = int(fieldls[3])
        self.Ny13p1: int = int(fieldls[4])
        self.Eredmenyek: str = fieldls[5]

    def __str__(self):
        return "ev = {a}, het = {b}, fordulo = {c}, T13p1 = {d}, Ny13p1e = {e}, Eredmenyek = {f}".format(a=self.ev, b=self.het, c=self.fordulo, d=self.T13p1, e=self.Ny13p1, f=self.Eredmenyek)

    def kifizetett(self) -> int:
        return self.T13p1 * self.Ny13p1

    def dontetlenekszama(self) -> int:
        db: int = 0
        for i in self.Eredmenyek:
            if i == "X":
                db+= 1
        return db


class Program:

    def __init__(self, fajlnev: str) -> None:
        super().__init__()
        lista: List['Adatok'] = list()
        for i in open(fajlnev, mode="r").read().strip().split("\n"):
            lista.append(Adatok(i))
        # for i in lista:
        #     print(i)
        print("3. feladat: ")
        print(len(lista))
        print("4. feladat: ")
        p: int = 0
        for i in lista:
            p += i.T13p1
        print(p)
        # print(lista[9].kifizetett())
        print("7. feladat: ")
        ismertlegnagyobb: Adatok = lista[0]
        for i in lista:
            if i.Ny13p1 > ismertlegnagyobb.Ny13p1:
                ismertlegnagyobb = i
        print(ismertlegnagyobb.ev)
        print(ismertlegnagyobb.het)

        ismertlegkisebb: Adatok = None
        for i in lista:
            if i.Ny13p1 > 0 and (ismertlegkisebb == None or \
                    i.Ny13p1 < ismertlegkisebb.Ny13p1):
                ismertlegkisebb = i
        print(ismertlegkisebb.ev)
        print(ismertlegkisebb.het)

        print(lista[0].dontetlenekszama())

        i = 0
        while i < len(lista) and lista[i].dontetlenekszama() != 0:
            i += 1
        if i >= len(lista):
            print("Nem volt olyan hét, amikor nem volt döntetlen")
        else:
            print("Volt olyan hét, amikor nem volt döntetlen")

        if self.voltedontetlennelkulihet(lista):
            print("Volt olyan hét, amikor nem volt döntetlen")
        else:
            print("Nem volt olyan hét, amikor nem volt döntetlen")

    def voltedontetlennelkulihet(self, lista: List['Adatok']):
        for i in lista:
            if i.dontetlenekszama() == 0:
                return True
        return False


Program("toto.txt")

# egypeldany: Adatok = Adatok("2020 17 1 30 0 2221XX12222121")
# megegypeldany: Adatok = Adatok("2023 10 2 10 2 21112xxxxxxx21")
# print(egypeldany)
# print(megegypeldany)
