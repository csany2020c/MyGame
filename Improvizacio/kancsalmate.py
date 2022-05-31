from typing import TextIO
from typing import List

class cipo:

    def __init__(self) -> None:
        super().__init__()
        self.szin: List['str'] = list()
        self.meret: int = 0
        self.marka: str = ""
        self.tepozaras: bool = False
        self.ar: float = 0





    def __str__(self) -> str:
        return f"Színe {self.szin} Mérete {self.meret} Márka {self.marka} Tépőzárás-e {self.tepozaras} ára {self.ar} $"

def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False


f: TextIO = open("Kancsalmate.txt", "w", encoding="utf8")
cipok: List['cipo'] = list()

while boolbeolvas("Szeretne autót felvinni a billentyűzetről?"):
    shoe1 = cipo()
    shoe1.meret = input("Meret")
    f.write(f"Méret: {shoe1.meret}")
    shoe1.ar = input("Ar")
    f.write(f" ÁR: {shoe1.ar}")
    shoe1.tepozaras = input("Tepozaras-e")
    f.write(f" Tépőzáras-e {shoe1.tepozaras}")
    shoe1.marka = input("Marka")
    f.write(f" Márka: {shoe1.marka}")

for i in range(3):
    x: str = str(input())
    shoe1.szin.append(x)


cipok.append(shoe1)


shoe2 = cipo()
shoe2.meret = 41
shoe2.ar = 101
shoe2.tepozaras = True
shoe2.marka = "adidas"

for i in range(3):
    x: str = str(input())
    shoe2.szin.append(x)

cipok.append(shoe2)


shoe3 = cipo()
shoe3.meret = 39
shoe3.ar = 60
shoe3.tepozaras = False
shoe3.marka = "puma"

for i in range(3):
    x: str = str(input())
    shoe3.szin.append(x)


cipok.append(shoe3)


for i in range(len(cipok)):
    print(cipok[i])

cipo()