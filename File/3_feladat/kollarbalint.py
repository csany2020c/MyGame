import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.elso: str = fields[0]
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]
        self.negyedik: str = fields[3]
        self.otodik: str = fields[4]

    def __str__(self) -> str:
        return "a = {a}; b = {b}; c = {c}; d = {d}; e = {e}".format(a=self.elso, b=self.masodik, c=self.harmadik, d=self.negyedik, e=self.otodik)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("")
        print("Adatok:")
        f: TextIO = open("!_Specifikacio//ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 0):
            d = Data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()
        #3.Feladat
        print("")
        print("3.Feladat:")
        print("Egyéni indulók: {szam} fő ".format(szam=len(datalist)))

        #4.Feladat
        #print("")
        #print("4.Feladat:")
        #fo = 0
        #for i in range(0, len(datalist)):
            #if datalist[i].harmadik -= "Ferfi":
                #fo = i
        #print("3.Egyéni indulók: {fo} fő ".format(fo=len(datalist)))

        #5.Feladat
        #print("")
        #print("5.Feladat:")

Main()