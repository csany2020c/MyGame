from typing import List
from typing import TextIO

class Het:

    def __init__(self, parse: str) -> None:
        super().__init__()
        fields: List['str'] = parse.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return "Év = {x}; Hét = {y}; Forduló = {txt}; T13p1 = {col}; Ny13p1 = {z}; Eredmények = {v}".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.t13p1, z=self.ny13p1, v=self.eredmenyek)

    def kifizetettpenz(self) -> int:
        return self.t13p1 * self.ny13p1

    def dontetlenekszama(self) -> int:
        db : int = 0
        for c in self.eredmenyek:
            if c == "X":
                db+= 1
        return db


class Feladat:

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.hetek: List['Het'] = list()
        f = open(filename, encoding="utf-8", mode="r")
        content: List['str'] = f.read().strip().split(sep="\n")
        for i in content:
            self.hetek.append(Het(i))



    def telitalalatosokszama(self) -> int:
        osszeg: int = 0
        for i in self.hetek:
            osszeg += i.t13p1
        return osszeg

    def feladat3(self):
        print("3. feladat:")
        print("Forsulók száma: " + str(len(self.hetek)))

    def feladat4(self):
        print("4. feladat:")
        print("Telitalálatosok száma: " + str(self.telitalalatosokszama()))

    def minegytelitalalatos(self) -> Het:
        min: Het = None
        for i in range(0, len(self.hetek)):
            if self.hetek[i].ny13p1 != 0:
                if min == None:
                    min = self.hetek[i]
                else:
                    if min.ny13p1 > self.hetek[i].ny13p1:
                        min = self.hetek[i]
        return min

    def maxegytelitalalatos(self) -> Het:
        max: Het = self.hetek[0]
        for i in range(1, len(self.hetek)):
            if max.ny13p1 < self.hetek[i].ny13p1:
                    max = self.hetek[i]
        return max

    def voltevalamikordontetlennelkulifordulo(self)->bool:
        for i in self.hetek:
            if i.dontetlenekszama() == 0:
                return True
        return False


    def feladat5(self):
        print("5. feladat (teszt)")
        print(self.hetek[9].kifizetettpenz())


    def feladat7(self):
        print("7. feladat")
        print("{ev} {het}".format(ev = self.minegytelitalalatos().ev, het = self.minegytelitalalatos().het))
        print("{ev} {het}".format(ev = self.maxegytelitalalatos().ev, het = self.maxegytelitalalatos().het))

    def feladat8(self):
        print("8. feladat (teszt)")
        print(self.hetek[0].dontetlenekszama())

    def feladat9(self):
        if self.voltevalamikordontetlennelkulifordulo():
            print("Volt olyan forduló, amikor nem volt döntetlen.")
        else:
            print("Nem volt olyan forduló, amikor nem volt döntetlen.")

f: Feladat = Feladat("toto.txt")
f.feladat3()
f.feladat4()
f.feladat7()
f.feladat9()
