import string
from typing import TextIO
from typing import List

class Adat:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

        fields: List['str'] = parseString.split(";")
        self.x: int = int(fields[0])  # A 0. indexű elemét a listának átkonvertálja számmá, és eltárolja az x mezőben.
        self.y: int = int(fields[1])  # Az 1. indexű elemét a listának átkonvertálja számmá, és eltárolja az y mezőben.
        self.color: int = (int(fields[2]), int(fields[3]), int(fields[4]))  # A 2,3,4. indexű elemét a listának átkonvertálja számmá, majd egy listába teszi, és eltárolja a color mezőben.
        self.text: str = ""  # A végén lévő stringgel viszont van még munka, mert szóközöket tartalmazhat, és akkor ez feleslegesen fel lett darabolva. Össze kell fűzni.

        for i in range(5, len(
                fields)):  # Az 5. elemtől a lista végéig számol, 1-esével, azaz a fennmaradó indexeket veszi elő, pládul 5 (Hello),6 (World)
            self.text += str(fields[i])  # Hozzáfűzi az str mezőhöz.
            if i < len(fields) - 1:  # Ha nem az utolsó elemről van szó, akkor még egy szóközt is hozzá kell fűzni.
                self.text += " "

        # Más nyelveken "toString". Az objektum példány szöveggé alakításakor ez fut le. Jól jön ebben az esetben, ha tesztelni kell, és csak simán printtel ki akarjuk íratni.

    def __str__(self) -> str:
        # Formázott szöveg, str.format(...) . A {} közé rakott szövegek a formati függvényben paraméterként használhatók, érték adható a helyükre.
        return "x = {x}; y = {y}; text = {txt}; color = {col}".format(x=self.x, y=self.y, txt=self.text, col=self.color)

    class Main:

        def __init__(self) -> None:
            super().__init__()

            # Fájl megnyitása olvasásra. A második paraméret a megnyitás típusa, r == read, w == write
            f: TextIO = open("readme.txt", "r")

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
            for s in lines:
                # Új példány létrehozása, a bemenet egy str. A további daraboládokat a Data konstruktora végzi.
                d = Adat(s)
                # Hozzáfűzés a listához.
                datalist.append(d)
            print("Print list")

            # Végigjárj a datalist listát, melynek minden eleme Data típusú.
            for d in datalist:
                # Mivel fent van egy szépen megírt __str__ függvény, ezlért a Data típus könnyedén, automatikusan (implicit) str típussá alakul.
                print(d)

    Main()
