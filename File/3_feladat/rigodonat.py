#1.&2.feladat
import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = str(fields[0])
        self.rajtszam: str = str(fields[1])
        self.kategoria: str = str(fields[2])
        self.versenyido: str = str(fields[3])
        self.tavszazalek: str = str(fields[4])

    def __str__(self) -> str:
        return "versenyzo = {x}; rajtszam = {y}; kategoria = {k}; versenyido = {v}; tavszazalek = {t}".format(x=self.versenyzo, y=self.rajtszam, k=self.kategoria, v=self.versenyido, t=self.tavszazalek)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        line: List['str'] = content.split(sep="\n")
        dataList: List['Data'] = list()
        for i in range(1, len(line)-1):
            d = Data(line[i])
            dataList.append(d)
        f.close()

        #3.feladat
        print("{db} egyéni sportoló indult el a versenyen. ".format(db=len(dataList)))


Main()