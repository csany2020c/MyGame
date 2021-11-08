import string
from typing import TextIO
from typing import List
class Data:

    def __init__(self, text) -> None:
        super().__init__()
        print(text)

        fields:List['str'] = text.split(";")

        self.year : int = int(fields[0])
        self.name : str = str(fields[1])
        self.borthdeath : str = str(fields[2])
        self.cCode : str = str(fields[3])
        self.szoveg : str = ""


    def __str__(self) -> str:
        # Formázott szöveg, str.format(...) . A {} közé rakott szövegek a formati függvényben paraméterként használhatók, érték adható a helyükre.
        return "year = {y}; name = {n}; borthdeath = {bd}; countryCode = {cc}".format(y=self.year, n=self.name,
                                                                                      bd=self.borthdeath, cc=self.cCode)


class Main:
    def __init__(self) -> None:
        super().__init__()

        t = TextIO = open("!_Spec/orvosi_nobeldijak.txt","r")
        szoveg : str = t.read()
        t.close()
        print("tartalom:")

        sorok : List['str'] = szoveg.split(sep="\n")
        print(sorok)

        dataList:List['Data'] = list()

        for s in sorok:
            # Új példány létrehozása, a bemenet egy str. A további daraboládokat a Data konstruktora végzi.
            d = Data(s)
            # Hozzáfűzés a listához.
            dataList.append(d)
        print("Print list")

        # Végigjárj a datalist listát, melynek minden eleme Data típusú.
        for d in dataList:
            # Mivel fent van egy szépen megírt __str__ függvény, ezlért a Data típus könnyedén, automatikusan (implicit) str típussá alakul.
            print(d)

Main()