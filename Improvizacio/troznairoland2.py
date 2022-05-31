from typing import List

class focilabda:

    def __init__(self):
        super().__init__()
        self.szin: str = ""
        self.meret: int = 0
        self.ar: int = 0
        self.hasznalat: str = ""
        self.hasznose: bool = False

lista: List['focilabda'] = list()

focilabda1 = focilabda()
focilabda1.szin = "fehér-fekete"
focilabda1.meret = 5
focilabda1.ar = 8000
focilabda1.hasznalat = "kezdő"
focilabda1.hasznose = True
lista.append(focilabda1)

focilabda2 = focilabda()
focilabda2.szin = "fehér-kék"
focilabda2.meret = 5
focilabda2.ar = 15000
focilabda2.hasznalat = "haladó"
focilabda2.hasznose = True
lista.append(focilabda2)

focilabda3 = focilabda()
focilabda3.szin = "sárga-fehér"
focilabda3.meret = 5
focilabda3.ar = 12000
focilabda3.hasznalat = "haladó"
focilabda3.hasznose = False
lista.append(focilabda3)

focilabda4 = focilabda()
focilabda4.szin = input("A labda színe:")
focilabda4.meret = input("A labda mérete:")
focilabda4.ar = input("A labda ára forintban:")
focilabda4.hasznalat = input("Megfelelő csoport:")
focilabda4.hasznose = input("Hasznos-e a labda:")
lista.append(focilabda4)
print(lista)