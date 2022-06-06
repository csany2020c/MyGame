from typing import List
import random

class hazi:

    def __init__(self) -> None:
        super().__init__()
        #self.eldonto()
        #self.kiiratos(2, 3, 4, 5, 2, 1, 4, 4)
        #self.randomos()
        self.oszthatoe()
        #self.szamkitalalos()

#elso feladat
    def eldonto(self):
        listam : List[hazi] = list()
        self.elsoszam:int = int(input("Kérem írja be az első számot: "))
        self.masodikszam: int = int(input("Kérem írja be az második számot: "))
        self.harmadikszam: int = int(input("Kérem írja be az harmadik számot: "))
        listam.append(self.elsoszam)
        listam.append(self.masodikszam)
        listam.append(self.harmadikszam)

        self.biggestszam = max(listam)


        print(f"Az ön legnagyobb száma: {self.biggestszam}")

#masodik feladat
    def kiiratos(self, egy: int, ketto: int, harom: int, negy: int, ot:int, hat:int, het: int, nyolc: int):
        listam : List['hazi'] = list()
        listam.append(egy)
        listam.append(ketto)
        listam.append(harom)
        listam.append(negy)
        listam.append(ot)
        listam.append(hat)
        listam.append(het)
        listam.append(nyolc)
        alap:int = 0
        for i in listam:
            alap += i
        atlag:float = alap /len(listam)
        print(f"A számok átlaga {atlag}.")

#harmadik feladat
    def randomos(self):
        listam: List[hazi] = list()
        for i in range(0, 90):
            listam.append(i)
        for j in range(200):
            egyikrandom: int = random.randint(0, len(listam)-1)
            masodikrandom: int = random.randint(0, len(listam)-1)
            szam1: int = listam[egyikrandom]
            listam[egyikrandom] = listam[masodikrandom]
            listam[masodikrandom] = szam1
        print("Lista első öt eleme: ")
        for k in range(5):
            print(listam[k])

#negyedik feladat
    def oszthatoe(self):
        while True:
            be:int = input("Adj meg egy számot: ")
            if int(be) % 29 == 0:
                print("A beírt szám osztható 29-el.")
                return True
            else:
                pass
                print("A szám nem osztható 29-el, próbáld újra")

#otodikfeladat
    def szamkitalalos(self):
        beszam:int = int(input("Add meg a legnagyobb számot! \n Ide: "))
        listam:List['int'] = list()
        for i in range(0, beszam):
            listam.append(i)
        egyikrandom:int = random.randint(0, beszam)
        masodikrandom:int = listam[egyikrandom]
        while True:
            beszam2: str = input(f"Szám kitalálós! A legkisebb szám 0, a legnagyobb {beszam} \n Ide írhatod: ")
            bentszam: int = int(beszam2)
            if bentszam < masodikrandom:
                print("Ennél kicsit nagyobb lesz! :)")
                pass
            elif bentszam > masodikrandom:
                print("Leljebb próbálkozz!")
                pass
            else:
                print("Sikerült eltalálnod a számot!")
                return False


hazi()