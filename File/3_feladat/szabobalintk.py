from typing import TextIO
from typing import List


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = fields[0]
        self.rajtsz: str = fields[1]
        self.kateg: str = fields[2]
        self.versido: str = fields[3]
        self.tavsz: str = fields[4]

    def __str__(self) -> str:
        return "versenyzo = {v}; rajtsz = {r}; kateg = {k}; versido = {vi}; tavsz = {t}".format(v=self.versenyzo, r=self.rajtsz, k=self.kateg, vi=self.versido, t=self.tavsz)

class Nemertemafeladatot:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 0):
            d = Data(lines[i])
            datalist.append(d)

        f.close()

        print("|3: Induló sportolók száma: {db}| ".format(db=len(datalist)))

        women: str = "Noi"
        woman: int = 0
        tav: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].tavsz == tav and datalist[index].kateg == women:
                woman += 1

        print("|4: Célba ért női sportolók: {db}| ".format(db=woman))

        nevek = input("|5: Az induló neve : ")
        volt: str = "Nem"
        teljesitette: str = "Nem"
        for x in range(1, len(datalist)):

            if datalist[x].versenyzo == nevek:
                volt = "Igen"

            if datalist[x].tavsz == "100" and datalist[x].versenyzo == nevek:
                teljesitette = "Igen"

        print("|5.1:Egyéniben indult? {volt}|".format(volt=volt))
        print("|5.2:Teljesítette a távot? {teljesitette}|".format(teljesitette=teljesitette))


Nemertemafeladatot()