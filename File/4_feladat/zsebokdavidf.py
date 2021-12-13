from typing import List
from typing import TextIO


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        field: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(field[0])
        self.sportolokszama: int = int(field[1])
        self.sportag: str = str(field[2])
        self.versenyszam: str = str(field[3])

    def __int__(self) -> str:
        return "helyezes = {a}; sportolokszama = {b}; sportag = {c}; versenyszam = {d}".format(a=self.helyezes,
                                                                                               b=self.sportolokszama,
                                                                                               c=self.sportag,
                                                                                               d=self.versenyszam)

class Main:
    def __init__(self):
        global legtobb
        fajl: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = fajl.read()
        datalist: List['Data'] = list()
        lines: List['str'] = content.split(sep="\n")
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        fajl.close()

        print("3feladat:    " + str(len(lines)) + " darab magyar helyezés született")

        elsohelyezes = 0
        masodikhelyezes = 0
        harmadikhelyezes = 0
        osszeshelyezes = 0
        for index in range(0, len(lines)):
            if datalist[index].helyezes == 1:
                elsohelyezes = elsohelyezes + 1
                osszeshelyezes = osszeshelyezes + 1
            if datalist[index].helyezes == 2:
                masodikhelyezes = masodikhelyezes + 1
                osszeshelyezes = osszeshelyezes + 1
            if datalist[index].helyezes == 3:
                harmadikhelyezes = harmadikhelyezes + 1
                osszeshelyezes = osszeshelyezes + 1
        print("4feladat:    Arany: " + str(elsohelyezes))
        print("4feladat:    Ezüst: " + str(masodikhelyezes))
        print("4feladat:    Bronz: " + str(harmadikhelyezes))
        print("4feladat:    Összes: " + str(osszeshelyezes))

        pontok = 0
        for index in range(0, len(lines)):
            if datalist[index].helyezes == 1:
                pontok = pontok + 7
            if datalist[index].helyezes == 2:
                pontok = pontok + 5
            if datalist[index].helyezes == 3:
                pontok = pontok + 4
            if datalist[index].helyezes == 4:
                pontok = pontok + 3
            if datalist[index].helyezes == 5:
                pontok = pontok + 2
            if datalist[index].helyezes == 6:
                pontok = pontok + 1
        print("5feladat:    Elért pontok: " + str(pontok))

        uszaspontok = 0
        tornapontok = 0
        for index in range(0, len(lines)):
            if datalist[index].sportag == "uszas":
                uszaspontok = uszaspontok + 1
            if datalist[index].sportag == "torna":
                tornapontok = tornapontok + 1
        if tornapontok > uszaspontok:
            print("6feladat:    A torna sportágban szereztek több érmet")
        if tornapontok < uszaspontok:
            print("6feladat:    Az úszás sportágban szereztek több érmet")
        if tornapontok == uszaspontok:
            print("6feladat:    Az érmek száma egyenlő a két sportágban")

        legtobbsportolo = 0
        for index in range(0, len(lines)):
            if datalist[index].sportolokszama > legtobbsportolo:
                legtobb = index
        helyezes = datalist[legtobb].helyezes
        sportag = datalist[legtobb].sportag
        versenyszam = datalist[legtobb].versenyszam
        sportszam = datalist[legtobb].sportolokszama
        print("8feladat:    Helyezés: " + str(helyezes))
        print("8feladat:    Sportág: " + str(sportag))
        print("8feladat:    Versenyszám: " + str(versenyszam))
        print("8feladat:    Sportolók száma: " + str(sportszam))


Main()




