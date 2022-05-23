import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        # print(parseString)
        fields: List['str'] = parseString.split(" ")
        self.ev: int = int(fields[0])
        self.het: str = fields[1]
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmeny: str = fields[5]




    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col}; {asd}; {igen};".format(x=self.ev, y=self.het, txt=self.fordulo, col=self.t13p1, asd=self.ny13p1, igen=self.eredmeny)



class Main:

    def __init__(self) -> None:

        super().__init__()
        f: TextIO = open("toto.txt", "r", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        if len(lines) > 2000:
            print("2000 sor felet van")
        else:
            for i in range(0, len(lines) - 1):
                d = Data(lines[i])
                datalist.append(d)
            for d in datalist:
                print(d)

            eredmeny = 0
            for i in range(0, len(lines) - 1):
                eredmeny = datalist[i].fordulo + eredmeny
            print(eredmeny)

            telitalat = 0
            for i in range(0, len(lines) - 1):
                telitalat = datalist[i].t13p1 + telitalat
            print(telitalat)

            fizet = 0
            osszeg = 0
            for i in range(0, len(lines) - 1):
                fizet = datalist[i].t13p1 * datalist[i].ny13p1
                osszeg = fizet + osszeg
            print(osszeg)


            legkisebb: int = 99999999999999999
            for i in range(len(lines) - 1):
                if datalist[i].ny13p1 > 0:
                    if datalist[i].ny13p1 < legkisebb:
                        legkisebb = datalist[i].ny13p1
                        legkisebbsorszam = i
            print(legkisebb)
            print(legkisebbsorszam)
            print(datalist[legkisebbsorszam].ev, datalist[legkisebbsorszam].het, datalist[legkisebbsorszam].fordulo)







        f.close()

Main()