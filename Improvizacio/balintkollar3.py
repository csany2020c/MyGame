class Dolgozat:
    def __init__(self) -> None:
        super().__init__()
        self.max: int = 0
        self.sajat: int = 0

    def szazalekokfuggveny(self):
        return (self.sajat / self.max) * 100


x = Dolgozat()
x.max = int(input("A maximum pontszám: "))
x.sajat = int(input("Elér pontszám: "))
x.szazalek = (x.sajat / x.max) * 100
print("Elért százalék {a}%".format(a=x.szazalek))
print("Elért százalék fügvénnyel {a}%".format(a=x.szazalekokfuggveny()))





