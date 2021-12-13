from typing import TextIO
from typing import List


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.nev: str = str(fields[0])
        self.rajtsz: str = str(fields[1])
        self.kategoria: str = str(fields[2])
        self.ido: str = str(fields[3])
        self.megtetttav: str = str(fields[4])

    def __str__(self) -> str:
        return "nev = {a}; rajtszam = {b}; kategoria = {c}; idoeredmeny = {d}; elertszazalek = {e}".format(a=self.nev,
                                                                                                           b=self.rajtsz,
                                                                                                           c=self.kategoria,
                                                                                                           d=self.ido,
                                                                                                           e=self.megtetttav)


class Main:
    def __init__(self):
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        datalist: List['Data'] = list()
        lines: List['str'] = content.split(sep="\n")
        for i in range(1, len(lines)):
            d = Data(lines[i])
            datalist.append(d)

        fo = len(datalist)
        print("3feladat:    " + str(fo) + " fő indult")

        db = 0
        for index in range(0, len(datalist)):
            if datalist[index].kategoria == "Noi" and datalist[index].megtetttav == str(100):
                db = db + 1
        print("4feladat:    " + "a versenyzők közül " + str(
            db) + " női kategóriában induló versenyző tette meg a teljes távot")

        sportolonev = input()
        szamlalo = 0
        megvan = False
        for index in range(0, len(datalist)):
            szamlalo = szamlalo + 1
            if datalist[index].nev == sportolonev:
                print("5feladat:    " + sportolonev + " indult egyéniben a versenyen")
                print(sportolonev + " a verseny " + datalist[index].megtetttav + " százalékát teljesítette")
                megvan = True
                break
            if megvan == False and szamlalo == len(datalist):
                print("5feladat:    " + sportolonev + " nem indult egyéniben a versenyen")



        legjobbnoi = None
        legjobbferfi = None
        for index in range(0, len(datalist)):
            if datalist[index].kategoria == "Noi":
                jelenleginoi = datalist[index].ido
                jelenleginoi = jelenleginoi.replace(":", "")
                int(jelenleginoi)
                if legjobbnoi == None:
                    legjobbnoi = jelenleginoi
                    legjobbnoinev = datalist[index].nev
                    legjobbnoiido = datalist[index].ido
                if jelenleginoi < legjobbnoi:
                    legjobbnoi = jelenleginoi
                    legjobbnoinev = datalist[index].nev
                    legjobbnoiido = datalist[index].ido
            if datalist[index].kategoria == "Ferfi":
                jelenlegiferfi = datalist[index].ido
                jelenlegiferfi = jelenlegiferfi.replace(":", "")
                int(jelenlegiferfi)
                if legjobbferfi == None:
                    legjobbferfi = jelenlegiferfi
                    legjobbferfinev = datalist[index].nev
                    legjobbferfiido = datalist[index].ido
                if jelenlegiferfi < legjobbferfi:
                    legjobbferfi = jelenlegiferfi
                    legjobbferfinev = datalist[index].nev
                    legjobbferfiido = datalist[index].ido

        print("8feladat:    Női kategória győztese: " + str(legjobbnoinev) + " -- " + str(legjobbnoiido))
        print("8feladat:    Férfi kategória győztese: " + str(legjobbferfinev) + " -- " + str(legjobbferfiido))



Main()
