import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.x: int = int(fields[0])
        self.y: int = int(fields[1])
        self.color: int = (int(fields[2]), int(fields[3]), int(fields[4]))
        self.text: str = ""

        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

    def __str__(self) -> str:
        return "x = {x}; y = {y}; text = {txt}; color = {col}".format(x=self.x, y=self.y, txt=self.text, col = self.color)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        f.close()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for s in lines:
            d = Data(s)
            datalist.append(d)
        print("Print list")
        for d in datalist:
            print(d)


Main()
