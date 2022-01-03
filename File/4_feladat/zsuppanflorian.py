from typing import List
from typing import TextIO

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.szam: int = int(fields[1])
        self.sportag: str = fields[2]
        self.versenyszam: str = fields[3]


    def __str__(self) -> str:
        return "Helyezés = {a}; Rajtszám = {b}; Sportág = {c}; Versenyszám = {d}".format(a=self.helyezes, b=self.szam, c=self.sportag, d=self.versenyszam)

class Main:
    def __init__(self) -> None:
        super().__init__()
        fajl: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf8")
        content: str = fajl.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            #print(d)
        fajl.close()

#3.feladat
        print("3.feladat:")
        print("Pontzszerző helyezések száma : {db} fő".format(db=len(datalist)))
#4.feladat
        print("4. feladat:")
        elso: int = 1
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == elso:
                db += 1
        print("Arany: {db}".format(db=db))


        masodik: int = 2
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == masodik:
                db += 1
        print("Ezüst: {db}".format(db=db))

        harmadik: int = 3
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == harmadik:
                db += 1
        print("Bronz: {db}".format(db=db))

        db: int = 0
        for i in range(0, len(datalist)):
            if datalist[i].helyezes >= 1 and datalist[i].helyezes <= 3:
                db += 1
        print("Összesen: {db}".format(db=db))

        print("5.feladat")
        elso: int = 1
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == elso:
                db += 1 * 7
            if datalist[index].helyezes == elso + 1:
                db += 1 * 5
            if datalist[index].helyezes == elso + 2:
                db += 1 * 4
            if datalist[index].helyezes == elso + 3:
                db += 1 * 3
            if datalist[index].helyezes == elso + 4:
                db += 1 * 2
            if datalist[index].helyezes == elso + 5:
                db += 1
        print("Olimpiai pontok száma: {db}".format(db=db))
Main()