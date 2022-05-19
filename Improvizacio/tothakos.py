from typing import List

class Motor:
    def __init__(self):
        self.Gyárto: str = str()
        self.Típus: str = str()
        self.Köbcenti: int = int()
        self.Szín: str = str()
        self.Lóerő: int = int()
        self.Váltó: bool = bool()

    def __str__(self) -> str:
        return "Gyártó = {a}; Típus = {b}; Köbcenti = {c}; Szín = {d}; Lóerő = {e}; Váltó = {f}".format(a=self.Gyárto, b=self.Típus, c=self.Köbcenti, d=self.Szín, e=self.Lóerő, f=self.Váltó)


motor = Motor()
motor.Gyárto = "KTM"
motor.Típus = "Duke"
motor.Köbcenti = 125
motor.Szín = "Fekete"
motor.Lóerő = 15
motor.Váltó = True

motor2 = Motor()
motor2.Gyárto = "Yamaha"
motor2.Típus = "MT-125"
motor2.Köbcenti = 125
motor2.Szín = "Kék"
motor2.Lóerő = 15
motor2.Váltó = True

motor3 = Motor()
motor3.Gyárto = input("Motor gyártója:")
motor3.Típus = input("Motor típusa:")
motor3.Köbcenti = input("Köbcenti:")
motor3.Szín = input("Motor színe:")
motor3.Lóerő = input("Lóerő:")
valto = input("Váltós? (I/N):")
if valto == "I":
    motor3.Váltó = True
if valto == "N":
    motor3.Váltó = False




#print(motor)
#print(motor2)
print(motor3)

#hf: +2osztály létrehozása, kirása

class Csuka:
    def __init__(self):
        self.Gyártó: str = str()
        self.Típus: str = str()
        self.Méret: int = int()
        self.Stopli: str = str()

    def __str__(self) -> str:
        return "Gyártó = {a}; Típus = {b}; Méret = {c}; Stopli = {d}".format(a=self.Gyártó, b=self.Típus, c=self.Méret, d=self.Stopli)


csuka = Csuka()
csuka.Gyártó = "Adidas"
csuka.Típus = "Predator"
csuka.Méret = 42
csuka.Stopli = "Fém"

csuka2 = Csuka()
csuka2.Gyártó = "Nike"
csuka2.Típus = "Superfly"
csuka2.Méret = 43
csuka2.Stopli = "Gumi"

#print(csuka)
#print(csuka2)