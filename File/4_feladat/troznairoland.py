from typing import TextIO
from typing import List

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(fields[0])
        self.szam: int = int(fields[1])
        self.sportag: str = fields[2]
        self.versenyszam: str = fields[3]

    def __str__(self) -> str:
        return "Helyezés = {x}; Sportoló(k) száma = {y}; Sportág = {txt}; Versenyszám = {col}".format(x=self.helyezes, y=self.szam, txt=self.sportag, col=self.versenyszam)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs\helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            #print(d)
        f.close()

        #print("3.feladat:")
        #db: int = len(datalist)
        #print("Pontszerző helyezések száma: {db} fő".format(db=db))

        #print("4.feladat:")
        #elso: int = 0
        #masodik: int = 0
        #harmadik: int = 0
        #osszesen: int = 0
        #for index in range(0, len(lines)):
            #if datalist[index].helyezes == 1:
                #elso = elso + 1
                #osszesen = osszesen + 1
            #if datalist[index].helyezes == 2:
                #masodik = masodik + 1
                #osszesen = osszesen + 1
            #if datalist[index].helyezes == 3:
                #harmadik = harmadik + 1
                #osszesen = osszesen + 1
        #print("Arany:" + str(elso))
        #print("Ezüst:" + str(masodik))
        #print("Bronz:" + str(harmadik))
        #print("Összesen:" + str(osszesen))

        #print("5.feladat:")
        #pont: int = 0
        #for index in range(0, len(lines)):
            #if datalist[index].helyezes == 1:
                #pont = pont + 7
            #if datalist[index].helyezes == 2:
                #pont = pont + 5
            #if datalist[index].helyezes == 3:
                #pont = pont + 4
            #if datalist[index].helyezes == 4:
                #pont = pont + 3
            #if datalist[index].helyezes == 5:
                #pont = pont + 2
            #if datalist[index].helyezes == 6:
                #pont = pont + 1
        #print("Olimpiai pontok száma:" + str(pont))

        print("6.feladat:")
        uszas = 0
        torna = 0
        for index in range(0, len(lines)):
            if datalist[index].sportag == "uszas":
                uszas = uszas + 1
            if datalist[index].sportag == "torna":
                torna = torna + 1
        if torna > uszas:
            print("A torna sportágban szereztek több érmet")
        if torna < uszas:
            print("Az úszás sportágban szereztek több érmet")
        if torna == uszas:
            print("Az érmek száma egyenlő a két sportágban")

Main()