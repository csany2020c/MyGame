import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.év: int = int(fields[0])
        self.név: str = fields[1]
        self.születés: str = fields[2]
        self.országkód: str = fields[3]

    def __str__(self) -> str:
        return "{x}; {y}; {txt}; {col}".format(x=self.év, y=self.név, txt=self.születés, col=self.országkód)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", encoding="utf-8")
        content: str = f.read()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        i: int = 0
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()

        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].év >= 1980 and datalist[index].év <= 1989:
                db += 1
                print(datalist[index].év, datalist[index].név)
        print(db)

Main()
