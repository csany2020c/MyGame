from typing import List
from typing import TextIO

class data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.nev: str = fields[0].strip()
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.tavszazalek: int = int(fields[4])

    def __str__(self) -> str:
        return "Name = {x}; Startnumber = {y}; Category = {txt}; Time = {col}; Percentage = {z}".format(x=self.nev, y=self.rajtszam, txt=self.kategoria, col=self.ido, z=self.tavszazalek)

class olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['data'] = list()
        for i in range(1, len(lines)):
            d = data(lines[i])
            datalist.append(d)
        #for d in datalist:
        #   print(d)

        print("3. feladat: Egyéni indulók: {db} fő ".format(db=len(datalist)))

        kategória: str = "Noi"
        tav: int = 100
        db: int = 0
        for index in range(0, len(datalist)):
            if datalist[index].kategoria == kategória and datalist[index].tavszazalek == tav:
                db += 1
        print("4. feladat: Célba érkező női sportolók: {db} fő ".format(db=db))

        print("5. feladat: Kérem a sportoló nevét: ")
        név: str = input().strip()
        szemely: int = -1
        # táv: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].nev == név:
                szemely = index
                print(datalist[index].nev)
        print(szemely)

        if szemely == -1:
            print("Indult egyéniben a sportoló? Nem")
        else:
            print("Indult egyéniben a sportoló? Igen")
            print(int(datalist[szemely].tavszazalek))
            if datalist[szemely].tavszazalek == 100:
                print("Teljesítette a teljes távot? Igen")
            else:
                print("Teljesítette a teljes távot? Nem")




olvasas()