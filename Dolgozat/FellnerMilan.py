import random
from typing import List


class Dolgozat:
    def __init__(self) -> None:
        super().__init__()
        print("1.feladat:\n")
        szam1:int = int(self.checkInt("Irj be egy szamot!"))
        szam2: int = int(self.checkInt("Irj be meg egy szamot!"))
        print(self.inttosorozat(szam1,szam2))

        print("2.feladat:\n")
        print(self.nevek("Irj be egy nevet!"))

        print("3.feladat:\n")
        mButtons:List['int'] = list()
        for i in range(1,10):
            mButtons.append(i)
        mVizszintes:List['bool'] = (True,False)
        mFuggoleges:List['bool'] = (True,False)
        mGyarto:List['str'] = ("Logitech","Razer","Trust","Sony","LG","Apple")
        egerek:List['Eger'] = list()

        eger1 = Eger()
        eger1.gombokszama = 5
        eger1.vizszintesgorgo = True
        eger1.fuggolegesgorgo = False
        eger1.gyarto = "Logitech"

        egerek.append(eger1)

        eger2 = Eger()
        eger2.gombokszama = 2
        eger2.vizszintesgorgo = True
        eger2.fuggolegesgorgo = True
        eger2.gyarto = "Trust"

        egerek.append(eger2)

        eger3 = Eger()
        eger3.gombokszama = 4
        eger3.vizszintesgorgo = False
        eger3.fuggolegesgorgo = True
        eger3.gyarto = "Razer"

        egerek.append(eger3)


        for i in egerek:
            print(i)

        randomize:bool = self.strtobool("Szeretned randomizalni?")
        if randomize:
            egerek2:List['Eger'] = list()
            for i in range(3):
                mouse:Eger = Eger()
                mouse.gombokszama = mButtons[random.randint(0,len(mButtons)-1)]
                mouse.vizszintesgorgo = mVizszintes[random.randint(0,1)]
                mouse.fuggolegesgorgo = mFuggoleges[random.randint(0, 1)]
                mouse.gyarto = mGyarto[random.randint(0,len(mGyarto)-1)]

                egerek2.append(mouse)
            for i in egerek2:
                print(i)
        else:
            print("Rendben!:)")
            quit()



    def checkInt(self,text:str) -> int:
        while True:
            be:str = input(text)
            try:
                szam:int = int(be)
                return szam
            except:
                pass

    def inttosorozat(self,szam1:int, szam2:int) -> List['int']:
        szamok:List['int'] = list()
        for i in range(1,szam2+1):
            szamok.append(szam1 * i)
        return  szamok

    def nevek(self,text) -> str:
        names:List['str'] = list()
        while True:
            be:str = input(text)
            if be != "" and be != "\n":
                names.append(be)
            else:
                break
        if len(names) > 0:
            return names[random.randint(0,len(names)-1)]
        else:
            return "Nem irtal be egy nevet se!"

    def strtobool(self,text:str) -> bool:
        while True:
            be:str = input(text + "I/N")
            if be.upper() == "I" or be.upper() == "Y":
                return True
            elif be.upper() == "N" or be.upper() == "F":
                return False
            else:
                pass

class Eger():

    def __init__(self,gombokszama:int = 0,vizszintesgorgo:bool = True,fuggolegesgorgo:bool = False,gyarto:str = "Valami Kft.") -> None:
        super().__init__()
        self.gombokszama:int = gombokszama
        self.vizszintesgorgo:bool = vizszintesgorgo
        self.fuggolegesgorgo:bool = fuggolegesgorgo
        self.gyarto = gyarto

    def __str__(self) -> str:
        return f"Gombok szama:{self.gombokszama}, van-e vizszintes gorgo:{self.vizszintesgorgo},van-e fuggoleges gorgo:{self.fuggolegesgorgo}, gyarto:{self.gyarto}"


Dolgozat()