from typing import List
from typing import TextIO

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmenyek: str = str(fields[5])

    def __str__(self) -> str:
        return "Év = {ev}; Hét = {het}; Forduló = {ford}; T13p1 = {t13p1}; Ny13p1 = {ny13p1}; Eredmények = {eredm}".format(ev=self.ev, het=self.het, ford=self.fordulo, t13p1=self.t13p1, ny13p1= self.ny13p1, eredm=self.eredmenyek)

class Feladatok:
    def __init__(self) -> None:
        super().__init__()
        f: List['str'] = open("toto.txt",).read().strip().split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(f)):
            d = Data(f[i])
            datalist.append(d)
            print(d)

        print("3,feladat:")
        fordulo = 0
        for i in range(0, len(datalist)):
            fordulo += datalist[i].fordulo
        print("Összesen {fordulo} forduló volt eddig.".format(fordulo=fordulo))

        print("4,feladat:")
        telitalalat = 0
        for i in range(0, len(datalist)):
            telitalalat += datalist[i].t13p1
        print("Eddig összesen {telitalalat} telitalálat volt.".format(telitalalat=telitalalat))

        print("5,feladat:")
        fizet = 0
        nyeremeny = 0
        for i in range(0, len(datalist)):
            nyeremeny = nyeremeny + i
        fizet = telitalalat * nyeremeny
        print("Eddig összesen {fizetet} Ft-ot fizettek ki.".format(fizetet=fizet))

        print("7,feladat:")
        #legnagyobb = 0
        #legkisebb = 0
        #for i in range(0, len(datalist)):
            #if legnagyobb < datalist[i].t13p1:
                #legnagyobb = datalist[i].t13p1

        print("8,feladat:")
        dontetlen = 0
        for i in range(0, len(datalist)):
            for i in str(datalist[i].eredmenyek):
                if i == "X":
                    dontetlen = dontetlen + 1
        print("Eddig összesen {dontetlen} db döntetlen volt.".format(dontetlen = dontetlen))

        print("9,feladat:")
        for i in range(0, len(datalist)):
            for i in str(datalist[i].eredmenyek):
                if i == "X":
                    print("Volt döntetlen!")
                    break
            break

Feladatok()