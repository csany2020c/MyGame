from typing import List
from random import randint
class Doga:
    def __init__(self) -> None:
        super().__init__()
        self.masodik()

    def elso(self):
        a: int = int(input("kérem a számot!"))
        b: int = int(input("kérem a másik számot!"))
        for i in range(b + 1):
            osszeg = a * i
            if i != 0:
                print(osszeg)


    def masodik(self):
        nevek: ['List'] = list()
        counter = 0
        while True:
            myrandom = randint(0, counter)
            nev: str = str(input("kérem a nevet!"))
            if nev == "":
                break
            nevek.append(nev)
            counter = counter + 1
        print(nevek[myrandom])







class mouse:
    def __init__(self) -> None:
        super().__init__()
        self.eger1()

    def eger1(self):
        egerek: ['List'] = list()
        buttons: int = int(input("egér gombjai:"))
        scroll: str = str(input("Van-e függőleges görgője: (True, False)"))
        if scroll == "True":
            scroll1: bool = True
        if scroll == "False":
            scroll1: bool = False

        scrollv: str = str(input("Van-e vízszintes görgője: (True, False)"))
        if scrollv == "True":
            scrollv1: bool = True
        if scrollv == "False":
            scrollv1: bool = False
        manufacturer: str = str(input("Gyártója:"))
        egerek.append(buttons)
        egerek.append(scroll1)
        egerek.append(scrollv1)
        egerek.append(manufacturer)

        buttonsa: int = int(input("egér gombjai:"))
        scrolla: str = str(input("Van-e függőleges görgője: (True, False)"))
        if scrolla == "True":
            scroll1a: bool = True
        if scrolla == "False":
            scroll1a: bool = False

        scrollva: str = str(input("Van-e vízszintes görgője: (True, False)"))
        if scrollva == "True":
            scrollv1a: bool = True
        if scrollva == "False":
            scrollv1a: bool = False
        manufacturera: str = str(input("Gyártója:"))
        egerek.append(buttonsa)
        egerek.append(scroll1a)
        egerek.append(scrollv1a)
        egerek.append(manufacturera)

        buttonsb: int = int(input("egér gombjai:"))
        scrollb: str = str(input("Van-e függőleges görgője: (True, False)"))
        if scrollb == "True":
            scroll1b: bool = True
        if scrollb == "False":
            scroll1b: bool = False

        scrollvb: str = str(input("Van-e vízszintes görgője: (True, False)"))
        if scrollvb == "True":
            scrollv1b: bool = True
        if scrollvb == "False":
            scrollv1b: bool = False
        manufacturerb: str = str(input("Gyártója:"))
        egerek.append(buttonsb)
        egerek.append(scroll1b)
        egerek.append(scrollv1b)
        egerek.append(manufacturerb)





        print(f"Egér gombjainak száma:{egerek[0]}, Van-e függőleges görgő:{egerek[1]}, Van-e vízszintes görgő:{egerek[2]}, Gyártója:{egerek[3]}")
        print(f"Egér gombjainak száma:{egerek[4]}, Van-e függőleges görgő:{egerek[5]}, Van-e vízszintes görgő:{egerek[6]}, Gyártója:{egerek[7]}")
        print(f"Egér gombjainak száma:{egerek[8]}, Van-e függőleges görgő:{egerek[9]}, Van-e vízszintes görgő:{egerek[10]}, Gyártója:{egerek[11]}")
Doga()