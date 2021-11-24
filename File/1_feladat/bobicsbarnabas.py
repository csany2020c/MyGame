import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.text: str = ""
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szuleteshalalozas: str = fields[2]
        self.orszagkod: str = fields[3]
        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

    def __str__(self) -> str:
        return "Ev = {x}; Nev = {y}; Szuletes-Halalozas = {txt}; Orszagkod = {col}".format(x=self.ev, y=self.nev, txt=self.szuleteshalalozas, col = self.orszagkod)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
       # print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        #print("Split content")
        print(lines)
        #print("Load to List")
        dijazottak: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            dijazottak.append(d)
        #print("Print list")
        for d in dijazottak:
            print(d)


        kod: str = input()


Main()
