import random
from typing import List


class Hazi:
    def __init__(self) -> None:
        super().__init__()
        print("1. Feladat \n")
        szamok:List['int'] = list()
        szam1:int = self.checkint("Írj be egy számot: \n")
        szam2:int = self.checkint("Írj be egy számot: \n")
        szam3:int = self.checkint("Írj be egy számot: \n")
        szamok.append(szam1)
        szamok.append(szam2)
        szamok.append(szam3)
        max = szamok[0]
        for i in szamok:
            if i > max:
                max = i
        print(f"A Legnagyobb szám a(z) {max}")

        print("2.feladat \n")
        szamok2:List['int'] = list()
        for i in range(8):
            szamok2.append(i)
        osszeg:int = 0
        for i in szamok2:
            osszeg+=i
        atlag:float = osszeg / len(szamok2)
        atlagalattiak:List['int'] = list()
        for i in szamok2:
            if i < atlag:
                atlagalattiak.append(i)
        print(f"Átlagalatti számok: {atlagalattiak}")

        print("3.Feladat \n")
        szamok3:List['int'] = list()
        for i in range(1,91):
            szamok3.append(i)
        for i in range(200):
            randomIndex:int = random.randint(0,len(szamok3)-1)
            randomIndex2:int = random.randint(0,len(szamok3)-1)
            szam1:int = szamok3[randomIndex]
            szamok3[randomIndex] = szamok3[randomIndex2]
            szamok3[randomIndex2] = szam1
        print("Lista első öt eleme: ")
        for i in range(5):
            print(szamok3[i])

        print("4.Feladat \n")
        self.checkdividable(21)

        print("5.Feladat \n")
        self.szamkitalalas(17)






    def checkint(self,text:str) -> int:
        while True:
            be: str = input(text)
            try:
                szam:int = int(be)
                return szam
            except:
                pass

    def checkdividable(self,szam:int) -> bool:
        while True:
            be:str = input(f"Írj be egy {szam}-el osztható számot")
            try:
                n:int = int(be)
                if n % szam == 0 and n != 0:
                    return True
            except:
                pass

    def szamkitalalas(self,max:int):
        szamok:List['int'] = list()
        for i in range(0,max+1):
            szamok.append(i)
        randomIndex:int = random.randint(0,max)
        randomNumber:int = szamok[randomIndex]

        while True:
            be:str = input(f"Találd ki a számot! A szám 0 és {max} között van!")
            try:
                inputszam:int = int(be)
                if inputszam < randomNumber:
                    print("A generált szám nagyobb!")
                    pass
                elif inputszam > randomNumber:
                    print("A generált szám kisebb!")
                    pass
                else:
                    print("Eltaláltad! :)")
                    return True
            except:
                print("Lehetőleg számot :)")








Hazi()