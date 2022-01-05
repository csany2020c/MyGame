
from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.hely: int = int (fields[0])
        self.pont: int = int (fields[1])
        self.kati: str = str (fields[2])
        self.szam: str = str (fields[3])


    def __str__(self) -> str:
        return "{x}    {y}     {txt}     {col}".format(x=self.hely, y=self.pont, txt=self.kati, col=self.szam)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("2.feladat")
        f: TextIO = open("!_Specs//helsinki.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(0, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
            print(d)

        f.close()

        print("3.feladat")
        print("Pontszerző helyezések száma: {db} fő".format(db=len(datalist)))
        print(datalist[len(datalist)-1].pont)
        max: int = 0
        for i in range(1, len(datalist)):
            if datalist [max].hely < datalist[i].hely:
                max = i

        helyp: int = int(input())

        print(datalist[max].hely)
        print("4.feladat")
        print("Arany: {db}".format(db=len(datalist)))

        db: int =0
        for index in range(0, len(datalist)):
            if datalist[index].hely == helyp:
                db +=1

        if db ==1:
            print("Arany:{db}")

        else :
            print("Ezüst: {db}")

Main()