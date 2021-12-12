from typing import List
from typing import TextIO


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = fields[0]
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: int = int(fields[4])

    def __str__(self) -> str:
        return "versenyzo = {v}; rajtszam = {r}; kategoria = {k}; versenyido = {vi}; tavszazalek = {t}".format(v=self.versenyzo, r=self.rajtszam, k=self.kategoria, vi=self.versenyido, t=self.tavszazalek)


class Read:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
        #3.feladat
        print("3. feladat: Egyéni indulók: {db} fő ".format(db=len(datalist)))

        #4.feladat
        nok: int = 0
        noi: str = "Noi"
        for i in range(1, len(datalist)):
            if datalist[i].kategoria == noi:
                nok += 1
        print("4. feladat: Célba érkező női sportolók száma: {nok} fő".format(nok=nok))

        #5.feladat
        vnev = input("5.feladat: Kérem a sportoló nevét: ")
        van: str = "Nem"
        tav: str = "Nem"
        for x in range(1, len(datalist)):
            if datalist[x].versenyzo == vnev:
                van = "Igen"
            if datalist[x].tavszazalek == 100 and datalist[x].versenyzo == vnev:
                tav = "Igen"
        print("Indult egyéniben a sportoló? {van}".format(van=van))
        print("Teljesítette a teljes távot? {tav}".format(tav=tav))

        # #6.feladat
        # for c in range(1, len(datalist)):
        #     cella: datalist[c].versenyido['str'] = parseString.split(":")
        #     self.ora:int = int(cella[1])
        #     self.perc:int = int(cella[2])
        #     self.masodperc:int = int(cella[3])
        #     print(self.ora)
        #
        # def __str__(self) -> str:
        #     return "ora = {o}; perc = {p}; masodperc = {mp}".format(o=self.ora, p=self.perc, mp=self.masodperc)
        #
        #
        #
        # #7.feladat
        # tferfiak: int = 0
        # ferfi: str = "Ferfi"
        # for z in range(1, len(datalist)):
        #     if datalist[z].kategoria == ferfi and datalist[x].tavszazalek == 100:
        #         tferfiak += 1
        # teljesferfiatlag = tferfiak /
        # print(teljesferfiatlag)

        # #8.feladat
        # minferfi
        # minno

Read()