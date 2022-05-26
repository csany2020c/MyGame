from typing import List
from typing import TextIO


class Iphone:
    def __init__(self):
        super().__init__()
        self.nev = str
        self.szallitasiido = int
        self.szallitasikoltseg = int
        self.ar = int
        self.szin = str
        self.kapacitas = int

    def __str__(self) -> str:
        return "nev = {x}; szallitasiido = {y}; szallitasikoltseg = {z}; ar = {a}; szin = {b}; kapacitas = {k}".format(x=self.nev, y=self.szallitasiido, z=self.szallitasikoltseg, a=self.ar, b=self.szin, k=self.kapacitas)



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

print(myIphone)
print(myIphone2)
print(myIphone3)