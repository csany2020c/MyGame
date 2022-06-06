
class Dolgozatok:

    def __init__(self) -> None:
        super().__init__()
        self.maxpont: int = 0
        self.sajatpont: int = 0
        self.jegy: int = 0

    def szazalekok(self) -> int:
        return self.sajatpont / self.maxpont * 100

    def mijegy(self) -> int:
     if self.szazalekok() >= 0 and self.szazalekok() <= 25:
        a.jegy += 1

     if self.szazalekok() >= 26 and self.szazalekok() <= 40:
        a.jegy += 2

     if self.szazalekok() >= 41 and self.szazalekok() <= 60:
        a.jegy += 3

     if self.szazalekok() >= 61 and self.szazalekok() <= 80:
        a.jegy += 4

     if self.szazalekok() >= 81 and self.szazalekok() <= 100:
        a.jegy += 5




    def __str__(self) -> str:
        return "Maximális pontszám: {x}, Elért pontszám: {y}, Elért százalék: {c}%".format(x = self.maxpont, y = self.sajatpont, c = self.szazalek)

a = Dolgozatok()
a.maxpont = int(input("Maximális pontszám: "))
a.sajatpont = int(input("Elért ponrszám: "))
a.szazalek = (a.szazalekok())
a.jegy = (a.mijegy())

#if a.szazalekok() >= 0 and a.szazalekok() <= 25:
#    a.jegy += 1
#
#if a.szazalekok() >= 26 and a.szazalekok() <= 40:
#    a.jegy += 2
#
#if a.szazalekok() >= 41 and a.szazalekok() <= 60:
#    a.jegy += 3
#
#if a.szazalekok() >= 61 and a.szazalekok() <= 80:
#    a.jegy += 4
#
#if a.szazalekok() >= 81 and a.szazalekok() <= 100:
#    a.jegy += 5

print(a)



