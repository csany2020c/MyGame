from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(" ")
        self.text: str = ""
        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

    def __str__(self) -> str:
        return "Ev = {x};Nev = {y};Szuleteshalal = {txt};Orszag = {col}".format(x=self.text, y=self.text, txt=self.text, col=self.text)


class olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print(lines)
        datalist: List['data'] = list()
        for str in lines:
            d = data(str)
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()

olvasas()