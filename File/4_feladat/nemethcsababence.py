from typing import TextIO
from typing import List

class Adat:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        field: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(field[0])
        self.sportolokszama_csp: int = int(field[1])
        self.sport: str = str(field[2])
        self.versenyszam: str = str(field[3])

    def __int__(self) -> str:
        return "helyezes = {a}; sportolokszama_csp = {b}; sport = {c}; versenyszam = {d}".format(a=self.helyezes, b=self.sportolokszama_csp, c=self.sport, d=self.versenyszam)


class Main:
    def __init__(self):
        f: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        adatlist: List['Adat'] = list()
        sorok: List['str'] = content.split(sep="\n")
        for i in range(0, len(sorok)):
            d = Adat(sorok[i])
            adatlist.append(d)
        f.close()
        print("3. feladat")
        print("Pontszerző heléyezések száma:" + str(len(sorok)))

        arany = 0
        ezust = 0
        bronz = 0
        osszes = 0

        for index in range(0, len(sorok)):
            if adatlist[index].helyezes == 1:
                arany = arany + 1
                osszes = osszes + 1
            if adatlist[index].helyezes == 2:
                ezust = ezust + 1
                osszes = osszes + 1
            if adatlist[index].helyezes == 3:
                bronz = bronz + 1
                osszes = osszes + 1
        print("4. feladat")
        print("Arany:" + str(arany))
        print("Ezüst:" + str(ezust))
        print("Bronz:" + str(bronz))
        print("Osszes:" + str(osszes))

        print("5. feladat")

        pontok = 0

        for index in range(0, len(sorok)):
            if adatlist[index].helyezes == 1:
                pontok = pontok + 7
            if adatlist[index].helyezes == 2:
                pontok = pontok + 5
            if adatlist[index].helyezes == 3:
                pontok = pontok + 4
            if adatlist[index].helyezes == 4:
                pontok = pontok + 3
            if adatlist[index].helyezes == 5:
                pontok = pontok + 2
            if adatlist[index].helyezes == 6:
                pontok = pontok + 1
        print("Osszesen:" + str(pontok))

        print("6. feladat")

        uszas = 0
        torna = 0
        for index in range(0, len(sorok)):
            if adatlist[index].sport == "uszas":
                uszas = uszas + 1
            if adatlist[index].sport == "torna":
                torna = torna + 1
        if torna > uszas:
            print("A torna sportágban szereztek több érmet")
        if torna < uszas:
            print("Az úszás sportágban szereztek több érmet")
        if torna == uszas:
            print("Az érmek száma egyenlő a két sportágban")

        print("7. feladat, IDK :D")
Main()