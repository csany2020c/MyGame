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
        # print(len(szh))
        if szh[1] != "":
            self.Halalozas = int(szh[1])
        self.Orszagkod: str = fields[3]


    def __str__(self) -> str:
        return "Ev = {x}; Nev = {y}; SzuletesHalalozas = {txt}; Sz = {sz} H = {h}  Orszagkod = {col}".format(x=self.Ev, y=self.Nev, txt=self.SzuletesHalalozas, col = self.Orszagkod, sz= self.Szuletes, h= self.Halalozas)




class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r", encoding= "utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        dijazottak: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            dijazottak.append(Data(lines[i]))

        f.close()
        kod: str = input().upper().strip()
        utolso_megtalalt = Data
        db : int = 0
        for k in range(0, len(dijazottak)):

            if dijazottak[k].Orszagkod == kod:
                db += 1
                utolso_megtalalt = dijazottak[k]
            if dijazottak[k].Ev == 1970:
            and
            if dijazottak[k].Orszagkod == kod:
                print(dijazottak[k])

        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print(utolso_megtalalt)
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))


Main()




