import string
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.eloadoid: int = int(fields[0])
        self.nev: str = str(fields[1])
        self.zenekar: str = str(fields[2])

        for i in range(1, len(fields)):
            self.text += str(fields[i])

    def __str__(self) -> str:
        return "Year = {x}; Name = {y}; Born-Die = {txt}".format(x=self.eloadoid, y=self.nev, txt=self.zenekar)


class songs:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/dalok.txt", "r", encoding="utf-8")
        content: str =f.read()
        print(content)
        f.close()


class eloado:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/eloadok.txt", "r", encoding="utf-8")
        content: str =f.read()
        print(content)
        f.close()


class list:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/lista.txt", "r", encoding="utf-8")
        content: str =f.read()
        print(content)
        f.close()
        #lines: List['str'] = content.split(sep="\n")
        #datalist: List['Data'] = list()
        #for i in range(1, len(lines) - 1):
            #d = Data(lines[i])
            #datalist.append(d)


#eloado()
list()
#songs()