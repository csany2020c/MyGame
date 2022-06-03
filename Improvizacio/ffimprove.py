
class Dogak:
    def __init__(self) -> None:
        super().__init__()
        self.maxpont: int = 0
        self.sajatpont: int = 0

    def szazalek(self):
        return self.sajatpont / self.maxpont + 100

    def __str__(self):
        return("Maxpontszám:{b} Sajátpontszám: {c} Szazalek {d}" .format(b = self.maxpont, c = self.sajatpont, d = self.szazalek))
a = Dogak()
a.maxpont: int(input("Kérem a maxpontszámot:"))
a.sajatpont: int(input("Kérem az elért pontszámot:"))
a.szazalek