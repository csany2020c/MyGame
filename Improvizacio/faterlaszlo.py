from typing import List

class jatek:
    def __init__(self):
        super().__init__()
        self.jatekneve: str = [0]
        self.tetszett: str = [1]
        self.hanyora: int = [2]
        self.ajanl: str = [3]
        # print(self.jatekneve, self.tetszett, str(self.hanyora), self.ajanl)

    # def __str__(self) -> str:
    #     return f"Játék neve = {a} Vélemény = {b}{}{}"


# jatek()

elso = jatek()
elso.jatekneve = "Need for speed"
elso.tetszett = "Nem"
elso.hanyora = 12
elso.ajanl = "Igen"
print(elso.jatekneve)

masodik = jatek()
masodik.jatekneve = "Valami más"
masodik.tetszett = "Nem"
masodik.hanyora = 13
masodik.ajanl = "Igen"
print(masodik.jatekneve)

lista: List['jatek'] = list()
lista.append(masodik)
lista.append(elso)
for i in lista:
    print(i)


# class elment():
#     def __init__(self):
#         super().__init__()
#         self.jatekneve = "Need for speed"
#         self.tetszett = "Nem"
#         if self.tetszett == "Nem" or self.tetszett == "NEM":
#             print("Próbálj ki másik játékot")
#         self.hanyora = 12
#         self.ajanl = "Igen"
#         print(self.jatekneve, self.tetszett, self.hanyora, self.ajanl)
#
# elment()
#



class valtozos(jatek):
    def __init__(self):
        super().__init__()
        a = True
        while a == True:
            self.jatekneve: str = str(input("ELső: "))
            self.tetszett: str = str(input("MÁsodik:"))
            self.hanyora: int = int(input("HArmadik:"))
            self.ajanl: str = str(input("NEgyedik:"))

            lista: List['str'] = list()
            bobbyka = self.jatekneve, self.tetszett, str(self.hanyora), self.ajanl

            lista.append(bobbyka)

            if input("KIdob=") == "i":
                a = False

        for i in lista:
            print(i)


valtozos()


