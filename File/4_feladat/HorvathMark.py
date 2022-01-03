from typing import List
from typing import TextIO

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(fields[0])
        self.team: int = int(fields[1])
        self.sport: str = fields[2]
        self.type: str = fields[3]

    def __str__(self) -> str:
        return "{h}; {te}; {s}; {ty}".format(h = self.helyezes, te = self.team, s = self.sport, ty = self.type)

class Olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        f.close()
        print("3. feladat")
        print("Pontszerző helyezések száma: " + str(len(lines)))

        print("4. feladat")
        Gold: int = 0
        Silver: int = 0
        Bronze: int = 0
        all: int = 0

        for i in range(0, len(lines)):
            if datalist[i].helyezes == 1:
                Gold += 1
                all += 1

            if datalist[i].helyezes == 2:
                Silver += 1
                all += 1

            if datalist[i].helyezes == 3:
                Bronze += 1
                all += 1

        print("Arany: {g}".format(g=Gold))
        print("Ezüst: {s}".format(s=Silver))
        print("Bronz: {b}".format(b=Bronze))
        print("Összesen: {a}".format(a=all))

        print("5.feladat")

        points: int = 0

        for i in range(0,len(lines)):
            if datalist[i].helyezes == 1:
                points += 7
            if datalist[i].helyezes == 2:
                points += 5
            if datalist[i].helyezes == 3:
                points += 4
            if datalist[i].helyezes == 4:
                points += 3
            if datalist[i].helyezes == 5:
                points += 2
            if datalist[i].helyezes == 6:
                points += 1

        print("Olimpiai pontok száma: {p}".format(p=points))

        print("6.feladat")

        torna: int = 0
        uszas: int = 0

        for i in range(0, len(lines)):
            if datalist[i].sport == "torna" and datalist[i].helyezes <= 3:
                torna += 1
            if datalist[i].sport == "uszas" and datalist[i].helyezes <= 3:
                uszas += 1
        if uszas < torna :
            print("Torna sportágban szerezek több érmet")
        if uszas > torna :
            print("Úszás sportágban szerezek több érmet")
        if uszas == torna :
            print("Egyenlő volt az érmek száma")

        print("8.feladat")

        max: int = 0

        for i in range(0, len(lines)):
            if datalist[i].helyezes <= 3 and datalist[i].team > datalist[max].team:
                max = i
        print("Helyezés: {m}".format(m = datalist[max].helyezes))
        print("Sportág: {m}".format(m =datalist[max].sport))
        print("Versenyszám: {m}".format(m = datalist[max].type))
        print("Sportolók száma: {m}".format(m = datalist[max].team))

Olvasas()