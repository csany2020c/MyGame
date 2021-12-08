import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        self.Ev: int = int(fields[0])
        self.Nev: str = fields[1]
        self.Halalozas: int = None
        self.SzuletesHalalozas: str = fields[2]
        szh: List['str'] = self.SzuletesHalalozas.split("-")
        self.Szuletes: int = int(szh[0])
        #print(len(szh))
        if szh[1] != "":
            self.Halalozas = int(szh[1])
        self.Orszagkod: str = fields[3]
        #print(self)

    def __str__(self) -> str:
        return "Ev = {x}; Nev = {y}; SzuletesHalalozas = {txt}; Sz = {sz} H = {h}  Orszagkod = {col}".format(x=self.Ev, y=self.Nev, txt=self.SzuletesHalalozas, col = self.Orszagkod, sz= self.Szuletes, h= self.Halalozas)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", encoding="utf8")
        content: str = f.read()
        #print("Content:")
        #print(content)
        lines: List['str'] = content.split(sep="\n")
        dijazottak: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            dijazottak.append(Data(lines[i]))
        f.close()

        max: int = 0

        for i in range(1, len(dijazottak)):
            if dijazottak[i].Ev > dijazottak[max].Ev:
                max = i

        print(dijazottak[max].Ev)

        kod: str = input().upper().strip()

        print(5.1 feladat:)

        db: int = 0
        utolso_megtalalt:Data

        for k in range(0, len(dijazottak)):
            if dijazottak[k].Orszagkod == kod:
                db += 1
                utolso_megtalalt = dijazottak[k]

        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print(utolso_megtalalt)
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db = db))


        for it in dijazottak:
            if it.Ev <= 1970:
                print(it)


        # iterátoros végigjárás
        # for it in dijazottak:
        #     print(it)

        # index alapú végigjárás
        #for index in range(0, len(dijazottak)):
            #print(str(index) + " ---- " + str(dijazottak[index]))

Main()