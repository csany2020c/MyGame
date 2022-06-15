from typing import List
#1.feladat
#egy = int(input("Kérem az első számot:"))
#ketto = int(input("Kérem a második számot:"))
#def ja(min = int, max = int):
    #if egy == min:
        #ketto == max
    #if ketto == min:
        #egy == max


#ja()



#2.feladat
#listx = []
#while True:
#    szamok = input("Kérek egy számot:")
#
#    if szamok == -1:
#        break




#3.feladat
class belista:
    def __init__(self):
        self.nev= str
        self.ar = int
        self.tomeg = int

    def __str__(self):
        return "Neve: {a} Ára: {b} Tömege: {c}".format(a=self.nev, b=self.ar, c=self.tomeg)

lista = []

asd = belista()
asd.nev = "Tej"
asd.ar = 500 #FT
asd.tomeg = 0.5 #l

asd2 = belista()
asd2.nev = "Fanta"
asd2.ar = 400
asd2.tomeg = 0.5

asd3 = belista()
asd3.nev = "Papucs"
asd3.ar = 2000#ft
asd3.tomeg = 1#dkg


lista.append(asd)
lista.append(asd2)
lista.append(asd3)


dgdf : int = 0
for i in lista:
    dgdf = dgdf.ar + i.ar
    print(dgdf)
