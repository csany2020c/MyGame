import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elethalal: str = fields[2]
        self.orszagkod: str = fields[3]
        szh: List['str'] = fields[2].split("-")  # 1922-2000
        self.szuletes: int = int(szh[0])
        self.halalozas: int = None
        if szh[1] != "":
            self.halalozas = int(szh[1])


    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col}".format(x=self.ev, y=self.nev, txt=self.elethalal, col=self.orszagkod)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec//orvosi_nobeldijak.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        f.close()

        print("3. feladat: Díjazottak száma: {db} fő".format(db=len(datalist)))
        print(datalist[len(datalist) - 1].nev)
        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[max].ev < datalist[i].ev:
                max = i
        print(datalist[max].ev)

        kod: str = input()

        db:int = 0
        utolso:int = -1
        for index in range(0, len(datalist)):
            if datalist[index].orszagkod == kod:
                db += 1
                utolso = index
        print(db)
        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print(datalist[utolso])
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))

        db70: int = 0
        for it in datalist:
            if it.ev >= 1970 and it.ev <= 1979:
                print(it.nev)
                db70 += 1
        print("Az 1970-es években {db70} díjazott volt.".format(db70 = db70))

        ev: dict = dict()
        for k in range(0, len(datalist)):
            try:
                ev[datalist[k].ev]+=1
            except:
                ev[datalist[k].ev]= 1

        for k, v in ev.items():
            print("{k} {v}".format(k=k, v=v))

Main()