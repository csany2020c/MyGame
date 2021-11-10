from typing import List
from typing import TextIO
import string

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print(parseString)

        fields: List['str'] = parseString.split(";")

        self.ev: int = int(fields[0])
        self.nev: str = str(fields[1])
        self.szuleteshalalozas: str = str(fields[2])
        self.orszagkod: str = str(fields[3])

        for i in range(5, len(fields)):
            self.orszagkod += str(fields[i])
            if i < len(fields) - 1:
                self.orszagkod += " "

    def __str__(self) -> str:
        return "x = {ev}; y = {nev}; text = {orszagkod}; color = {szuleteshalalozas}".format(x=self.ev, y=self.nev, txt=self.orszagkod, col=self.szuleteshalalozas)


class Olvas:
    f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
    content: str = f.read()
    print("Content:")
    print(content)
    lines: List['str'] = content.split(sep="\n")
    print(lines)

    datalist: List['Data'] = list()
    for s in range(1, len(lines)-1):
        d = Data(lines[s])
        datalist.append(d)
    print("A listamnak a vege, sajnos vege")

    f.close()

Olvas()



