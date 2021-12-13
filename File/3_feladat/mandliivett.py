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
        self.szazalek: str = fields[4]

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

        # db: int = 0
        # for i in range(0, len(datalist)):
        #    if datalist[i].kategoria == "Noi":
        #        db += 1
        # print("4. feladat: Célba érkező női sportolók: {db} fő")

#5.feladat

        print("5. feladat: Kérem a sportoló nevét:")
        sportolo: str = input()
        for index in range(0, len(datalist)):
            if datalist[index].nev == sportolo:
                print("Indult egyéniben a sportoló? : Igen.")




Main()
