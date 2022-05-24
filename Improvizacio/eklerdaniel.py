from typing import List
from typing import TextIO
class Deez:
    def __init__(self):
        super().__init__()
        self.aldozat = ""
        self.ido = ""
        self.fegyver = ""
        self.bunos = ""
        self.gyanusitott = ""
        #if self.bunos == True:      #print(self.gyanusitott + " Did it!!! with a " + self.fegyver + " He killed" + self.aldozat + " at" + input(3))

    def __str__(self) -> str:
        return "{a} {b} {c} {d}".format(a= self.aldozat , b= self.gyanusitott , c= self.fegyver, d=self.ido )


X = Deez()
X.aldozat = "Gary Cooper"
X.ido =  1013
X.fegyver = "Cancer"
X.bunos = True
X.gyanusitott = "Stevie Wonder"





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
# Nuts()

Y = Deez()

Lista: List['Deez'] = list()


Z = Deez()
Z.aldozat = " Zack "
Z.ido = 2145
Z.fegyver = "Kitchen knife"
Z.bunos = True
Z.gyanusitott = "Jody"
Lista.append(X)
Lista.append(Z)
for i in range (len(Lista)):
    if input() == "Z áldozat":
        print(Z.aldozat)
    if input() == "X áldozat":
        print(X.aldozat)