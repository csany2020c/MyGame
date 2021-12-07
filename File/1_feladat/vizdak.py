import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.elet: str = fields[2]
        self.kod: str = fields[3]

    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col}".format(x=self.ev, y=self.nev, txt=self.elet, col = self.kod)


class Feladat:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec//orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)



        print("...")
        f.close()

        print("3. feladat")
        print("Díjazottak száma: {db} fő ".format(db=len(datalist)))

        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[i].ev > datalist[max].ev:
                max = i
        print(datalist[max].ev)

        #kod: str = input()
        print("5. feladat")
        kod: str = input()

        db: int = 0
        utolso: int = -1
        for index in range(0, len(datalist)):
            if datalist[index].orszagkod == kod:
                db += 1
                utolso = index
        print(db)
        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print(datalist[utolso])
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))


        print("6. feladat")
        kod: str = input()
        max: int = 0
        for i in range(0, len(datalist)):
            if datalist[i].ev > datalist[max].ev:
                max = i
            print(datalist[max].ev)

        if datalist[index].ev >= 1970 and  datalist[index].ev <=1979:

Feladat()