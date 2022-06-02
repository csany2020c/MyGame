from typing import List

class Rendeles:


    def __init__(self) -> None:
        super().__init__()
        self.termeknev: str="asd"
        self.ar: int
        self.szallitasikoltseg: int
        self.kiszallitasiido: int
        self.elektromos: bool

    def __str__(self) -> str:
        return "Termék neve: {a}; Ár: {b}; Szalltási Költség: {c};  Kiszallítási idő: {d};  Elektromos: {e}".format(a=self.termeknev,b=self.ar,c=self.szallitasikoltseg,d=self.kiszallitasiido,e=self.elektromos)
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


termek1 = Rendeles()
termek1.termeknev = "Szemüveg"
termek1.ar = 6127
termek1.szallitasikoltseg = 555
termek1.kiszallitasiido = 30
termek1.szin = "fekete"
termek1.suly = 24
termek1.elektromos = False

termek2 = Rendeles()
termek2.termeknev = "Telefon"
termek2.ar = 101709
termek2.szallitasikoltseg = 0
termek2.kiszallitasiido = 30
termek2.akummlator = 5000
termek2.screen = 6.43
termek2.elektromos = False

termek3 = Rendeles()
termek3.termeknev = "Hangszoró"
termek3.ar = 5827
termek3.szallitasikoltseg = 1638
termek3.kiszallitasiido = 15
termek3.vizallosag = True
termek3.bluetoothversion = 5.0
termek3.elektromos = True

termek4 = Rendeles()
termek4.termeknev = "Drón"
termek4.ar = 59242
termek4.szallitasikoltseg = 0
termek4.kiszallitasiido = 60
termek4.zoom = "50x"
termek4.remotecontroldistance = 1200
termek4.elektromos = True

termek5 = Rendeles()
termek5.termeknev = "Okos Óra"
termek5.ar = 21863
termek5.szallitasikoltseg = 0
termek5.kiszallitasiido = 85
termek5.type = "Lithium polymer"
termek5.chargingtime = 2
termek5.elektromos = True

Termeklista: List['Rendeles'] = list()
Termeklista.append(termek1)
Termeklista.append(termek2)
Termeklista.append(termek3)
Termeklista.append(termek4)
Termeklista.append(termek5)

x = Rendeles()
x.termeknev = input("Kérem a termék nevét: ")
x.ar = intbeolvas("Kérem a termék árát: ", 5000, 999999)
x.szallitasikoltseg = intbeolvas("Kérem a termék szálltási költségét: ", 250, 10000)
x.kiszallitasiido = intbeolvas("Kérem a termék kiszálltási idejét: ",0, 250)
x.elektromos = boolbeolvas("A termék elektromos-e?: ")
Termeklista.append(x)

print(len(Termeklista))

Termeklista.remove(termek1)
print("Lista elemei:")
for i in Termeklista:
    print(i)

















