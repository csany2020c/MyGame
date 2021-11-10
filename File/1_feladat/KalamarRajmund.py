import string
from typing import TextIO
from typing import List

class Data:


    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")


    def __str__(self) -> str:
        return "x = {x}; y = {y}; text = {txt}; color = {col}".format(x=self.x, y=self.y, txt=self.text, col = self.color)




class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r", encoding= "utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        f.close()

Main()




