import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szuleteshalalozas: str = fields[2]
        self.orszag: str = fields[3]

    def __str__(self) -> str:
            return "ev = {x}; nev = {y}; szuleteshalalozas = {txt}; orszag = {col}".format(x=self.ev, y=self.nev, txt=self.szuleteshalalozas, col=self.orszag)

class Main:
        def __init__(self) -> None:
            super().__init__()
            f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
            content: str = f.read()
            f.close()
            print("Content:")
            print(content)
            lines: List['str'] = content.split(sep="\n")
            print("Split content")
            print(lines)
            print("Load to List")
            datalist: List['Data'] = list()
            for i in range(1, len(lines) - 1):
                d = Data(lines[i])
                datalist.append(d)
                print("Print list")
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



            ev: dict = dict()
            for i in range(0, len(datalist)):
                 try:
                     ev[datalist[i].ev]+=1
                 except:
                     ev[datalist[i].ev]=1

            for k, v in ev.items():
                    print("{k} {v}".format(k=k, v=v))

Main()