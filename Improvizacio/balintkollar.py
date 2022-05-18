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

        print("Roller:")
        print(rollerosszes)
        print(rollerasd.szin)
        print("------")

Sajatroller()

class Labda:
    def __init__(self):
        super().__init__()
        self.meret: int = 50
        self.szin: str = "pottyos"
        self.pottyokszama: int = 0
        self.felvanfujva: bool = True

class SajatLabda:
    def __init__(self):
        super().__init__()
        labdaasd = Labda()
        labdaasd.pottyokszama = 6
        labdaasd.szin ="nempottyos"

        print("Labda:")

        if labdaasd.szin =="pottyos":
            print(labdaasd.pottyokszama, labdaasd.szin)
        else:
            print("A labda nem pöttyös")
        print("------")

SajatLabda()


class Teve:
    def __init__(self):
        super().__init__()
        self.magassag: int = 200
        self.szin: str ="barna"
        self.nosteny: bool = True
        self.pupokszama: int = 2
        self.fajta: str ="2-pupu"

class SajatTeve:
    def __init__(self):
        super().__init__()
        teveasd = Teve()
        teveasd.pupokszama = 1
        teveasd.magassag = 180

        if teveasd.pupokszama == 1:
            teveasd.fajta="1-pupu"
        else:
            teveasd.fajta="2-pupu"

        print("Teve:")
        print(teveasd.fajta)
        print("------")

SajatTeve()



