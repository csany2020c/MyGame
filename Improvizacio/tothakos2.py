from typing import List

class Motor:
    def __init__(self) -> None:
        super().__init__()
        self.Gyarto: str = str()
        self.Tipus: str = str()
        self.Kobcenti: int = int()
        self.Szin: str = str()
        self.Loero: int = int()
        self.Valto: bool = bool()
        self.Szallitasiido: int = int
        self.Szallitasikoltseg: int = int
        self.Ar: int = int

    def teljesar(self) -> int:
        return self.Ar + self.Szallitasikoltseg

    def __str__(self) -> str:
        return "Gyarto = {a}; Tipus = {b}; Kobcenti = {c}; Szin = {d}; Loero = {e}; Valto = {f}; Szallitasiido = {g}; Szallitasikoltseg = {h}; ar = {i}".format(a=self.Gyarto, b=self.Tipus, c=self.Kobcenti, d=self.Szin, e=self.Loero, f=self.Valto, g=self.Szallitasiido, h=self.Szallitasikoltseg, i=self.Ar)

    def strtobool(value: str) -> bool:
        if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
            return True
        if value.upper() == "N" or value.upper() == "FALSE":
            return False
        return None

    def boolbeolvas(prompt: str) -> bool:
        while True:
            be: str = input(prompt + "(I/N):")
            if be.upper() == "I" or be.upper() == "Y":
                return True
            if be.upper() == "N":
                return False

    def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
        while True:
            be: str = input(prompt + "(" + str(min) + "-" + str(max) + "):")
            try:
                i: int = int(be)
                if i >= min and i <= max:
                    return i
                else:
                    print("Hibás érték! Nem az intervallumba tartozó szám!")
            except:
                print("Hibás érték! Számot kérek!")

motor = Motor()
motor.Gyarto = "KTM"
motor.Tipus = "Duke"
motor.Kobcenti = 125
motor.Szin = "Fekete"
motor.Loero = 15
motor.Valto = True
motor.Szallitasiido = 5
motor.Szallitasikoltseg = 5000
motor.Ar = 1500000

motor2 = Motor()
motor2.Gyarto = "Yamaha"
motor2.Tipus = "MT-125"
motor2.Kobcenti = 125
motor2.Szin = "Kék"
motor2.Loero = 15
motor2.Valto = True
motor2.Szallitasiido = 5
motor2.Szallitasikoltseg = 10000
motor2.Ar = 2000000

motor3 = Motor()
motor3.Gyarto = "Suzuki"
motor3.Tipus = "GSX-R"
motor3.Kobcenti = 1000
motor3.Szin = "Piros"
motor3.Loero = 30
motor3.Valto = True
motor3.Szallitasiido = 3
motor3.Szallitasikoltseg = 15000
motor3.Ar = 5000000

#print(motor)
#print(motor2)
#print(motor3)

lista: List[Motor] = list()
lista.append(motor)
lista.append(motor2)
lista.append(motor3)

motor2.Ar = 1500000

Vasarlo = Motor()
Vasarlo.Gyarto = input("Motor márkája:")
Vasarlo.Tipus = input("Motor típusa:")
Vasarlo.Kobcenti = input("Hány köbcenti?:")
Vasarlo.Szin = input("Motor színe:")
Vasarlo.Loero = input("Hány lóerő?:")
Vasarlo.Valto = input("Váltó típusa:")
Vasarlo.Szallitasiido = input("Hány nap a szállítás?:")
Vasarlo.Szallitasikoltseg = input("Szállítási költség:")
Vasarlo.Ar = input("Motor ára:")
lista.append(Vasarlo)


for i in lista:
    print(i)
    print(i.teljesar())