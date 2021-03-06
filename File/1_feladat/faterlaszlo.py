import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        # print(parseString)
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elethalal: str = fields[2]
        self.orszagkod: str = fields[3]
        szh: List['str'] = fields[2].split("-")  # 1922-2000
        # print(szh)
        self.szuletes: int = int(szh[0])
        self.halalozas: int = None
        if szh[1] != "":
            self.halalozas = int(szh[1])


    def __str__(self) -> str:
        return "Ev = {x};   Nev = {y};   Elethalal = {txt};   Orszagkod = {col}".format(x=self.ev, y=self.nev, txt=self.elethalal, col=self.orszagkod)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec//orvosi_nobeldijak.txt", "r", encoding="utf-8")
        content: str = f.read()
        # print(content)
        lines: List['str'] = content.split(sep="\n")
        # print(lines)
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        # for d in datalist:
        #     print(d)
        f.close()

        print("3. feladat: Díjazottak száma: {db} fő".format(db=len(datalist)))
        print(datalist[len(datalist) - 1].nev)
        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[max].ev < datalist[i].ev:
                max = i
        print(datalist[max].ev)

        kod: str = input()

        for index in range(0, len(datalist)):
            print(str(index) + " ---- " + str(datalist[index]))

        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].orszagkod == kod:
                db += 1
        print(db)
        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print()
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))

        szam: int = 0
        for o in range(0, len(datalist)):
            if datalist[o].ev >= 1980 and datalist[o].ev < 1990:
                szam += 1
        print("5.1 feladat")
        print("Az 1980-es években {db} díjazott volt. ".format(db=szam))

        orsz: str = "USA"
        sz: int = 0
        for z in range(0, len(datalist)):
            if datalist[z].orszagkod == orsz and datalist[z].ev <= 1970:
                sz += 1
        print("5.2")
        print("Az 1970-es évek előtti dijazottak száma: {db}".format(db=sz))

        sz1: int = 0
        for o in range(0, len(datalist)):
            if datalist[o].ev >= 1970 and datalist[o].ev < 1980:
                sz1 += 1
        print("Gyakorlás")
        print("Dijjak száma:{db}".format(db=sz1))

Main()