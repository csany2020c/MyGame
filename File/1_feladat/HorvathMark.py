from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.text: int = int(fields[0])

    def __str__(self) -> str:
        return "text = {txt}".format(txt = self.text)

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