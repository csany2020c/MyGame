from typing import TextIO
from typing import List


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = str(fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: str = fields[4]

    def __str__(self) -> str:
        return "Versenyző = {x};   Rajtszám = {y};   Kategória = {txt};   Versenyidő = {col}; Távszázalék = {tav}".format(x=self.versenyzo, y=self.rajtszam, txt=self.kategoria, col=self.versenyido, tav=self.tavszazalek)


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
        print("Egyéni indulók száma: {db} fő".format(db=db))

        bevitel: str = input()

        keresett_index: int = -1
        for index in range(0, len(datalist)):
            if datalist[index].versenyzo == bevitel:
                keresett_index = index
                break

        if keresett_index == -1:
            print("Nem indult ilyen nevű versenyző!")
        else:
            print("Ez a nevű versenyző eredménye: {db}.".format(db=datalist[keresett_index].tavszazalek))

        for index in range(0, len(datalist)):
            if datalist[index].tavszazalek == 100:
                print("datalist[index].kategoria")
            else:
                print("")


Main()
