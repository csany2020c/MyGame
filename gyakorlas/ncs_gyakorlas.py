from typing import TextIO
from typing import List


class Szamok:

    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.Ev: int = int(fields[0])
        self.Het: int = int(fields[1])
        self.Fordulo: int = int(fields[2])
        self.T13p1: int = int(fields[3])
        self.Ny13p1: int = int(fields[4])
        self.Eredmenyek: str = str(fields[5])

    def __str__(self) -> str:
        return "Ev = {x}; Het = {y}; Fordulo = {txt}; T13p1 = {sz}; Ny13p1 = {h};  Eredmenyek = {col}".format(x=self.Ev, y=self.Het, txt=self.Fordulo, col=self.Eredmenyek, sz=self.T13p1, h=self.Ny13p1)


class Feladat:
    def __init__(self) -> None:
        super().__init__()
        read: List['str'] = open("toto.txt",).read().strip().split(sep="\n")
        toto: List[Szamok] = list()
        for i in range(1, len(read)):
            toto.append(Szamok(read[i]))

        print("3. feladat")
        a = 0
        for i in range(0, len(toto)):
            a += toto[i].Fordulo
        print(a)

        print("4. feladat")
        b = 0
        for i in range(0, len(toto)):
            b += toto[i].T13p1
        print(b)

        print("5. feladat")

        print("7. feladat")
        c = 0
        for i in range(0, len(toto)):
            if c < toto[i].Ny13p1:
                c = toto[i].Ny13p1
            if c == toto[i].Ny13p1:
                print("Legnagyobb = ", toto[i].Ev, toto[i].Het)
        d = 0
        for i in range(0, len(toto)):
            if d > toto[i].Ny13p1:
                d = toto[i].Ny13p1
            if d == toto[i].Ny13p1:
                print("Legkisebb = ", toto[i].Ev, toto[i].Het)

        print("8. feladat")
        e = 0
        for i in range(0, len(toto)):
            for i in str(toto[i].Eredmenyek):
                if i == "X":
                    e += 1
        print(e)

        print("9. feladat")
        f = 0
        for i in range(0, len(toto)):
            for i in str(toto[i].Eredmenyek):
                if str(i) == "X":
                    f += 1
                    if f == 1:
                        print("Van döntetlen!")
                        break


Feladat()
