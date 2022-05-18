from typing import List

class huto:
    def __init__(self):
        self.szin: "szine"
        self.tipus: "fajtaja"
        self.szeleseg: int + 0
        self.magassag: int + 0
        self.marka: "markaneve"
        self.teljesitmeny: "Wolt szam"

adat = huto()
adat.marka = "Gorenje"
adat.szin = "Piros"
adat.szeleseg = 600
adat.magassag = 1940
#ezek mm-be megadott értékek
adat.tipus = "Standard"
adat.teljesitmeny = "70 W"
print(adat.marka)
print(adat.szin)
print(adat.szeleseg)
print(adat.magassag)
print(adat.teljesitmeny)












