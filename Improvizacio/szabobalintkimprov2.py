from typing import List
import os

class AliExpress:

    def __init__(self) -> None:
        super().__init__()
        self.hangszer : str = ""
        self.vankolts: bool = True
        self.szallkolts : int =0
        self.ar: int = 0
        self.szallido: int = 0
        self.honnanjon: str = ""

    def teljesar(self) -> int:
        return self.ar + self.szallkolts

    def __str__(self) -> str:
        return "Tárgy : {a}, Van kiszállítási díj : {b}, Szállítási költség = {c}, Ár : {d} Ft, Kiszállítási idő : {e} hónap, Innen érkezik : {f}".format(a = self.hangszer, b = self.vankolts, c = self.szallkolts, d = self.ar, e = self. szallido, f = self.honnanjon)

def strtobool(value: str) -> bool:
        if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
            return True
        if value.upper() == "N" or value.upper() == "FALSE":
            return False
        return None

def boolbeolvas(prompt: str) -> bool:
        while True:
            be: str = input(prompt + " (I/N): ")
            if be.upper() == "I" or be.upper() == "Y":
                return True
            if be.upper() == "N":
                return False

def intbeolvas(prompt: str, min: int = 0, max: int = 1000000) -> int:
        while True:
            be: str = input(prompt)
            try:
                i: int = int(be)
                if i >= min and i <= max:
                    return i
            except:
                pass

def haigaz(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False


#AliExpress()

while boolbeolvas("Szeretne rendelést felvinni?"):
   a = AliExpress()
   a.hangszer = input("A hangszer fajtája: ")
   a.szallido = intbeolvas("Kérem a kiszállítási idejét ( napokban ): ")
   a.honnanjon = input("Honnan szállítják?: ")
   a.ar = intbeolvas("Kérem a termék árát ( Ft ): ")
   a.vankolts = haigaz("Van kiszállítási költsége?: ")

   if a.vankolts:
    a.szallkolts = intbeolvas("A kiszállítási díj: ")

dob = AliExpress()
dob.hangszer = "Dobkészlet"
dob.vankolts = True
dob.ar = 24330
dob.szallkolts = 34941
dob.szallido = 3
dob.honnanjon = "Kína"

klarinet = AliExpress()
klarinet.hangszer = "Klarinét bambusz kiegészítő"
klarinet.vankolts = False
klarinet.ar = 1145
klarinet.szallido = 3.5
klarinet.honnanjon = "Kanada"

hegedu = AliExpress()
hegedu.hangszer = "Hegedű"
hegedu.vankolts = True
hegedu.ar = 178669
hegedu.szallkolts = 17630
hegedu.szallido = 3
hegedu.honnanjon = "Ismeretlen"

#print(dob)
#print(klarinet)
#print(hegedu)


list = AliExpress()
lista: list = []
lista.append(a)
#lista.append(dob)
#lista.append(klarinet)
#lista.append(hegedu)

#print(lista)
print("")
print("")
print("")
for i in lista:
    print(i)
    print("Teljes ára:", i.teljesar())
