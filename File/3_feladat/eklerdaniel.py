import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        # print(parseString)
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = str(fields[0])
        self.szam: int = int(fields[1])
        self.kategoria: str = fields[2]
        # https://docs.python.org/3/library/datetime.html
        self.versenyido: str = fields[3]
        self.tav: int = int(fields[4])
        #szh: List['str'] = fields[2].split("-")
        #self.szuletes: int = int(szh[0])
        #self.halalozas: int = None
        #if szh[1] != "":
            #self.halalozas = int(szh[1])


    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col};  {tavi}".format(x=self.versenyzo, y=self.szam, txt=self.kategoria, col=self.versenyido, tavi=self.tav)


class Main:

    def __init__(self) -> None:
        super().__init__()
        print("2. feladat")
        f: TextIO = open("!_Specifikacio//ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        # print(content)
        lines: List['str'] = content.split(sep="\n")
        #print(lines)
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            print(d)
        #for d in datalist:
             #print(d)
        f.close()

        print("3. feladat: Egyéni indulok : {db} fő".format(db=len(datalist)))
        print(datalist[len(datalist) - 1].szam)
        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[max].versenyzo < datalist[i].versenyzo:
                max = i
        print(datalist[max].versenyzo)

        kat: str = input()
        tavo: int = int(input())


        db: int = 0
        utolso: int = -1
        for index in range(0, len(datalist)):
            if datalist[index].tav == tavo and datalist[index].kategoria == kat:
                db += 1
                utolso = index

        print(db)
        if db == 0:
            print("A megadott kateg nem volt díjazott!")
        elif db == 1:
            print(datalist[utolso])
        else:
            print("4. feladat: Célba érkező Gugu gágá sportolók:{db} fő".format(db=db))

Main()