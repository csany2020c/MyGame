class Piano:
    def __init__(self):
        super().__init__()
        self.brand: str = ""
        self.value: int = 0
        self.year: int = 0
        self.wood: str = ""

    def __str__(self) -> str:
        return "{b}; {v}; {y}; {w}".format(b=self.brand, v=self.value, y=self.year, w=self.wood)


lista: list = []
a = Piano()
b = Piano()
c = Piano()
d = Piano()
a.brand = "Kawai"
b.brand = "Yamaha"
c.brand = "Steinway"
d.brand = input()
a.value = 525
b.value = 679
c.value = 1500
d.value = input()
a.year = 2013
b.year = 1956
c.year = 1893
d.year = input()
a.wood = "Mahagóni"
b.wood = "Tölgy"
c.wood = "Fenyő"
d.wood = input()
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
for i in range(len(lista)):
    print(lista[i])
