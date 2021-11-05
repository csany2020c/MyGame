from typing import IO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        self.text: str = ""

    def __str__(self) -> str:
        return "text = {txt}".format(txt = self.text)

class olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print(lines)
        datalist: List['Data'] = list()
        for str in lines:
            d = Data(str)
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()

olvasas()