from typing import TextIO
from typing import List

class Adat:
    def __init__(self, parseString: str) -> None:
        super().__init__()

        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.sportolokszama_csp: int = int(fields[1])
        self.sport:str = str(fields[2])
        self.versenyszam: str = (fields[3])

    def __str__(self) -> str:
        return "helyezes = {a}; sportolokszama_csp = {b}; sport = {c}; versenyszam = {d}".format(a= self.helyezes, b=self.sportolokszama_csp, c=self.sport, d=self.versenyszam)


class Main:
    def __int__(self):
        f: TextIO = open("!_Specs/helsinki.txt", "r")
        content: str = f.read()
        sorok: List['str'] = content.split(sep="\n")
        adatlist: List['Adat'] = list()
        for i in range(0, len(sorok)):
            d = Adat(sorok[i])
            adatlist.append(d)
        f.close()

        print("3.feladat:--> " + "pontszerző heléyezések száma:" + str(len(sorok)))

Main()