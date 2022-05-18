from typing import List

class Alma:
        nagysaga: int

        def __init__(self, parse: str) -> None:
            super().__init__()
            fields: List['str'] = parse.split(" ")
            self.szin: str = "piros"
            self.nagysaga: int = int("5")
            self.erett: bool
            self.finom: bool


myalma = Alma()

myalma.szin = "piros"
myalma.nagysaga = "5"
myalma.erett = True or False
myalma.finom = True or False


print(myalma.szin)
