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
        return "{x};   {y};   {txt};   {col}".format(x=self.ev, y=self.nev, txt=self.elethalal, col=self.orszagkod)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r", encoding="utf-8")
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

        # # iterátoros végigjárás
        for it in datalist:
            print(it)
        #
        # # index alapú végigjárás
        for index in range(0, len(datalist)):
            print(str(index) + " ---- " + str(datalist[index]))

        db70: int = 0
        for it in datalist:
            if it.ev >= 1980 and it.ev <= 1989:
                print(it.nev)
                db70 += 1
        print("Az 1980-es években {db70} díjazott volt.".format(db70=db70))

        db70: int = 0
        for it in datalist:
            if it.ev <= 1970:
                if it.orszagkod == "USA":
                    db70 += 1
        print("{db70} 1970 előtti amerika díjazott volt.".format(db70=db70))

        db70: int = 0
        for it in datalist:
            if it.ev >= 1960:
                if it.orszagkod == "S":
                    db70 += 1
        print("{db70} 1970 előtti spanyol díjazott volt.".format(db70=db70))





Main()