from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = (fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: str = fields[4]

    def __str__(self) -> str:
        return "{v}, {r}, {k}, {vi}, {t}".format(v=self.versenyzo, r=self.rajtszam, k=self.kategoria, vi=self.versenyido, t=self.tavszazalek)

class bajvanhelp:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        # print(content)
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()

        print("Egyeniek: {db}".format(db=len(datalist)))

        nok: str = "Noi"
        no: int = 0
        tavolsag: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].tavszazalek == tavolsag and datalist[index].kategoria == nok:
                no += 1
        print("Noi sportolok: {db}".format(db=no))

bajvanhelp()