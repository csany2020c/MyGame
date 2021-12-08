import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        self.Ev: int = int(fields[0])
        self.Nev: str = fields[1]
        self.Halalozas: int = None
        self.SzuletesHalalozas: str = fields[2]
        szh: List['str'] = self.SzuletesHalalozas.split("-")
        self.Szuletes: int = int(szh[0])
        #print(len(szh))
        if szh[1] != "":
            self.Halalozas = int(szh[1])
        self.Orszagkod: str = fields[3]
        #print(self)

    def __str__(self) -> str:
        return "Ev = {x}; Nev = {y}; SzuletesHalalozas = {txt}; Sz = {sz} H = {h}  Orszagkod = {col}".format(x=self.Ev, y=self.Nev, txt=self.SzuletesHalalozas, col = self.Orszagkod, sz= self.Szuletes, h= self.Halalozas)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt")
        content: str = f.read()
        #print("Content:")
        #print(content)
        lines: List['str'] = content.split(sep="\n")
        dijazottak: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            dijazottak.append(Data(lines[i]))
        f.close()


        print("3. feladat")
        print("Díjazottak száma: {db} fő ".format(db=len(dijazottak)))


        # Legnagyobb értékének a kiválasztása egy listából

        # A jelenlegi legnagyobb érték a legyen a legelső eleme a listának.
        # Ha egy eleme van a listának, akkor ez marad a legnagyobb.
        # Mivel a listák indexelése 0-tól kezdődik, így ez az index legyen 0.
        # A max változó indexet tartalmaz.
        # Ha egy eleme sincs a listának, akkor az algoritmus nem ad helyes megoldást, külön IF szerkezetben kellene kezelni.
        max: int = 0

        # Mivel az első elemet már kezeltük (ez a legnagyobb eddig), ezért a többi elemet kell végignézni, hogy van-e
        # közte nagyobb. A for ciklus a 1-es indextől (azaz a 2. elemtől) kezdve a legutolsó indexig (elemszám -1-ig)
        # minden indexet sorra vesz.
        for i in range(1, len(dijazottak)):
            # Indexek kiírása
            # print(i)

            # Az indexeket felhasználva ha az i-edik (amin végig jár a ciklus) elem nagyobb, mint a max-adik:), akkor
            # akkor a max változóba másolja az i változó értékét, mert ez volt az eddigi legnagyobb.
            if dijazottak[i].Ev > dijazottak[max].Ev:
                max = i

        # Az algoritmus megy minimum keresésre is, az IF-ben a relációs jelet meg kell fordítani.
        print(dijazottak[max].Ev)


        # Az input függvény a billentyűzetről olvas be szöveget, a kimenete str típus.
        kod: str = input()
        #print(kod)


        # Feltételnek megfelelő elemek megszámlálása egy listában

        # A db változó értéke kezdetben legyen 0, mert 0 db feltételnek megfelelő elem van, mielőtt nekiállunk számolni.
        db: int = 0

        # A ciklus 0-tól indul az utols idexig. A k változó index érték, és minden körben egy másik elemet vesz elő ennek a segítségével.
        for k in range(0, len(dijazottak)):
            # Az elemek kírása indexekkel együtt. Ez nem a feladat része, csak teszt.
            # print(str(k) + " - " + str(dijazottak[k]))

            # Ha a k-adik érték megfelel a feltételnek, akkor a db változó értékét növeli 1-el.
            # A példában a káadik díjazott országkódja megegyezik a felhasználó által beírttal, akkor növeli.
            if dijazottak[k].Orszagkod == kod:
                db += 1

        # A darabszám értékének a felhasználása a ciklus végén
        if db == 0:
            print("A megadott országból nem volt díjazott!")
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db = db))


        # iterátoros végigjárás
        for it in dijazottak:
            print(it)

        # index alapú végigjárás
        for index in range(0, len(dijazottak)):
            print(str(index) + " ---- " + str(dijazottak[index]))

        #
        # orszagok: dict = dict()
        # for k in range(0, len(dijazottak)):
        #     try:
        #         orszagok[dijazottak[k].Orszagkod]+=1
        #     except:
        #         orszagok[dijazottak[k].Orszagkod]=1
        #
        # for k, v in orszagok.items():
        #     if v > 5:
        #         print("{k} {v}".format(k=k, v=v))
        #

Main()












