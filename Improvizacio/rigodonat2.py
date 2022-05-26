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

for i in lista:
    print(i)



