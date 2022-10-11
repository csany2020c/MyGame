from typing import List

szam: List['int'] = list()
szam1: int = int(input("Kerek egy számot:"))
szam2: int = int(input("Kerek egy számot:"))
#print(min(szam1, szam2))

for i in range(min(szam1 + 1, szam2 + 1)):
    print(i)


print("2.feladat")

szamok: List['int'] = list()
while True:
      valami: int = int(input("Kérek egy számot:"))
      if valami < 0:
        #print(szamok)
         break

print("3.feladat")
class Termekek:
    def __init__(self):
        super().__init__()
        self.nev: str = ""
        self.ar: int = 0
        self.tomeg: int = 0

    def __str__(self):
        return "nev = {n}, ar = {a}, tomeg = {t}".format(n=self.nev, a=self.ar, t=self.tomeg)


termek: List['int'] = list()
t = Termekek()
t.nev = "csoki"
t.ar = 500
t.tomeg = 100

t2 = Termekek()
t2.ar = 150
t2.nev = "fank"
t2.tomeg = 50

t3 = Termekek()
t3.ar = 300
t3.nev = "kenyer"
t3.tomeg = 1000

termek.append(t)
termek.append(t2)
termek.append(t3)
for i in termek:
    print(i)

osszeg = 0
osszeg += t.ar + t2.ar + t3.ar
print(osszeg)
Termekek()

