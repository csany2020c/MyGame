from typing import TextIO, List

class Gyakorlas:
    def __init__(self) -> None:
        super().__init__()
        self.osszpenz:int = 0
        self.ismertlegnagyobb:int = 0
        self.legnagyobbindex:int = 0
        f:TextIO = open("toto.txt","r")
        file:str = f.read()
        self.lines:List['str'] = file.split("\n")
        print("3. feladat:\n")
        self.fordulomennyiseg:int = 0
        self.telitali = 0

        for a in range(len(self.lines)-1):
            self.toto(self.lines[a])
        print(self.fordulomennyiseg)

        print("4.feladat\n")
        print(self.telitali)

        print("5.feladat\n")
        print(str(self.osszpenz) + "ft")

        print("7.feladat\n")

        for a in range(len(self.lines)-1):
            self.legnagyobb(self.lines[a],a)

    def toto(self,lines:str):
        line = lines.split(" ")
        self.ev = int(line[0])
        self.het = int(line[1])
        self.fordulo = int(line[2])
        self.t13p1 = int(line[3])
        self.ny13p1 = int(line[4])
        self.eredmeny = str(line[5])

        self.fordulomennyiseg+=self.fordulo
        self.telitali+=self.t13p1
        self.penz(self.t13p1 * self.ny13p1)

    def penz(self,penz:int):
        self.osszpenz+=penz

    def legnagyobb(self,sor:str,index:int):
        ev = sor[0]
        het = sor[1]
        penz = int(sor[4])

        if penz > self.ismertlegnagyobb:
            self.ismertlegnagyobb = penz
            self.legnagyobbindex = index


Gyakorlas()