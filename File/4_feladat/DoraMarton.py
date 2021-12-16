import string
from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.sportolok: int = int(fields[1])
        self.sport: str = fields[2]
        self.versenyszam: str = fields[3]

    def __str__(self) -> str:
        return "{h}; {s}; {s2}; {v}".format(h=self.helyezes, s=self.sportolok, s2=self.sport, v=self.versenyszam)

class sziahogyvagy:
    def __init__(self):
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        f.close()

        ermesek = 0

        for index in range(0, len(lines)):
            if datalist[index].helyezes == 1:
                ermesek = ermesek + 1
            if datalist[index].helyezes == 2:
                ermesek = ermesek + 1
            if datalist[index].helyezes == 3:
                ermesek = ermesek + 1
        print("Pontszerző helyezések:" + str(ermesek))

        elso = 0
        masodik = 0
        harmadik = 0
        negyedik = 0
        otodik = 0
        hatodik = 0
        pontok = 0

        for index in range(0, len(lines)):
            if datalist[index].helyezes == 1:
                elso = elso + 1
                pontok = pontok + 7
            if datalist[index].helyezes == 2:
                masodik = masodik + 1
                pontok = pontok + 5
            if datalist[index].helyezes == 3:
                harmadik = harmadik + 1
                pontok = pontok + 4
            if datalist[index].helyezes == 4:
                negyedik = negyedik + 1
                pontok = pontok + 3
            if datalist[index].helyezes == 5:
                otodik = otodik + 1
                pontok = pontok + 2
            if datalist[index].helyezes == 6:
                hatodik = hatodik + 1
                pontok = pontok + 1

        print("Arany:" + str(elso))
        print("Ezüst:" + str(masodik))
        print("Bronz:" + str(harmadik))
        print("Összesen:" + str(pontok))


sziahogyvagy()