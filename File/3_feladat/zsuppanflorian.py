from typing import List
from typing import TextIO

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.nev: str = fields[0]
        self.rszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tavszaz: int = int(fields[4])

    def __str__(self) -> str:
        return "Név = {x}; Rajtszám = {y}; Kategória = {txt}; Idő = {col}; Távszázalék = {z}".format(x=self.nev, y=self.rszam, txt=self.kategoria, col=self.ido, z=self.tavszaz)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
            f.close()


#3.feladat
        print("Egyéni indulók száma: {db} fő".format(db=len(datalist)))

#4.feladat
        #r = 0
        #for index in range(0, len(datalist)):
          #  if datalist[index].kategoria == "Noi":
         #       r = r + 1
        #print(f"Női versenyzők száma : {r} fő")

        db: int = 0
        Noiversenyzok: Data
        for i in range(0, len(datalist)):
            if datalist[i].kategoria == "Noi":
                db = db + 1
        print("Női versenyzők száma : {db} fő".format(db=db))

#5.feladat




Main()