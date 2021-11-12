from typing import TextIO
from typing import List

class lista:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("\t")
        self.ev: int = int(fields[0])
        self.helyezes: int = int(fields[1])
        self.dalid: int = int(fields[2])

    def __str__(self) -> str:
        return "Ev = {x};Place = {y};ZeneID = {txt}".format(x=self.ev, y=self.nev, txt=self.helyezes, col = self.dalid)

class eloado:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        field: List['str'] = parseString.split(" ")
        self.eloadoid: int(field[0])
        self.nev: str = field[1]
        self.zenekar: str = field[2]

class dal:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split("   ")
        self.dalid: int = int(fields[0])
        self.eloadoid: int = int(fields[1])
        self.cim: int = int(fields[2])
        self.megjelenes: int = int(fields[3])


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/lista.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['lista'] = list()
        for i in range(1, len(lines) - 1):
            l = lista(lines[i])
            datalist.append(l)

        for d in datalist:
            print(d)

        f.close()

Main()
