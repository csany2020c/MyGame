from typing import List

class motor:
    def __init__(self,) -> None:
        super().__init__()

        self.marka: str = 0
        self.evjarat: int = 0
        self.ccm: int = 0
        self.valto: int = 0
        self.szereted: bool = False

    def __str__(self):
        return " marka = {a}, evjarat = {b}, ccm = {c}, valto = {d}".format(a=self.marka, b=self.evjarat, c=self.ccm, d=self.valto)

nev = motor()
nev.marka = "Honda"
nev.evjarat = 2022
nev.ccm = 450
nev.valto = "manuális"
nev.szereted = False
nev.szereted = True

nev1 = motor()
nev1.marka = "Suzuki"
nev1.evjarat = 2021
nev1.ccm = 450
nev1.valto = "manuális"
nev1.szereted = False
nev1.szereted = True

nev2 = motor()
nev2.marka = "KTM"
nev2.evjarat = 2020
nev2.ccm = 450
nev2.valto = "manuális"
nev2.szereted = False
nev2.szereted = True

nev3 = motor()
nev3.marka = input("A márka neve:")
nev3.evjarat = input("A motor évjárata:")
nev3.ccm = input("Lökettérfogat:")
nev3.valto = input("Váltó típusa:")
nev3.szereted = input("Szeretem ezt a márkát (I/N):")

lista:List['motor'] = list()
lista.append(nev)
lista.append(nev1)
lista.append(nev2)
lista.append(nev3)
for i in lista:
    print(i)



