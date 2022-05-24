from typing import List


class Adatok:
    def __init__(self, Parsestring: str) -> None:
        super().__init__()
        fieldls: List['str'] = Parsestring.split(" ")
        self.ev: int = int(fieldls[0])
        self.het: int = int(fieldls[1])
        self.fordulo: int = int(fieldls[2])
        self.T13p1: int = int(fieldls[3])
        self.Ny13p1: int = int(fieldls[4])
        self.Eredmenyek: str = str(fieldls[5])

    def __str__(self):
        return "ev = {a}, het = {b}, fordulo = {c}, T13p1 = {d}, Ny13p1e = {e}, Eredmenyek = {f}".format(a=self.ev, b=self.het, c=self.fordulo, d=self.T13p1, e=self.Ny13p1, f=self.Eredmenyek)


class Beolvasasa:
    def __init__(self):
        super().__init__()
        read: List['str'] = open("toto.txt", "r", encoding="utf-8").read().strip().split(sep="\n")
        adatokuj: List[Adatok] = list()
        for i in range(0, len(read)):
            adatokuj.append(Adatok(read[i]))

        for i in adatokuj:
            print(i)

        print("3. feladat:")
        # a = 0
        # for i in range(0, len(adatokuj)):
        #     a += adatokuj[i].fordulo
        # print(a)
        print(len(adatokuj))

        print("4.feladat:")
        aa = 0
        for i in range(0, len(adatokuj)):
            aa += adatokuj[i].T13p1
        print(aa)

        print("5. feladat:")
        b = 0
        for i in range(0, len(adatokuj)):
            b += adatokuj[i].T13p1 * adatokuj[i].Ny13p1
        print(b)

        print("7. feladat:")
        e = 0
        for i in range(0, len(adatokuj)):
            if adatokuj[i].Ny13p1 > e:
                e = adatokuj[i].Ny13p1

        for i in range(0, len(adatokuj)):
            if e == adatokuj[i].Ny13p1:
                print(adatokuj[i].ev, adatokuj[i].het)

        b = adatokuj[0].Ny13p1
        for i in range(0, len(adatokuj)):
            if adatokuj[i].Ny13p1 < b:
                b = adatokuj[i].Ny13p1

        for i in range(0, len(adatokuj)):
            if b == adatokuj[i].Ny13p1:
                print("Legkisebb:", adatokuj[i].ev, adatokuj[i].het)

        print("8. feladat:")
        asd = 0
        for i in range(0, len(adatokuj)):
            for i in str(adatokuj[i].Eredmenyek):
                if i == "X":
                    asd += 1
        print(asd)

        print("9. feladat:")
        alma = 0
        for i in range(0, len(adatokuj)):
            for i in str(adatokuj[i].Eredmenyek):
                if i == "X":
                    alma += 1
                    if alma == 1:
                        print("False")
                        break
#elkeszetesi ido: 1h
Beolvasasa()
