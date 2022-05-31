from typing import List
from typing import TextIO
import os

class Deez:
    def __init__(self):
        super().__init__()
        self.aldozat = ""
        self.ido = ""
        self.fegyver = ""
        self.bunos = ""
        self.gyanusitott = ""
        self.gabagool: bool = True
        self.fajta = ""
        #if self.bunos == True:      #print(self.gyanusitott + " Did it!!! with a " + self.fegyver + " He killed" + self.aldozat + " at" + input(3))

    def __str__(self) -> str:
        return "{a} {b} {c} {d}".format(a= self.aldozat , b= self.gyanusitott , c= self.fegyver, d=self.ido )


X = Deez()
X.aldozat = "Gary Cooper"
X.ido =  1013
X.fegyver = "Cancer"
X.bunos = True
X.gyanusitott = "Stevie Wonder"
X.gabagool = True





# class Nuts:
#     def __init__(self):
#         super().__init__()
#         self.aldozat = " Salvador Big Pussy Salfiery "
#         self.ido  =  1530
#         self.fegyver = ".38 sub nosed"
#         self.bunos = True
#         self.gyanusitott = "Tony Soprano"
#         if self.bunos == True:
#             print(self.gyanusitott + " Did it!!! with a " + self.fegyver + " He killed" + self.aldozat + " at")
# Nuts()0

Y = Deez()
def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False
def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

Lista: List['Deez'] = list()

fn = "gabagool.txt"

# while boolbeolvas("Gabagool? "):
#
#     Z = Deez()
#
#     Z.aldozat = input("Gabagool színe")
#     Z.fajta = input("Gabagool fajtája")
#     Z.ido = int(input("Kérem a Gabagool súlyát kg-ban"))
#     Lista.append(Z)
#
# for i in Lista:
#     print(i)
# Z.bunos = True
# Z.gyanusitott = "Jody"
# Lista.append(X)
# Lista.append(Z)
# for i in range (len(Lista)):
#     if input() == "Z áldozat":
#         print(Z.aldozat)
#     if input() == "Z":
#         print(Z)
#     if input() == "X":
#         print(X)
#     if input() == "X áldozat":
#         print(X.aldozat)

f = open("gabagool.txt", mode='w')
sorok = f.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    a = Deez()
    a.szin = sorok[i]
    i += 1
    a.marka = sorok[i]
    i += 1
    a.automatavaltos = strtobool(sorok[i])
    i += 1
    a.ar = int(sorok[i])
    i += 1
    Lista.append(a)
f.close()




print("_______")

for i in Lista:
    print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in Lista:
    f.write(i.__str__() + "\n")
f.close()