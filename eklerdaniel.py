import string
from typing import TextIO
from typing import List


class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        # print(parseString)
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = str(fields[0])
        self.szam: int = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tav: int = fields[4]
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
        print(content)
        lines: List['str'] = content.split(sep="\n")
        #print(lines)
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
        #for d in datalist:
             #print(d)
        f.close()

        print("3. feladat: Egyéni indulók : {db} fő".format(db=len(datalist)))
        print(datalist[len(datalist) - 1].szam)
        max: int = 0
        for i in range(1, len(datalist)):
            if datalist[max].versenyzo < datalist[i].versenyzo:
                max = i
        print(datalist[max].versenyzo)

        kod: str = input()
        # # iterátoros végigjárás
         #for it in datalist:
             #print(it)
        #
         # index alapú végigjárás
         #for index in range(0, len(datalist)):
             #print(str(index) + " ---- " + str(datalist[index]))

        db:int = 0
        utolso:int = -1
        for index in range(0, len(datalist)):
            if datalist[index].kategoria == kod:
                db += 1
                utolso = index
        print(db)
        if db == 0:
            print("A megadott országból nem volt díjazott!")
        elif db == 1:
            print(datalist[utolso])
        else:
            print("A megadott országból {db} fő díjazott volt!".format(db=db))


        # Kik kaptak nóbeldíjat a 70-es években, és hányan voltak?
        # A nevüket és a darabszámukat jelenítse meg.


        #db70: int = 0
        #for it in datalist:
            #if it.ev >= 1970 and it.ev <= 1979:
                #print(it.nev)
                #db70 += 1
        #print("Az 1970-es években {db70} díjazott volt.".format(db70 = db70))



        # 6. feladat

        # Létrehoz egy dictionary típusú adatszerkezetet.
        # Ez egy olyan "lista", amelynek az indexei lehetnek szövegek is.
        # Az indexeket itt kulcsnak is szoktuk nevezni.
        # A kulcsok értékei, mint az indexek is, egyediek.
        #orszagok: dict = dict()
        # Végigszalad az adatok listáján.
        #for k in range(0, len(datalist)):
            #try:
                # Megpróbál növelni egy kulcshoz tartozó értéket.
                # Ha bármely hibával elszállna, akkor nem piros hiba jelenik meg,
                # hanem a "try" miatt az "except"-re ugrik.
                #orszagok[datalist[k].orszagkod]+=1
            #except:
                # A kulcsok értékadással jönnek létre.
                # Amennyiben nem létezett ez a kulcs, létrehozza. Későbbiekben majd módosítani fogja csak a fenti utasítással, amennyiben újból előfordul ugyan az az országkód.
                #orszagok[datalist[k].orszagkod]=1

        # Dict végigjárása. k == key (kulcs), v = value (érték) párokat ad vissza.
        #for k, v in orszagok.items():
            # Ha az érték nagyobb, mint 5, akkor írja ki a kulcsot (itt az országkód) és a hozzá tartozó értéke.
            #if v > 5:
                #print("{k} {v}".format(k=k, v=v))





Main()