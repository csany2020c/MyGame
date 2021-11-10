import string
from typing import TextIO
from typing import List
class Eloado:
    def __init__(self,text) -> None:
        super().__init__()
        print(text)

        fields: List['str'] = text.split("  ")

        self.eloadoid: int = int(fields[0])
        self.name: str = str(fields[1])
        self.zenekar: int = int(fields[2])

    def __str__(self) -> str:
        return "artistId = {id}; name = {n}; band = {b}".format(id=self.eloadoid, n=self.name,
                                                                                      b=self.zenekar)

class Main:
    def __init__(self) -> None:
        super().__init__()

        t: TextIO = open("!_Specs/eloadok.txt","r")
        szoveg : str = t.read()
        t.close()

        sorok : List['str'] = szoveg.split(sep="\n")

        dataList:List['Eloado'] = list()

        for i in range(1, len(sorok) - 1):
            # Új példány létrehozása, a bemenet egy str. A további daraboládokat a Data konstruktora végzi.
            d = Eloado(sorok[i])
            # Hozzáfűzés a listához.
            dataList.append(d)
        print("Print list")

        # Végigjárj a datalist listát, melynek minden eleme Data típusú.
        for d in dataList:
            # Mivel fent van egy szépen megírt __str__ függvény, ezlért a Data típus könnyedén, automatikusan (implicit) str típussá alakul.
            print(d)

Main()