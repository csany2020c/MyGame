from typing import List

print("1.feladat")
print("")
szam1: int = int(input())
szam2: int = int(input())
if szam1 < szam2:
    print(szam1)
    x = 0
    for i in range(szam1 + 1):
        eredmeny = x + i
        print(eredmeny)
else:
    print(szam2)
    y = 0
    for i in range(szam2 + 1):
        eredmeny = y + i
        print(eredmeny)

if (szam1 > 0) < (szam2 > 0):
    print(szam1)
    x = 0
    for i in range(szam1 + 1):
        eredmeny = x - i
        print(eredmeny)

if (szam1 > 0) > (szam2 > 0):
    print(szam2)
    x = 0
    for i in range(szam2 + 1):
        eredmeny = x - i
        print(eredmeny)

print("")
print("2.feladat")
print("")

szamlista: List['int'] = list()

while True:
    szam3: int = int(input("Kérek egy számot:"))
    if szam3 < 0:
        break
    else:
        szamlista.append(szam3)
print(min(szamlista),max(szamlista))

print("")
print("3.feladat")
print("")

class bevasarlolista:
    def __init__(self):
        super().__init__()
        self.nev: str = str
        self.ar:int = int
        self.tomeg:int = int

    def __str__(self):
        return "Név = {a};Ár = {b};Tömeg = {c}".format(a=self.nev,b=self.ar,c=self.tomeg)

bevasarlolistam1=bevasarlolista()
bevasarlolistam1.nev = "Tej"
bevasarlolistam1.ar = 500
bevasarlolistam1.tomeg = 1

bevasarlolistam2=bevasarlolista()
bevasarlolistam2.nev = "Kenyér"
bevasarlolistam2.ar = 300
bevasarlolistam2.tomeg = 0,5

bevasarlolistam3=bevasarlolista()
bevasarlolistam3.nev = "Burgonya"
bevasarlolistam3.ar = 600
bevasarlolistam3.tomeg = 3

termeklista : List[bevasarlolista] = list()
termeklista.append(bevasarlolistam1)
termeklista.append(bevasarlolistam2)
termeklista.append(bevasarlolistam3)

for i in termeklista:
    print(i)

print(" ")
print("Árak összege:")
print(bevasarlolistam1.ar+bevasarlolistam2.ar+bevasarlolistam3.ar)









