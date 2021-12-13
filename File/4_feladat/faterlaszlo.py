import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.sportolokszama: int = int(fields[1])
        self.sportagnev: str = fields[2]
        self.versenyszam: str = fields[3]

    def __str__(self) -> str:
        return "Helyzes = {x}; Sportolokszama = {y}; Sportagnev = {txt}; Versenyszam = {col}".format(x=self.helyezes, y=self.sportolokszama, txt=self.sportagnev, col=self.versenyszam)


class Read:
    def __init__(self):
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()

        print("3.feladat:")
        print("Pontszerző helyezések száma: {db}".format(db=len(datalist)))

        print("4. feladat:")

        ehely: int = 1
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == ehely:
                db += 1
        print("Arany: {db}".format(db=db))


        mhely: int = 2
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == mhely:
                db += 1

        print("Ezüst: {db}".format(db=db))

        hhely: int = 3
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == hhely:
                db += 1

        print("Bronz: {db}".format(db=db))

        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes >= 1 and datalist[index].helyezes <= 3:
                db += 1

        print("Összesen: {db}".format(db=db))

        eshely: int = 1
        mshely: int = 2
        hshely: int = 3
        nshely: int = 4
        oshely: int = 5
        hashely: int = 6
        db: int = 0
        db1: int = 0
        db2: int = 0
        db3: int = 0
        db4: int = 0
        db5: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].helyezes == eshely:
                db += 1 * 7
            if datalist[index].helyezes == mshely:
                db1 += 1 * 5
            if datalist[index].helyezes == hshely:
                db2 += 1 * 4
            if datalist[index].helyezes == nshely:
                db3 += 1 * 3
            if datalist[index].helyezes == oshely:
                db4 += 1 * 2
            if datalist[index].helyezes == hashely:
                db5 += 1
        print("Olimpiai pontok száma: {db}".format(db=db + db1 + db2 + db3 + db4 + db5))


Read()