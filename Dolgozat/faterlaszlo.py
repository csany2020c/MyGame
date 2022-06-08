from typing import List
from random import randint


def elsofeladat(a: int, b: int) -> int:
    for i in range(1, int(b) + 1):
        szam = i * int(a)
        print(szam)


elsofeladat(2, 3)
elsofeladat(5, 4)
elsofeladat(input("Irjon be egy szamot: "), input("Irjon be egy masik szamot: "))


def beolvas() -> List['str']:
    lista: List['str'] = list()
    while True:
        a = input("Irjon be egy nevet: ")
        if a == "":
            break
        else:
            lista.append(str(a))
    randomoscucc = randint(0, len(lista) - 1)
    print(lista[randomoscucc])
beolvas()


class Egerek:
    def __init__(self) -> None:
        super().__init__()
        self.gombokszama: int = 0
        self.vizszintesgorgo: bool = False
        self.fuggolegesgorgo: bool = False
        self.gyartoneve: str = ""

    def __str__(self):
        return f"Gombok száma = {self.gombokszama} Vízszintes görgő = {self.vizszintesgorgo} Függőleges görgő = {self.fuggolegesgorgo} Gyártó neve = {self.gyartoneve}"


ujlista: List['Egerek'] = list()

elso = Egerek()
elso.gombokszama = 2
elso.vizszintesgorgo = False
elso.fuggolegesgorgo = True
elso.gyartoneve = "Logitech"

masodik = Egerek()
masodik.gombokszama = 0
masodik.vizszintesgorgo = True
masodik.fuggolegesgorgo = True
masodik.gyartoneve = "Genius"

harmadik = Egerek()
harmadik.gombokszama = 1
harmadik.vizszintesgorgo = False
harmadik.fuggolegesgorgo = False
harmadik.gyartoneve = "Hp"

ujlista.append(elso.__str__())
ujlista.append(masodik.__str__())
ujlista.append(harmadik.__str__())

print(ujlista)




