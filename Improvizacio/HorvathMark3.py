class Dolgozat:

    def __init__(self) -> None:
        super().__init__()
        self.max: int = 0
        self.elert: int = 0

    def szazalek(self):
        return self.elert / self.max * 100

    def erdemjegy(self):
        a.jegy = 0
        if a.szazalek() < 25:
            a.jegy = 1
        if 25 <= a.szazalek() < 40:
            a.jegy = 2
        if 30 <= a.szazalek() < 60:
            a.jegy = 3
        if 60 <= a.szazalek() < 80:
            a.jegy = 4
        if a.szazalek() >= 80:
            a.jegy = 5
        return a.jegy

a = Dolgozat()
a.max = int(input("Mennyi a maximum elérhető pontok száma? "))
a.elert = int(input("Mennyi pontot értél el? "))
print(a.szazalek())

#rint(a.jegy)
print(a.erdemjegy())