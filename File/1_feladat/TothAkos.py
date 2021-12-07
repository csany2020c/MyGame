import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.Ev: int = int(fields[0])
        self.Nev: str = fields[1]
        self.Halalozas: int = None
        self.SzuletesHalalozas: str = fields[2]
        szh: List['str'] = self.SzuletesHalalozas.split("-")
        self.Szuletes: int = int(szh[0])
        if szh[1] != "":
            self.Halalozas = int(szh[1])
        self.Orszagkod: str = fields[3]

    def __str__(self) -> str:
        return "Ev = {x}; Nev = {y}; SzuletesHalalozas = {txt}; Orszagkod = {col}".format(x=self.Ev, y=self.Nev, txt=self.SzuletesHalalozas, col = self.Orszagkod)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        dijazottak: List['Data'] = list()
        for i in range(2, len(lines) - 2):
            dijazottak.append(Data(lines[i]))
        f.close()

        print("5.feladat")
        db: int = 0
        kod: str = input()
        max: int = 1979
        min: int = 1970

        for i in range(1, len(dijazottak)):
            if dijazottak[i].Ev > dijazottak[min].Ev:
                min = i

        for i in range(1,len(dijazottak)):
            if dijazottak[i].Ev < dijazottak[max].Ev:
                max = i

        if db == i:
            print("{db}".format(db=len(dijazottak)))





Main()