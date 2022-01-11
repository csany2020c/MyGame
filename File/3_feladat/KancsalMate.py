import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.nev: str = str(fields[0])
        self.szam: str = fields[1]
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tav: str = fields[4]

    def __str__(self) -> str:
        return "Versenyzo = {x}; Rajtszam = {y}; Kategoria = {c};Versenyido = {v}; Tav = {v}".format(
            x=self.nev, y=self.szam, c=self.kategoria, v=self.ido, b=self.tav)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)-1):
            d = Data(lines[i])
            datalist.append(d)
        f.close()
        print("Egyéni indulók: {db} fő ".format(db=len(datalist)))
        x = 0
        for index in range(0, len(datalist)):
            if datalist[index].kategoria  == "Noi" and datalist[index].tav == "100":
                x = x + 1
        print(f"Női versenyzők száma : {x}")

        adat: str = input()
        for index in range(0, len(datalist)):
            if datalist[index].nev == adat:
                print("Indult a versenyen")

Main()