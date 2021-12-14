from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.nev: str = (fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.ido: str = fields[3]
        self.szazalek: int = int(fields[4])

    def IdoOra(self) -> float:
        s: List['str'] = self.ido.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0

    def __str__(self) -> str:
        return "{n}; {r}; {k}; {i}; {s}".format(n=self.nev, r=self.rajtszam, k=self.kategoria, i=self.ido, s=self.szazalek)


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        f.close()

# 3. feladat

        db: int = len(datalist)
        print("3. feladat: Egyéni indulók: {db} fő".format(db=db))

# 4. feladat

        fo: int = 0
        for i in range(0, len(datalist)):
            if datalist[i].kategoria == "Noi" and datalist[i].szazalek == 100:
                fo += 1
        print("4. Célba érkező női sportolók: {fo} fő ".format(fo=fo))


#5.feladat

        print("5. feladat: Kérem a sportoló nevét:")
        sportolo: str = input().strip()
        szemely: int = -1

        for index in range(0, len(datalist)):
            if datalist[index].nev == sportolo:
                szemely = index
                print(datalist[index].nev)
        print(szemely)

        if szemely == -1:
            print("Indult egyéniben a sportoló? Nem")

        else:
            print("Indult egyéniben a sportoló? Igen")
            print(int(datalist[szemely].szazalek))

            if datalist[szemely].szazalek == 100:
                print("Teljesítette a teljes távot? Igen")
            else:
                print("Teljesítette a teljes távot? Nem")

        osszeg: float = 0
        db: int = 0
        for i in datalist:
            if i.kategoria == "Ferfi" and i.szazalek == 100:
                db += 1
                osszeg += i.IdoOra()
        print("Átlag {atl}".format(atl = osszeg / db))

        # noiMinIndex: int = 0
        # ferfiMinIndex: int = 0
        
        befutottNok: List['Data'] = list()
        befutottFerfiak: List['Data'] = list()

        for i in datalist:
            if i.kategoria == "Ferfi" and i.szazalek == 100:
                befutottFerfiak.append(i)
            if i.kategoria == "Noi" and i.szazalek == 100:
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




Main()
