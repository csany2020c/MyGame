class Roller:
    def __init__(self):
        super().__init__()
        self.sebesseg: int = 25
        self.szin: str ="fekete"
        self.osszecsukhatos: bool = True
        self.ferohely: int = 1
        self.elektromos: bool = False

class Sajatroller:
    def __init__(self):
        super().__init__()
        rollerasd = Roller()
        rollerasd.ferohely = 2
        rollerasd.szin ="zold"
        rollerosszes = rollerasd.szin, rollerasd.ferohely, rollerasd.sebesseg

        print(rollerosszes)
        print(rollerasd.szin)

Sajatroller()

#HF: még 2 osztály ugyan ide és pár példányt


