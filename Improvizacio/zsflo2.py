import random
from random import randint

#1
szam1=int(input("kérek egy számot:"))
szam2=int(input("kérek egy számot:"))
szam3=int(input("kérek egy számot:"))
szamok = [szam1, szam2, szam3]
print("legnagyobb szam:", max(szamok))

#2
lista = [51,52,234,34,5,1]
atlag = sum(lista) / len(lista)
print("átlag", atlag)
for i in lista:
    if i < atlag:
        print("átlagnál kisebb:", i)

#3
def veletlen(start, end, db):
    listaa = []
    for i in range(db):
        listaa.append(random.randint(start, end))
    return listaa

db = 90
start = 1
end = 90
#print(veletlen(start, end, db))
elsoot = lista[0:5]
print("elso ot szam a listabol:",elsoot)

#4
while True:
    ertek = int(input('kerek egy szamot:'))
    if (ertek % 21 == 0):
        break
