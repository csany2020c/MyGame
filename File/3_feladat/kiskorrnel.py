from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.Versenyzo: str = str(fields[0])
        self.Rajtszam: str = fields[1]
        self.Kategoria: str = fields[2]
        self.Versenyido: str = fields[3]
        self.TavSzazalek: str = fields[4]

    def __str__(self) -> str:
        return "{x};     {y};    {a};  {b};  {c}".format(x=self.Versenyzo, y=self.Rajtszam, a=self.Kategoria, b=self.Versenyido, c=self.TavSzazalek)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()
        db: int = len(datalist)
        print("Egyéni indulók: {db}".format(db=db))

        valami: str = input()
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].Versenyzo == valami:
                db += 1
        if db == 0:
            print("Nem indult egyéniben")
        else:
            print("Indult egyéniben")
Main()