import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)

        fields: List['str'] = parseString.split(";")
        self.year: int = int(fields[0])
        self.name: str = str(fields[1])
        self.born: str = str(fields[2])
        self.country: str = str(fields[3])

        for i in range(5, len(
                fields)):
            self.text += str(fields[i])

    def __str__(self) -> str:
        return "Year = {x}; Name = {y}; Born-Die = {txt}; Country = {col}".format(x=self.year, y=self.name, txt=self.born, col=self.country)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r", encoding="utf-8")
        content: str = f.read()
        f.close()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)-1):
            d = Data(lines[i])
            datalist.append(d)
        print("Print list")
        for d in datalist:
            print(d)
        f.close()


Main()