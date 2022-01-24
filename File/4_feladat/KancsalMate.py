from typing import TextIO
from typing import List
import string

class Data:

    def __init__(self, parsestring : str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(fields[0])
        self.szama: int = int(fields[1])
        self.sportag: str = str(fields[2])
        self.versenyszam: str = str(fields[3])

    def __str__(self) -> str:
        return "Versenyző helyezése:{x} Helyezések száma:{y} Sportag:{c} Versenyszam:{v}".format(x= self.helyezes, y= self.helyezes, c= self.sportag, v= self.versenyszam)


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()
        #3. feladat
        g = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes < 7:
                g = g + 1
        print(g)

        #4.feladat
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        h = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == 1:
                a = a + 1
            if datalist[index].helyezes == 2:
                b = b + 1
            if datalist[index].helyezes == 3:
                c = c + 1
            if datalist[index].helyezes == 4:
                d = d + 1
            if datalist[index].helyezes == 5:
                e = e + 1
            if datalist[index].helyezes == 6:
                h = h + 1
        print("Első helyezettek:", a)
        print("Második helyezettek", b)
        print("Harmadik helyezettek", c)
        print("Összes", a+b+c)

        #5. feladat
        points = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == 1:
                points = points + 7
            if datalist[index].helyezes == 2:
                points = points + 5
            if datalist[index].helyezes == 3:
                points = points + 4
            if datalist[index].helyezes == 4:
                points = points + 3
            if datalist[index].helyezes == 5:
                points = points + 2
            if datalist[index].helyezes == 6:
                points = points + 1
        print("Összes pont:", points)

        #6.feladat
        uszas = 0
        torna = 0
        for index in range(0, len(datalist)):
            if datalist[index].sportag == "uszas":
                uszas = uszas + 1
            if datalist[index].sportag == "torna":
                torna = torna + 1
        if torna > uszas:
            print("Torna sportágban szereztek több érmet")
        if torna < uszas:
            print("Az úszás sportágban szereztek több érmet")
        if torna == uszas:
            print("Az érmek száma egyenlő")
Main()


