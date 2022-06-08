from typing import List


class eger:
    def __init__(self):
        super().__init__()
        self.gombokszama: int = 0
        self.vizszintesgorgo: bool = False
        self.fuggolegesgorgo: bool = False
        self.gyartoneve: str = ""

    def __str__(self) -> str:
        return "Gombok száma = {a}; Van vízszintes görgő = {s}; Van függőleges görgő = {d}; Gyártó neve = {f}".format(a=self.gombokszama, s=self.vizszintesgorgo, d=self.fuggolegesgorgo, f=self.gyartoneve)


eger1 = eger()
eger1.gombokszama = 3
eger1.vizszintesgorgo = False
eger1.fuggolegesgorgo = True
eger1.gyartoneve = "Genius"

eger2 = eger()
eger2.gombokszama = 5
eger2.vizszintesgorgo = True
eger2.fuggolegesgorgo = True
eger2.gyartoneve = "Logitech"

eger3 = eger()
eger3.gombokszama = 7
eger3.vizszintesgorgo = True
eger3.fuggolegesgorgo = True
eger3.gyartoneve = "Trust"


egerlista = eger

lista: List['egerlista'] = list()

lista.append(eger1)
lista.append(eger2)
lista.append(eger3)

for i in lista:
    print(i)
