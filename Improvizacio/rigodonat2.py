#{termek neve ,nehany tulajdonsaga ,ár, szalliutasi költség,szallitasi ido}
from typing import List

class napszemuveg:
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = str
        self.lencseszin: str = str
        self.naprasotetedike: bool
        self.szallitasiido: int = int
        self.szallitasikoltseg: int = int
        self.ar: int = int

    def teljesar(self) -> int:
        return self.ar + self.szallitasikoltseg


    def __str__(self) -> str:
        return "Név = {a}; Lencseszín = {b}; Napra sőtétedik e = {c}; Ár = {d}; Szállítási idő = {e}; Szállítási költség = {f}".format(a=self.nev, b=self.lencseszin, c=self.naprasotetedike, d=self.ar, e=self.szallitasiido, f=self.szallitasikoltseg)


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
def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
            else:
                print("Hibás érték! Nem az intervallumba tartozó szám!")
        except:
            print("Hibás érték! Számot kérek!")

MyNapszemuveg = napszemuveg()
MyNapszemuveg.nev = "Női Nagy Szemüveg"
MyNapszemuveg.lencseszin = "Kék"
MyNapszemuveg.naprasotetedike = False
MyNapszemuveg.ar = 420
MyNapszemuveg.szallitasiido = 41
MyNapszemuveg.szallitasikoltseg = 0

MyNapszemuveg2 = napszemuveg()
MyNapszemuveg2.nev = "Férfi kerékparos szemüveg"
MyNapszemuveg2.lencseszin = "Átlátszó"
MyNapszemuveg2.naprasotetedike = True
MyNapszemuveg2.ar = 2000
MyNapszemuveg2.szallitasiido = 41
MyNapszemuveg2.szallitasikoltseg = 0

MyNapszemuveg3 = napszemuveg()
MyNapszemuveg3.nev = "Unisex horgász szemüveg"
MyNapszemuveg3.lencseszin = "Zöld"
MyNapszemuveg3.naprasotetedike = False
MyNapszemuveg3.ar = 370
MyNapszemuveg3.szallitasiido = 61
MyNapszemuveg3.szallitasikoltseg = 203




#print(MyNapszemuveg)
#print(MyNapszemuveg2)
#print(MyNapszemuveg3)

lista: List[napszemuveg] = list()
lista.append(MyNapszemuveg)
lista.append(MyNapszemuveg2)
lista.append(MyNapszemuveg3)


MyNapszemuveg2.ar = 1500

for i in lista:
    print(i)
    print(i.teljesar())



