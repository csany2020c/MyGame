from typing import List

class Iphone:
    def __init__(self) -> None:
        #super().__init__()
        self.szallitasiido = int
        self.szallitasikoltseg = int
        self.ar = int
        self.szin = str
        self.kapacitas = int
        self.eredetiar = int
    def __str__(self) -> str:
        return "szallitasiido = {y}; szallitasikoltseg = {z}; ar = {a}; szin = {b}; kapacitas = {k}".format(y=self.szallitasiido, z=self.szallitasikoltseg, a=self.ar, b=self.szin, k=self.kapacitas)



myIphone = Iphone()
myIphone.szallitasiido = 28
myIphone.szalitasikoltseg = 5000
myIphone.ar = 235000
myIphone.szin = "fekete"
myIphone.kapacitas = 64


myIphone2 = Iphone()
myIphone2.szallitasiido = 28
myIphone2.szalitasikoltseg = 0
myIphone2.ar = 413000
myIphone2.szin = "fehér"
myIphone2.kapacitas = 128

myIphone3 = Iphone()
myIphone3.szallitasiido = 28
myIphone3.szalitasikoltseg = 0
myIphone3.ar = 118000
myIphone3.szin = "szürke"
myIphone3.kapacitas = 64

def osszeg(self) -> int:

#print(myIphone)
#print(myIphone2)
#print(myIphone3)


lista: List[Iphone] = list()
lista.append(myIphone)
lista.append(myIphone2)
lista.append(myIphone3)

for i in lista:
    print(i)
