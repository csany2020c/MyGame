from typing import TextIO, List

class Gyakorlas:
    def __init__(self) -> None:
        super().__init__()
        self.osszpenz:int = 0
        self.ismertnagyobb:int = 0
        self.nagyobbindex:int = 0
        f:TextIO = open("toto.txt","r")
        file:str = f.read()
        self.lines:List['str'] = file.split("\n")
        print("3. feladat:\n")
        self.fordulomennyiseg:int = 0
        self.talalat = 0

        for a in range(len(self.lines)-1):
            self.toto(self.lines[a])
        print(self.fordulomennyiseg)

        print("4.feladat\n")
        print(self.talalat)

        print("5.feladat\n")
        print(str(self.osszpenz) + "ft")

        print("7.feladat\n")

        for a in range(len(self.lines)-1):
            self.legnagyobb(self.lines[a],a)

    def penz(self,penz:int):
        self.osszpenz+=penz

    def nagyobb(self,sor:str,index:int):
        ev = sor[0]
        het = sor[1]
        penz = int(sor[4])

        if penz > self.ismertlegnagyobb:
            self.ismertnagyobb = penz
            self.nagyobbindex = index


Gyakorlas()