import string
from typing import TextIO
from typing import List

class Eloadok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        #self.text: str = ""
        self.eloado: int = fields[0]
        self.nev: str = fields[1]
        self.zenekar: str = fields[2]

        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "

class Dalok:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        #self.text: str = ""
        self.dalid: int = fields[0]
        self.eloadoid: str = fields[1]
        self.cim: str = fields[2]
        self.megjelenes: str = fields[3]


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/dalok.txt", "r")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        #print("Split content")
        #print(lines)
        #print("Load to List")
        datalist: List['Data'] = list()
        #i: int = 0
        #for i in range(1, len(lines) - 1):
         #   d = Data(lines[i])
          #  datalist.append(d)
        #print("Print list")
        #for d in datalist:
          #  print(d)


Main()