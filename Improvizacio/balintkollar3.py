class Dolgozat:
    def __init__(self) -> None:
        super().__init__()
        self.max: int
        self.sajat: int

x = Dolgozat()
x.max = int(input("A maximum pontszám: "))
x.sajat = int(input("Elér pontszám: "))
x.szazalek = (x.sajat / x.max) * 100
print("Elér százalék {a}%".format(a=x.szazalek))





