import string
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = str(fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tav: str = fields[4]

    def __str__(self) -> str:
        return "Versenyzo = {x}; Rajtszam = {y}; Kategotia = {txt};VErsenyido = {col}; Tav = {st}".format(x=self.versenyzo, y=self.rajtszam, txt=self.kategoria, col=self.versenyido, st=self.tav)


class Read:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)-1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()

Read()