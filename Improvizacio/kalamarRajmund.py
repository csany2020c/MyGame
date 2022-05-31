from typing import List
import os

class Focilabda():

    def __init__(self) -> None:
        super().__init__()

        self.labda_szine:str = str()
        self.labda_merete:int = int()
        self.felvanefujva:bool = bool()
        self.kg:float = 0.0

    def __str__(self) -> str:
        return "Labda szine = {a}; Labda mérete = {b}; Labda felvan-e fújva {c}; Labda súlya = {d}; " .format(a = self.labda_szine, b = self.labda_merete, c = self.felvanefujva, d = self.kg)

def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I":
            return True
        if be.upper() == "N":
            return False

def intbeolvas(prompt: str , min: int = 0, max: int = 5) -> int:
    while True:
        be:str = input(prompt + " 0 - 5")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

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
saller.kg= intbeolvas("Hány kg a laszti?")
saller.labda_merete = intbeolvas("Labda mérete:")
saller.labda_szine:str = str(input("Milyen a labda színe?"))
saller.felvanefujva = boolbeolvas("Fel van fújva?")


lista:List['Focilabda'] = list()
lista.append(saller)
lista.append(puma)
lista.append(adidas)
lista.append(nike)


fn = "nemuuuugy.txt"


fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    a = Focilabda()
    a.labda_szine = sorok[i]
    i += 1
    a.labda_kg = sorok[i]
    i += 1
    a.felvanefujva = strtobool(sorok[i])
    i += 1
    a.labda_merete = sorok[i]
    i += 1
    lista.append(a)
fr.close()

print(a)

# print("-------")
# for i in lista:
#     print(i)


 # os.remove(fn)
# f = open(fn, mode="w", encoding="utf-8")
# for i in lista:
#     f.write(i.__str__() + "\n")
# f.close()