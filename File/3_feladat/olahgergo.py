from typing import TextIO
from typing import List

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = str(fields[0])
        self.szam: str = fields[1]
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tav: str = fields[4]

    def __str__(self) -> str:
        return "Versenyző = {v}; Rajtszám = {r}; Kategória: {k}; Időeredmény: {i}; Táv százalék: {t}".format(v=self.versenyzo, r=self.szam, k=self.kategoria, i=self.ido, t=self.tav)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        print("3. feladat: Egyémni indulók: {db} fő".format(db=len(datalist)))

        # db: int = 0
        # for i in range(1, len(datalist)):
        #     if datalist[i].kategoria == db:
        #         db += 1
        # print("4. feladat: Célba érkező npi sportolók: {db} fő".format(db=len(datalist)))

Main()