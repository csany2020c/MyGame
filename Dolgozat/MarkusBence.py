import random
from typing import List

class doga:

    def __init__(self) -> None:
        super().__init__()

        self.be: int = 0
        self.ki: int = 0

    def __str__(self):
        return " be = {a}, ki = {b}".format(a=self.be, b=self.ki)

b = doga()
b.be = input('2 szám:')


print(b)


class nev:
    def __init__(self):
        super(nev, self).__init__()

        self.nevek: str = str

    def __str__(self) -> str:
        return " nev = {a}".format(a=self.nev)

a = nev()
a.nevek = input('Írj egy nevet:')
a.nevek1 = input('Írj egy nevet:')
a.nevek2 = input('Írj egy nevet:')

lista:List['nev'] = list()
lista.append(a)

class eger:

    def __init__(self) -> None:
        super().__init__()

        self.gombokszama: int = 0
        self.vizszintesgo: bool = False
        self.fuggolegesgorgo: bool = False
        self.gyartoneve: str = str

    def __str__(self) -> str:
        return " gombokszama = {a}, vizszintesgorgo = {b}, fuggolegesgorgo = {c}, gyartoneve = {d},".format(a=self.gombokszama, b=self.vizszintesgorgo, c=self.fuggolegesgorgo, d=self.gyartoneve)


e = eger()
e.gombokkszama = 3
e.vizszintesgorgo = True
e.fuggolegesgorgo = False
e.gyartoneve = "Logitech"

e1 = eger()
e1.gombokkszama = 4
e1.vizszintesgorgo = False
e1.fuggolegesgorgo = True
e1.gyartoneve = "Genius"

e2 = eger()
e2.gombokkszama = 6
e2.vizszintesgorgo = True
e2.fuggolegesgorgo = True
e2.gyartoneve = "Samsung"


lista:List['eger'] = list()
lista.append(e)
lista.append(e1)
lista.append(e2)
for i in lista:
    print(i)