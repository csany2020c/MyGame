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

print(MyMotor)

#hf:még két osztály létrehozása és kirása