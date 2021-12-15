from typing import TextIO
from typing import List

class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        field: List['str'] = parsestring.split(" ")
        self.helyezes: int = int(field[0])
        self.sportszam: int = int(field[1])
        self.sportag: str = str(field[2])
        self.versenyszam: str = str(field[3])

    def __int__(self) -> str:
        return "Helyezés = {x}; Sportolók száma = {y}; Sportág = {z}; Versenyszám = {v}".format(x=self.helyezes, y=self.sportszam, z=self.sportag, v=self.versenyszam)


class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specs/helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        f.close()
        print("3. feladat")
        print("Pontszerző helyezések száma: " + str(len(lines)))

        gold = 0
        silver = 0
        bronze = 0
        alls = 0

        for i in range(0, len(lines)):
            if datalist[i].helyezes == 1:
                gold = gold + 1
                alls = alls + 1

            if datalist[i].helyezes == 2:
                silver = silver + 1
                alls = alls + 1

            if datalist[i].helyezes == 3:
                bronze = bronze + 1
                alls = alls + 1

        print("Arany: " + str(gold))
        print("Ezüst: " + str(silver))
        print("Bronz: " + str(bronze))
        print("Összesen: " + str(alls))


        print("5. feladat")




Main()