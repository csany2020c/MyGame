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
lista2: list = []
lista3: list = []
lista4: list = []
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
lista2.append(b)
lista3.append(c)
lista4.append(d)
if input() != '':
    for i in range(len(lista)):
        print(lista4[i])

if input() == 'Kawai':
    for i in range(len(lista)):
        print(lista[i])

if input() == 'Yamaha':
    for i in range(len(lista2)):
        print(lista2[i])

if input() == 'Steinway':
    for i in range(len(lista3)):
        print(lista3[i])
