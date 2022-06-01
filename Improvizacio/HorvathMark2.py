from typing import List


class earphone():

    def __init__(self) -> None:
        super().__init__()
        self.ar: int = 0
        self.szallitas: int = 0
        self.hany_nap: int = 0
        self.nev: str = ""
        self.szin: str = ""
        self.wireless: bool = True

    def __str__(self) -> str:
        return "Ár = {a}; Szállítás = {b}; Hány nap = {c}; Név = {d}; Szín = {e}; Wireless = {f}".format(a = self.ar, b = self.szallitas, c = self.hany_nap, d = self.nev, e = self.szin, f=self.wireless)

    def teljesar(self) -> int:
        return self.ar + self.szallitas

F9 = earphone()
F9.ar = 5098
F9.szallitas = 253
F9.hany_nap = 31
F9.nev = "F9 TWS Headphones"
F9.szin = "black"
#print(F9.teljesar())

#print(F9)

PCS = earphone()
PCS.ar = 4
PCS.hany_nap = 61
PCS.nev = "PCS Portable Sport Earphone"
PCS.szin = "gray"
PCS.wireless = False

#print(PCS)

TWS = earphone()
TWS.ar = 1870
TWS.hany_nap = 41
TWS.nev = "Original Tws I12 Earphone"
TWS.szin = "white"

#print(TWS)

MSR = earphone()
MSR.ar = 965
MSR.szallitas = 0
MSR.hany_nap = 41
MSR.nev = "Magnetic Sports Running Earphone"
MSR.szin = "black"
# MSR.wireless = True

#print(MSR)

QKZ = earphone()
QKZ.ar = 965
QKZ.szallitas = 385
QKZ.hany_nap = 61
QKZ.nev = "AK6 Copper Driver HiFi Sport Earphone"
QKZ.szin = "red and blue"
QKZ.wireless = False

#print(QKZ)

lista: List = list()
lista.append(QKZ)
lista.append(MSR)
lista.append(TWS)
lista.append(PCS)
lista.append(F9)

for i in lista:
    print(i)
    print(i.teljesar(), "Forint")

