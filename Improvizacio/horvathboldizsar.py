from typing import *

class asvanyviz():
    def __init__(self):
        self.marka: str = str("Márka")
        self.szensavas: bool = False
        self.mennyisege: int = int(0)
        self.ara: int = int(0)
        self.szarmazasih: str = str("Származásihely")

    def __str__(self) -> str:
        return f"Márka: {self.marka} | Szénsav: {self.szensavas} | Mennyisége: {self.mennyisege}l | Ára: {self.ara}Ft,- | Származási helye: {self.szarmazasih}"

viz1 = asvanyviz()
viz1.marka = "Szentkirályi"
viz1.szensavas = True
viz1.mennyisege = 1
viz1.ara = 138
viz1.szarmazasih = "Magyarország"

viz2 = asvanyviz()
viz2.marka = "Jana"
viz2.szensavas = False
viz2.mennyisege = 5
viz2.ara = 719
viz2.szarmazasih = "Magyarország"

viz3 = asvanyviz()
viz3.marka = "Cоор Aquarius"
viz3.szensavas = False
viz3.mennyisege = 1.5
viz3.ara = 129
viz3.szarmazasih = "Magyarország"

ujviz = asvanyviz()
ujviz.marka: str = input("Márkája: ")
if ujviz.marka == "skip" or "Skip" or "SKIP":
    ujviz.marka = ""
else:
    ujviz.szensavas: str = input("Szénsavas(I/H): ")
    ujviz.mennyisege: int = input("Hány liter: ")
    ujviz.ara: int = input("Ára(Ft,-)): ")
    ujviz.szarmazasih: str = input("Származási helye: ")

teszt: List['asvanyviz'] = list()

teszt.append(viz1)
teszt.append(viz2)
teszt.append(viz3)

if ujviz.marka != "":
    teszt.append(ujviz)

for i in range(len(teszt)):
    print(teszt[i])









