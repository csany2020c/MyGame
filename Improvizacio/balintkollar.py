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

    def __str__(self) -> str:
        return "Méret = {a}; Szín = {b}; Pöttyökszáma = {c}; Felvanfújva = {d}".format(a=self.meret, b=self.szin, c=self.pottyokszama, d=self.felvanfujva)

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

        print(labdaasd)
        print("------")

SajatLabda()

labda2 = Labda()
labda2.meret = 70
labda2.szin = "feher"
labda2.pottyokszama = 0
labda2.felvanfujva = False
print(labda2)
print("------")

class Teve:
    def __init__(self):
        super().__init__()
        self.magassag: int = 200
        self.szin: str ="barna"
        self.nosteny: bool = True
        self.pupokszama: int = 2
        self.fajta: str ="2-pupu"

    def __str__(self) -> str:
        return "Magasság = {a}; Szín = {b}; Nöstény = {c}; Púpokszáma = {d}; Fajtája = {e}".format(a=self.magassag,b=self.szin,c=self.nosteny,d=self.pupokszama,e=self.fajta)

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

        print(teveasd)

SajatTeve()

teve2 = Teve()
teve2.pupokszama = 2
teve2.magassag = 190
teve2.szin = "foltos"
teve2.nosteny = False
print(teve2)

teve3 = Teve()
teve3.pupokszama =0
teve3.magassag = 185
teve3.szin = "fekete"
teve3.nosteny = True
teve3.fajta = "0-pupu"
print(teve3)

teve4 = Teve()
teve4.magassag = int(input("Kérem adja meg a magasságot: "))
teve4.szin = str(input("Kérem adja meg a színét: "))
teve4.nosteny = str(input("Kérem adja meg, hogy nöstény-e?(True or False): "))
if teve4.nosteny == "True" or teve4.nosteny == "False":
    pass
else:
    quit()
teve4.fajta = str(input("Kérem adja meg a fajtáját: "))
print(teve4)








