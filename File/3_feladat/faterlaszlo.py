import string
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = fields[0]
        self.rajtszam: int = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tav: int = fields[4]

    def __str__(self) -> str:
        return "Versenyzo = {x}; Rajtszam = {y}; Kategotia = {txt};Versenyido = {col}; Tav = {st}".format(
            x=self.versenyzo, y=self.rajtszam, txt=self.kategoria, col=self.versenyido, st=self.tav)


class Read:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()

        print("3. feladat: Egyéni indulok: {db} fő".format(db=len(datalist)))

        Noi: str = "Noi"
        szam: int = 0
        tav: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].tav == tav and datalist[index].kategoria == Noi:
                szam += 1
        print("4. feladat: Célba érkező női sportolók: {db} fő".format(db=szam))

        name: str = input()
        ember: int = 0
        for index in range(0, len(lines) - 1):
            if datalist[index].versenyzo == name:
                ember += 1
                print("5. feladat: Kérem a sportoló nevét: {v}".format(v=name))
        if ember == 0:
            print("Indult egyéniben a sportoló? Nem")
        else:
            print("Indult egyéniben a sportoló? Igen")

        if datalist[index].tav == 100:
            print("Teljesítette a teljes távot? Igen")
        # if datalist[index].tav < 0 and datalist[index].tav < 100:
        else:
            print("Teljesítette a teljes távot? Nem")


Read()