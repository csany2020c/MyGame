from typing import List
import os

class Iphone:
    def __init__(self) -> None:
        super().__init__()
        self.szallitasiido = int
        self.szallitasikoltseg = int
        self.ar = int
        self.szin: str = ""
        self.kapacitas = int
        #self.eredetiar = int
        self.hasznalhato: bool = True

    def __str__(self) -> str:
        return str(self.szallitasiido) + "\n" + str(self.szallitasikoltseg) + "\n" + str(self.ar) + "\n" + self.szin + "\n" + str(self.kapacitas) + "\n" + str(self.hasznalhato) + "\n" + str(self.ar)

   #def __str__(self) -> str:
     #   return "szallitasiido = {y}; szallitasikoltseg = {z}; ar = {a}; szin = {b}; kapacitas = {k}".format(y=self.szallitasiido, z=self.szallitasikoltseg, a=self.ar, b=self.szin, k=self.kapacitas)

def strtobool(value: str) -> bool:
    if value.upper() == "Igen" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "Nem" or value.upper() == "FALSE":
        return False
    return None
def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False
def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
            else:
                print("Hibás érték! Nem az intervallumba tartozó szám!")
        except:
            print("Hibás érték! Számot kérek!")
myIphone = Iphone()
myIphone.szallitasiido = 28
myIphone.szalitasikoltseg = 5000
myIphone.ar = 235000
myIphone.szin = "fekete"
myIphone.kapacitas = 64
myIphone.hasznalhato = True

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



myIphone = Iphone()
myIphone.szallitasiido = intbeolvas("Kérem a szállítási időt: ", 1, 44)
myIphone.szalitasikoltseg= intbeolvas("Kérem a szállítási költséget: ",1000, 10000 )
myIphone.ar = intbeolvas("Kérem a telefon árát: ", 20000, 999999999)
myIphone.szin = input("Kérem a telefonszínét")
myIphone.hasznalhato = boolbeolvas("Használható a telefon?: ")
#print(myIphone)
lista: List[Iphone] = list()
lista.append(myIphone)
lista.append(myIphone2)
lista.append(myIphone3)

for i in lista:
    print(i)
