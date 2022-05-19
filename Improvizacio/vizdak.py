from typing import List
from typing import TextIO


class Alma:
    def __init__(self):
        super().__init__()

        self.szin: str = "piros"
        self.nagysaga: int = 5
        self.erett: bool
        self.finom: bool

    def __str__(self) -> str:
            return "Szin = {x}; Nagysaga = {y}; Erett = {z}; Finom = {n}".format( x=self.szin, y=self.nagysaga, z=self.erett, n=self.finom)


myalma = Alma()

myalma.szin = "piros"
myalma.nagysaga = 5
myalma.erett = True
myalma.finom = True

myalma2 = Alma()
myalma2.szin = "zöld"
myalma2.nagysaga = 7
myalma2.erett = True
myalma2.finom = False
#print(myalma.erett)

myalma3 = Alma()
myalma3.szin = "sárga"
myalma3.nagysaga = 13
myalma3.erett = False
myalma3.finom = True


myalma.szin = input("Kérem az alma színét:")
myalma.nagysaga = input("Kérem az alma nagyságát:")
Erett = input("Az alma érett e vag nem(I/N):")
if Erett == "I":
    myalma.erett = True
if Erett == "N":
    myalma.erett = False

Finom = input("Az alma finom e vag nem:(I/N):")
if Finom == "I":
    myalma.finom = True
if Finom == "N":
    myalma.finom = False

print(myalma)
print(myalma2)
print(myalma3)




class Haz:
    def __init__(self):
        super().__init__()
        self.szin: str = "kék"
        self.nagysaga: int = 150
        self.csaladi: bool

    def __str__(self) -> str:
        return "Szin = {x}; Nagysaga = {y}; Csaladi = {z}".format(x=self.szin, y=self.nagysaga, z=self.csaladi)
myHaz = Haz()

myHaz.szin = "kék"
myHaz.nagysaga = 150
myHaz.csaladi = True or False

#print(myHaz)

class TV:
    def __init__(self):
        super().__init__()
        self.minoseg: str = "HD"
        self.nagysaga: int = 125
        self.szin: str = "fekete"

    def __str__(self) -> str:
        return "Szin = {x}; Nagysaga = {y}; Minoseg = {z}".format(x=self.szin, y=self.nagysaga, z=self.minoseg)

myTV = TV()
myTV.szin = "fekete"
myTV.nagysaga = 125
myTV.minoseg = "HD"
#print(myTV)