from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = fields[0]
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.vido: str = fields[3]
        self.tvszaz: int = int(fields[4])

    def __str__(self) -> str:
        return "versenyzo = {v}; rajtszam = {r}; kategoria = {k}; vido = {ve}; tvszaz = {t}".format(v=self.versenyzo, r=self.rajtszam, k=self.kategoria, ve=self.vido, t=self.tvszaz)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)):
            d = Data(lines[i])
            datalist.append(d)

        f.close()

        print(" Egyéni sportolók: {db}| ".format(db=len(datalist)))

        #4feladat
        db: int = 0
        Noiversenyzok: Data
        for i in range(0, len(datalist)):
            if datalist[i].kategoria == "Nok":
                db = db + 1
        print("Női versenyzők : {db} fő".format(db=db))


Main()