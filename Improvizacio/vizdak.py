from typing import List
from typing import TextIO


class Alma:
    def __init__(self):
        super().__init__()

        self.szin: str = "piros"
        self.nagysaga: int = 5
        self.erett: bool
        self.finom: bool


myalma = Alma()

myalma.szin = "piros"
myalma.nagysaga = 5
myalma.erett = True or False
myalma.finom = True or False
#hf ket osztalyt leterhozni es peldanyolakat

print(myalma.erett)


class Haz:
    def __init__(self):
        super().__init__()
        self.szin: str = "kék"
        self.nagysaga: int = 150
        self.csaladi: bool

myHaz = Haz()

myHaz.szin = "kék"
myHaz.nagysaga = 150
myHaz.csaladi = True or False

print(myHaz.csaladi)

class TV:
    def __init__(self):
        super().__init__()
        self.minoseg: str = "HD"
        self.nagysaga: int = 125
        self.szin: str = "fekete"


myTV = TV()
myTV.szin = "fekete"
myTV.nagysaga = 125
myTV.minoseg = "HD"
print()