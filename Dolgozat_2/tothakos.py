from typing import List

#1.feladat
def elso(a: int, b: int) -> List['int']:
    szam: List['int'] = list()
    while True:
        asd = input("Kérem az első számot:")
        dsa = input("Kérem a második számot:")
#print(elso)


#2.feladat
def masodik():
    while True:
        be: int = input("Kérek egy számot: ")
        if be.upper() == " ":
            return be
        if be.upper() == "-":
            return False
#masodik()

#3.feladat
class bevasarlolista:
    def __init__(self):
        self.Név: str = str()
        self.Ár: int = int()
        self.Tömeg: int = int()

    def __str__(self) -> str:
        return "Név = {a}; Ár = {b}; Tömeg = {c}" .format(a=self.Név, b=self.Ár, c=self.Tömeg)


termek = bevasarlolista()
termek.Név = "Alma"
termek.Ár = 50
termek.Tömeg = 10

termek2 = bevasarlolista()
termek2.Név = "Kenyér"
termek2.Ár = 200
termek2.Tömeg = 100

termek3 = bevasarlolista()
termek3.Név = "Tej"
termek3.Ár = 250
termek3.Tömeg = 200

lista: List[bevasarlolista] = list()
lista.append(termek)

print(termek)
print(termek2)
print(termek3)
print("Összeg:")
print(termek.Ár+termek2.Ár+termek3.Ár)