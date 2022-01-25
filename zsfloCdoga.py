from typing import List
from typing import TextIO

class Barlang:

    def __init__(self, parse: str):
        cucc: list[str] = parse.strip().split("\t")
        print(cucc)
        self.nev: str = cucc[0]
        self.hossz: int = int(cucc[1])
        self.kiterjedes: int = int(cucc[2])
        self.melyseg: int = int(cucc[3])
        self.magassag: int = int(cucc[4])
        self.telepules: str = cucc[5]


    def __str__(self) -> str:
        return "{nev}\t{hossz}\t{kiterjedes}\t{melyseg}\t{magassag}\t{telepules}".format(nev=self.nev, hossz=self.hossz, kiterjedes = self.kiterjedes, melyseg=self.melyseg, magassag=self.magassag, telepules=self.telepules)

def main():
    adat: list[Barlang] = []
    line: list[str] = open("barlang.txt", mode="r", encoding="windows-1250").read().strip().split("\n")
    for i in range(1, len(line)):
        adat.append(Barlang(adat[i]))

