from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elet: str = fields[2]
        self.orszag: str = fields[3]


    def __str__(self) -> str:
        return "Year = {x}; Name = {y}; Born-death = {txt}; Country = {col}".format(x=self.ev, y=self.nev, txt=self.elet, col=self.orszag)


class olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['data'] = list()
        for i in range(1, len(lines) - 1):
            d = data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()

        print("3. feladat")
        print("Díjazottak száma: {db} fő ".format(db=len(datalist)))

        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[i].ev > datalist[max].ev:
                max = i
        print(datalist[max].ev)

        kod: str = input()

olvasas()