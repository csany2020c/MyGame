import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        print(fields)



class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()

        lines: List['str'] = content.split(sep="\n")

        datalist: List['Data'] = list()
        for str in lines:
                d = Data(str)
                datalist.append(d)


        f.close()


Main()