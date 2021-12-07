import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szuleteshalalozas: str = fields[2]
        self.orszag: str = fields[3]

    def __str__(self) -> str:
        return "{x}; {y}; {txt}; {col}".format(x=self.ev, y=self.nev, txt=self.szuleteshalalozas, col=self.orszag)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        for d in datalist:
            print(d)
        f.close()
        print("3. feladat")
        print("Dijazottak száma: {db} fő".format(db=len(datalist)))
        max: int = 0;
        for i in range(1, len(datalist)):
            if datalist[i].ev > datalist[max].ev:
                max = i
        print(datalist[max].ev)
        print("5. feladat")
        kod: str = input()
        #for it in datalist:
            #print(it)
        db:int = 0
        for index in range(len(0, datalist)):
            if datalist[index].orszag == kod:
                db += 1
                utolso = index
        print(db)
        if db == 0:
            print("A megadott országból nem volt díjazott")
        elif db == 1:
            print(datalist[utolso])
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))
Main()