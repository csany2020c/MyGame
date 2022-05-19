from typing import List

class Motor:
    def __init__(self):
        self.gyarto: str = str()
        self.tipus: str = str()
        self.kobcenti: int = int()
        self.szin: str = str()
        self.loero: int = int()
        self.valto: bool = bool()

motor = Motor()
motor.gyarto = "KTM"
motor.tipus = "Duke"
motor.kobcenti = 125
motor.szin = "Fekete"
motor.loero = 15
motor.valto = True

#hf: +2osztály létrehozása, kirása

class Csuka:
    def __init__(self):
        self.gyarto: str = str()
        self.tipus: str = str()
        self.meret: int = int()
        self.stopli: str = str()

csuka = Csuka()
csuka.gyarto = "Adidas"
csuka.tipus = "Predator"
csuka.meret = 42
csuka.stopli = "Fém"