from typing import List, TextIO

class Motor:
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = str
        self.kobcenti: int = int
        self.vegsebesseg: int = int
        self.valto: bool
        self.hp: int = int

MyMotor = Motor()
MyMotor.gyarto = "Husqvarna"
MyMotor.kobcenti = 701
MyMotor.vegsebesseg = 200
MyMotor.valto = True
MyMotor.hp = 74

print(MyMotor.hp)

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

print(MyBicikli.csomagtarto)
print(MyBicikli.gyarto)



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

print(MyBukosisak.tipus)
print(MyBukosisak.meret)
print(MyBukosisak.szemuveg)