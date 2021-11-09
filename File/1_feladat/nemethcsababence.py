import string
from typing import List
from typing import TextIO

class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split("")
        self.year: int = int(fields[0])
        self.name: str = str(fields[1])
        self.borthdeath: str = str(fields[2])
        self.cCode: str = str(fields[3])
        self.szoveg: str = ""



class Beolv:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        print(content)
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for str in lines:
            d = Adat(str)
            datalist.append(d)
        for d in datalist:
            print(d)

        f.close()

Beolv()

