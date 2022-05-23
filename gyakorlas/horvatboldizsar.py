from typing import List


class Feladat:
    def __init__(self) -> None:
        olvasas = open("toto.txt", 'r', encoding="utf-8").read().strip().split(sep="\n")
        lista: List[Data] = list()
        for i in range(1, len(olvasas)):
            lista.append(Data(olvasas[i]))

        # 3.feladat

        print("3.feladat")
        fordulok = 0
        for z in range(len(lista)):
            fordulok += lista[z].fordulo
        print("{} forduló volt összesen".format(fordulok))

        # 4.feladat

        print("4.feladat")
        teli = 0
        for x in range(len(lista)):
            teli += lista[x].t13p1
        print("{} db telitalálatos szelvény van.".format(teli))

        # 5.feladat

        print("5.feladat")
        telikifizetett = 0
        for y in range(len(lista)):
            telikifizetett += lista[y].t13p1 * lista[y].ny13p1
        print("{} Ft a kifizetett pénz összege.".format(telikifizetett))

        # 8.feladat

        print("8.feladat")
        dontetlenek = 0
        for o in range(0, len(lista)):
            for o in str(lista[o].eredmenyek):
                if o == "X":
                    dontetlenek += 1
        print("{} db döntetlen volt.".format(dontetlenek))

        # 9.feladat

        print("9.feladat")
        vandxd = 0
        for q in range(0, len(lista)):
            for q in str(lista[q].eredmenyek):
                if q == "X":
                    vandxd += 1
                    if vandxd == 1:
                        print("Van döntetlen.")



class Data:
    def __init__(self, szokoz: str) -> None:
        szelet: List['str'] = szokoz.split(" ")
        self.ev: int = int(szelet[0])
        self.het: int = int(szelet[1])
        self.fordulo: int = int(szelet[2])
        self.t13p1: int = int(szelet[3])
        self.ny13p1: int = int(szelet[4])
        self.eredmenyek: str = str(szelet[5])

    def __str__(self) -> str:
        return "Év = {}; Hét = {}; Forduló = {}; T13p1 = {}; Ny13p1 = {}; Eredmények = {}".format(self.ev, self.het, self.fordulo, self.t13p1, self.ny13p1, self.eredmenyek)


Feladat()
