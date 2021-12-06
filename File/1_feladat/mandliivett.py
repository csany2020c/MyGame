import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")

        self.text: int = int(fields[0])
        self.nev: str = fields[1]
        self.szh: str = fields[2]
        self.orszag: str = fields[3]

    def __str__(self) -> str:
        return "Year = {x}; Name = {y}; Born-death = {txt}; Country = {col}".format(x=self.text, y=self.nev, txt=self.szh, col=self.orszag)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        dijazottak: List['str'] = content.split(sep="\n")
        datalist: List['data'] = list()

        for i in range(1, len(dijazottak) - 1):
            d = Data(dijazottak[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()


        print("3. feladat")
        print("Díjazottak száma: {db} fő ".format(db=len(dijazottak)))

        max: int = 0
        for i in range(1, len(dijazottak)):
            if dijazottak[i].Ev > dijazottak[max].Ev:
                max = i
        print(dijazottak[max].Ev)

        kod: str = input()

        print("A megadott országból nem volt dijazott!")


Main()
