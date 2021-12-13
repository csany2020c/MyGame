from typing import TextIO
from typing import List

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.nev: str = str(fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tavszazalek: int = int(fields[4])

    def __str__(self) -> str:
        return "Versenyző = {x}; Rajtszám = {y}; Kategória = {txt}; Idő = {col}; Távszázalék = {tav}".format(x=self.nev, y=self.rajtszam, txt=self.kategoria, col=self.ido, tav=self.tavszazalek)

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
            #print(d)
        f.close()

        #print("3.feladat:")
        #db: int = len(datalist)
        #print("Egyéni indulók száma: {db} fő.".format(db=db))

        print("4.feladat:")
        kategória: int = "Noi"
        tav: int = 100
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].kategoria == kategória and datalist[index].tavszazalek == tav:
                db += 1
        print("A célba érkező női sportolók száma: {db} fő ".format(db=db))

        # print("5.feladat:")
        # név: str = input()
        # ember: int = 0
        # for index in range(0, len(datalist)):
        #     if datalist[index].nev == név:
        #         ember += 1
        # if ember == 0:
        #     print("Nem indult egyéniben a sportoló!")
        # else:
        #     print("Indult egyéniben a sportoló.")
        #
        # if datalist[index].tavszazalek == 100:
        #     print("Teljesítette a teljes távot.")
        # else:
        #     print("Nem teljesítette a teljes távot.")

Main()