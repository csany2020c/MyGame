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
        return "Ev = {x}; Nev = {y}; SzuletesHalalozas = {txt}; Sz = {sz} H = {h}  Orszagkod = {col}".format(x=self.Ev, y=self.Nev, txt=self.SzuletesHalalozas, col = self.Orszagkod, sz= self.Szuletes, h= self.Halalozas)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", encoding="utf8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        dijazottak: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            dijazottak.append(d)
        f.close()


        print("3. feladat")
        print("Díjazottak száma: {db} fő ".format(db=len(dijazottak)))


        max: int = 0

        for i in range(1, len(dijazottak)):

            if dijazottak[i].Ev > dijazottak[max].Ev:
                max = i

        print(dijazottak[max].Ev)


        kod: str = input()

        db: int = 0

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

        orszagok: dict = dict()
        for k in range(0, len(dijazottak)):
            try:
                orszagok[dijazottak[k].Orszagkod]+=1
            except:
                orszagok[dijazottak[k].Orszagkod]=1

        for k, v in orszagok.items():
            if v > 5:
                print("{k} {v}".format(k=k, v=v))

        db80: int = 0
        for it in dijazottak:
            if it.Ev >= 1980 and it.Ev <= 1989:
                print(it.Nev)
                db80 += 1
        print("Az 1980-as években {db80} díjazott volt.".format(db80 = db80))


        for it in dijazottak:
            if it.Ev <= 1969 and it.Orszagkod == str("USA") or it.Ev >= 1960 and it.Orszagkod == str("S"):
                print(it.Nev)


Main()









