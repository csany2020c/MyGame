from typing import List


class Improvizacio:

    def __int__(self):
        super().__init__()
        self.size: int = 0
        self.color: str = "None"
        self.weight: int = 0
        self.hasznos: bool = False


peldany1 = Improvizacio()
peldany1.size = 50
peldany1.color = "Blue"
peldany1.weight = 20
peldany1.hasznos = True

peldany2 = Improvizacio()
peldany2.size = 20
peldany2.color = "Red"
peldany2.weight = 60
peldany2.hasznos = False

peldany3 = Improvizacio()
peldany3.size = 120
peldany3.color = "Black"
peldany3.weight = 7
peldany3.hasznos = True

peldany4 = Improvizacio()
peldany4.size = input("Kérem a méretet: ")
peldany4.color = input("Kérem a színt: ")
peldany4.weight = input("Kérem a súlyt: ")
peldany4.hasznos = input("Kérem hogy hasznos-e: ")

lista: List[Improvizacio] = list()
lista.append(peldany1)
lista.append(peldany2)
lista.append(peldany3)
lista.append(peldany4)

for i in range(len(lista)):
    print(lista[i].size)
    print(lista[i].color)
    print(lista[i].hasznos)
    print(lista[i].weight)







