from typing import List

# class jatek:
#     def __init__(self):
#         super().__init__()
#         self.jatekneve: str = ""
#         self.tetszett: bool = False
#         self.hanyora: int = 0
#         self.ajanl: bool = False
#         # print(self.jatekneve, self.tetszett, str(self.hanyora), self.ajanl)
#
#     # def __str__(self) -> str:
#     #     return f"Játék neve = {a} Vélemény = {b}{}{}"
#
#
# # jatek()
#
# elso = jatek()
# elso.jatekneve = "Need for speed"
# elso.tetszett = "Nem"
# elso.hanyora = 12
# elso.ajanl = "Igen"
# print(elso.jatekneve)
#
# masodik = jatek()
# masodik.jatekneve = "Valami más"
# masodik.tetszett = "Nem"
# masodik.hanyora = 13
# masodik.ajanl = "Igen"
# print(masodik.jatekneve)
#
# lista: List['jatek'] = list()
# lista.append(masodik)
# lista.append(elso)
# for i in lista:
#     print(i)
#
# # class elment():
# #     def __init__(self):
# #         super().__init__()
# #         self.jatekneve = "Need for speed"
# #         self.tetszett = "Nem"
# #         if self.tetszett == "Nem" or self.tetszett == "NEM":
# #             print("Próbálj ki másik játékot")
# #         self.hanyora = 12
# #         self.ajanl = "Igen"
# #         print(self.jatekneve, self.tetszett, self.hanyora, self.ajanl)
# #
# # elment()
#
#
#
#
# class valtozos(jatek):
#     def __init__(self):
#         super().__init__()
#         a = True
#         while a == True:
#             self.jatekneve: str = str(input("ELső: "))
#             self.tetszett: str = str(input("MÁsodik:"))
#             self.hanyora: int = int(input("HArmadik:"))
#             self.ajanl: str = str(input("NEgyedik:"))
#
#             lista: List['str'] = list()
#             bobbyka = self.jatekneve, self.tetszett, str(self.hanyora), self.ajanl
#
#             lista.append(bobbyka)
#
#             if input("KIdob=") == "i":
#                 a = False
#
#         for i in lista:
#             print(i)
#
# valtozos()


class telefon:
    def __init__(self):
        super().__init__()
        self.marka: str = ""
        self.szine: str = ""
        self.eves: float = 0
        self.mukodik: bool = False

    def __str__(self):
        return f"Márka = {self.marka}, Színe = {self.szine}, Éves = {self.eves}, Működik = {self.mukodik}"

t1 = telefon()
t1.marka = "Xiaomi"
t1.szine = "Fekete"
t1.eves = 1
t1.mukodik = False

t2 = telefon()
t2.marka = "Samsung"
t2.szine = "Feher"
t2.eves = 0.5
t2.mukodik = True

t3b = telefon()
t3b.marka = str(input("Telefon márkája: "))
t3b.szine = str(input("Telefon színe: "))
t3b.eves = int(input("Hány éves a telefon: "))
t3b.mukodik = bool(input("Működik? _True vagy False_: "))


telefonlista: List['telefon'] = list()
telefonlista.append(t1)
telefonlista.append(t2)
telefonlista.append(t3b)

for i in telefonlista:
    print(i)