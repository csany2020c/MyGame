from typing import List

class Focilabda():

    def __init__(self) -> None:
        super().__init__()

        self.labda_szine:str = str()
        self.labda_merete:int = int()
        self.felvanefujva:bool = bool()
        self.kg:float = 0.0

    def __str__(self) -> str:
        return "Labda szine = {a}; Labda mérete = {b}; Labda felvan-e fújva {c}; Labda súlya = {d}; " .format(a = self.labda_szine, b = self.labda_merete, c = self.felvanefujva, d = self.kg)




adidas = Focilabda()
adidas.kg = 3
adidas.labda_szine = "White"
adidas.felvanefujva = True
adidas.labda_merete = 3

nike = Focilabda()
nike.kg = 1
nike.labda_szine = "Black"
nike.felvanefujva = False
nike.labda_merete = 4

puma = Focilabda()
puma.kg = 2
puma.labda_szine = "Blueberry"
puma.felvanefujva = True
puma.labda_merete = 2

saller = Focilabda()
saller.kg:int = int(input())
saller.labda_merete:int = int(input())
saller.felvanefujva = bool(input())
saller.labda_szine:str = str(input())

lista:List['Focilabda'] = list()
lista.append(saller)
lista.append(puma)
lista.append(adidas)
lista.append(nike)

while Focilabda != "":

    for i in lista:
        print(i)

        break
