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

    def IdoOra(self) -> float:
        s: List['str'] = self.ido.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0


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

        print("5. feladat: Kérem a sportoló nevét :")
        név: str = input().strip()
        szemely: int = -1
        # táv: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].nev == név:
                szemely = index

        if szemely == -1:
            print("Indult egyéniben a sportoló? Nem")
        else:
            print("Indult egyéniben a sportoló? Igen")
            print(int(datalist[szemely].tavszazalek))
            if datalist[szemely].tavszazalek == 100:
                print("Teljesítette a teljes távot? Igen")
            else:
                print("Teljesítette a teljes távot? Nem")

        osszeg: float = 0
        db: int = 0
        for i in datalist:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                db += 1
                osszeg += i.IdoOra()
        print("Átlag {atl}".format(atl=osszeg / db))

        # noiMinIndex: int = 0
        # ferfiMinIndex: int = 0
        befutottNok: List['data'] = list()
        befutottFerfiak: List['data'] = list()
        for i in datalist:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                befutottFerfiak.append(i)
            if i.kategoria == "Noi" and i.tavszazalek == 100:
                befutottNok.append(i)

        # for i in befutottNok:
        #     print(i)

        minIndex = 0
        for i in range(1, len(befutottNok)):
            if befutottNok[minIndex].IdoOra() > befutottNok[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottNok[minIndex]))

        minIndex = 0
        for i in range(1, len(befutottFerfiak)):
            if befutottFerfiak[minIndex].IdoOra() > befutottFerfiak[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottFerfiak[minIndex]))

olvasas()