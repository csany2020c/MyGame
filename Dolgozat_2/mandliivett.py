from typing import List


class dolgozat:
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = str()
        self.ar: int = 0
        self.tomeg: int = 0

    def __str__(self) -> str:
        return "Név = {a}; Ár = {s}; Tömeg = {d}".format(a =self.nev, s=self.ar, d=self.tomeg)

    # def elsofeladat(self):
    #     szam: 0
    #     q: int = int(input("Adjon meg egy számot: "))
    #     w: int = int(input("Adjon meg még egy számot:"))
    #     for i in range:
    #
    #         print(szam)

    def arosszeg(self) -> int:
        return x.ar + y.ar + z.ar


x = dolgozat()
x.nev = "Kenyér"
x.ar = 500
x.tomeg = 1

y = dolgozat()
y.nev = "Cukor"
y.ar = 1500
y.tomeg = 3

z = dolgozat()
z.nev = "Liszt"
z.ar = 1000
z.tomeg = 2

print("3. feladat")
# print(x)
# print(y)
# print(z)


bevasarlolista = dolgozat

lista: List['bevasarlolista'] = list()

lista.append(x)
lista.append(y)
lista.append(z)


for i in lista:
    print(i)
    print("A termékek árának összege:", i.arosszeg(), "Forint")

print("--------------------")
print("1.feladat")
q: input("Adjon meg egy számot:")
w: input("Adjon meg még egy számot:")