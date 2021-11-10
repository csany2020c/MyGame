import string
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        #fields: List['str'] = parseString.split(";")
        self.text: str = ""


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/dalok.txt")
        content: str = f.read()
        #print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        #print("Split content")
        #print(lines)
        #print("Load to List")
        datalist: List['Data'] = list()

        for str in lines:
            d = Data(str)
            datalist.append(d)
        #("Print list")
        #for d in datalist:
        #print(d)

        f.close()


Main()
