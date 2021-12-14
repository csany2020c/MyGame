import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = fields[0]
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tav: int = int(fields[4])
        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

    def __str__(self) -> str:
        return "versenyzo = {versenyzo}; rajtszam = {rajtszam}; kategoria = {kategoria}; ido = {ido}; tav = {tav}".format(versenyzo=self.versenyzo, rajtszam=self.rajtszam, kategoria=self.kategoria, ido=self.ido, tav=self.tav)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)

Main()
