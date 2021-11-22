import string
from typing import TextIO
from typing import List

class Adat:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

        fields: List['str'] = parseString.split(";")
        self.ev: int = int(fields[0])
        self.nev: str = fields[1]
        self.szul: str = fields[2]
        self.orszag: str = fields[3]

    def __str__(self) -> str:
        # Formázott szöveg, str.format(...) . A {} közé rakott szövegek a formati függvényben paraméterként használhatók, érték adható a helyükre.
        return "ev = {ev}; nev = {nev}; szul = {szul}; orszag = {orszag}".format(ev=self.ev, nev=self.nev, szul=self.szul, orszag=self.orszag)

class Main:

    def __init__(self) -> None:
        super().__init__()

        # Fájl megnyitása olvasásra. A második paraméret a megnyitás típusa, r == read, w == write
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")

        # A fájl összes adatát kiolvassa. Az f-en keresztül többféle metódus is elérhető, olvasható egy bájt, egy sor, stb...
        content: str = f.read()

        # Fájl bezárása. Illik megtenni, ha már nem használjuk tovább. Így más programok is hozzáférhetnek. Egyébként a program végén úgyis felszabadul:)
        f.close()

        print("Content:")
        # A tartalom egy sima string a read() függvény után.
        print(content)
        # A megoldáshoz szükséges, hogy a fájl tartalmát a sorvégeknél törjük meg. A tördelést az str típus split függvénye teszi lehetővé, aminek a kimenete egy lista, melyben az eltört részek találhatók.
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        # Lista kiírása. A lista a 0. indexxel kezdődik. lines[0] lines[1] ... ahány darab van - 1
        print(lines)

        print("Load to List")
        # Egy új lista létrehozása a fent deklarált típusból, mert ezzel szeretnénk majd tárolni a későbbi feldolgozáshoz az adatokat.
        datalist: List['Adat'] = list()
        # Ez a ciklus végigjárja a sorok listáját. Minde elem str típusú. Az s változó is str típusú, minden körben (ciklusban) egyetlen listaelemre mutat, és az összeset végigveszi.
        # Ilyen ciklusban NE töröljünk listaelemet! Megoldás későbbiekben...
        for i in range(1, len(lines)-1):
            # Új példány létrehozása, a bemenet egy str. A további daraboládokat a Data konstruktora végzi.
            d = Adat(lines[i])
            # Hozzáfűzés a listához.
            datalist.append(d)
        print("Print list")

        # Végigjárj a datalist listát, melynek minden eleme Data típusú.
        for d in datalist:
            # Mivel fent van egy szépen megírt __str__ függvény, ezlért a Data típus könnyedén, automatikusan (implicit) str típussá alakul.
            print(d)

Main()
