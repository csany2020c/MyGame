import os
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
        return " marka = {a}, evjarat = {b}, ccm = {c}, valto = {d}, szereted = {e}".format(a=self.marka, b=self.evjarat, c=self.ccm, d=self.valto, e=self.szereted)

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def intbeolvas(prompt: str, min: int = 0, max: int = 1000) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

# nev = motor()
# nev.marka = "Honda"
# nev.evjarat = 2022
# nev.ccm = 450
# nev.valto = "manuális"
# nev.szereted = True
#
# nev1 = motor()
# nev1.marka = "Suzuki"
# nev1.evjarat = 2021
# nev1.ccm = 450
# nev1.valto = "manuális"
# nev1.szereted = False
#
#
# nev2 = motor()
# nev2.marka = "KTM"
# nev2.evjarat = 2020
# nev2.ccm = 450
# nev2.valto = "manuális"
# nev2.szereted = False

lista:List['motor'] = list()

fn = "mbmotorok.txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    a = motor()
    a.marka = sorok[i]
    i += 1
    a.evjarat = sorok[i]
    i += 1
    a.ccm = strtobool(sorok[i])
    i += 1
    a.valto = int(sorok[i])
    i += 1
    list.append(a)
fr.close()


while boolbeolvas("Akarsz többet felvinni?"):
    nev3 = motor()
    nev3.marka = input("A márka neve:")
    nev3.evjarat = input("A motor évjárata:")
    nev3.ccm = intbeolvas("Kérem a motor lökettérfogatát: ")
    nev3.valto = input("Váltó típusa:")
    nev3.szereted = boolbeolvas("Szereted?")


#lista.append(nev)
#lista.append(nev1)
#lista.append(nev2)
#lista.append(nev3)
#for i in lista:
    #print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in lista:
    f.write(i.__str__() + "\n")
f.close()



