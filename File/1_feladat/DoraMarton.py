import string
from typing import TextIO
from typing import List
class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szuletes: str = fields[2]
        self.orszagkod: str = fields[3]

    def __str__(self) -> str:
        return "{x}; {y}; {txt}; {col}".format(x=self.ev, y=self.nev, txt=self.szuletes, col=self.orszagkod)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        i: int = 0
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()

        print("3. feladat")
        #print("Dijazottak szama: {db} fő ".format(db=len(datalist)))

        max: int = 0

        for i in range(1, len(datalist)):
            # print(i)
            if datalist[i].ev > datalist[max].ev:
                max = i

        print(datalist[max].ev)

        # kod: str = input()
        db: int = 0

        for index in range (0, len(datalist)):
            if datalist[index].ev >= 1970 and datalist[index].ev <= 1979:
                db += 1

        if db >= 0:
            print("A 70-es evekben {db} dijazott volt".format(db=db))

        if db == 0:
            print("innen nincs díjazott")

        print("6. feladat")

        ev: dict = dict()

        for k in range(0, len(datalist)):
            try:
                ev[datalist[k].ev]+=1
            except:
                ev[datalist[k].ev]=1

        for k, v in ev.items():
            print("{k} {v}".format(k=k, v=v))


Main()
