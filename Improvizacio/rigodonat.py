from typing import List, TextIO

class Motor:
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = str
        self.kobcenti: int = int
        self.vegsebesseg: int = int
        self.valto: bool
        self.hp: int = int

    def __str__(self) -> str:
        return "Gyarto = {a}; Kobcenti = {b}; Vegsebesseg = {c}; Valto = {d}; Hp = {e}".format(a=self.gyarto, b=self.kobcenti, c=self.vegsebesseg, d=self.valto, e=self.hp)


MyMotor = Motor()
MyMotor.gyarto = "Husqvarna 701 Supermoto"
MyMotor.kobcenti = 701
MyMotor.vegsebesseg = 200
MyMotor.valto = True
MyMotor.hp = 74

MyMotor2 = Motor()
MyMotor2.gyarto = "KTM 1290 Super Duke"
MyMotor2.kobcenti = 1290
MyMotor2.vegsebesseg = 289
MyMotor2.valto = True
MyMotor2.hp = 180

MyMotor3 = Motor()
MyMotor3.gyarto = "Honda Africa Twin"
MyMotor3.kobcenti = 1084
MyMotor3.vegsebesseg = 214
MyMotor3.valto = False
MyMotor3.hp = 101

MyMotorFelhasznalo = Motor()
MyMotorFelhasznalo.gyarto = input("Kérem a motor gyartojat:")
MyMotorFelhasznalo.kobcenti = input("Mennyi a hengerűrtartalma(ccm):")
MyMotorFelhasznalo.vegsebesseg = input("Mennyi a motor vegsebessege(km/h):")
Valtose = input("Automata váltós vagy manuális(A/M):")
if Valtose == "M":
    MyMotorFelhasznalo.valto = True
if Valtose == "A":
    MyMotorFelhasznalo.valto = False
MyMotorFelhasznalo.hp = input("Mennyi lóerős a motorkerékpár(hp):")

#print(MyMotor.hp)
print(MyMotor)
print(MyMotor2)
print(MyMotor3)
print(MyMotorFelhasznalo)


#hf:még két osztály létrehozása és kirása



class bicikli:
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = str
        self.sebessegbaltofkozatszam: int = int
        self.kerekmeret: int = int
        self.csomagtarto: bool


MyBicikli = bicikli()
MyBicikli.gyarto = "KTM"
MyBicikli.sebessegbaltofkozatszam = 24
MyBicikli.kerekmeret = 28
MyBicikli.csomagtarto = False

#print(MyBicikli.csomagtarto)
#print(MyBicikli.gyarto)



class bukosisak:
    def __init__(self):
        self.gyarto: str = str
        self.szemuveg: bool
        self.tipus: str = str
        self.meret: int = int

MyBukosisak = bukosisak()
MyBukosisak.gyarto = "Thor"
MyBukosisak.szemuveg = True
MyBukosisak.meret = 58
MyBukosisak.tipus = "cross"

#print(MyBukosisak.tipus)
#print(MyBukosisak.meret)
#print(MyBukosisak.szemuveg)


