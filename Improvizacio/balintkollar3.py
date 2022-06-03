class Dolgozat:
    def __init__(self) -> None:
        super().__init__()
        self.max: int = 0
        self.sajat: int = 0
        self.jegy: int = 0

    def szazalekokfuggveny(self):
        return (self.sajat / self.max) * 100

#    def jegyek(self):
#        if self.szazalekokfuggveny() <= 24:
#            self.jegy = 1
#        if self.szazalekokfuggveny() >= 25 and self.szazalekokfuggveny() <= 39:
#            self.jegy = 2
#        if self.szazalekokfuggveny() >= 40 and self.szazalekokfuggveny() <= 59:
#            self.jegy = 3
#        if self.szazalekokfuggveny() >= 60 and self.szazalekokfuggveny() <= 79:
#            self.jegy = 4
#        if self.szazalekokfuggveny() >= 80:
#            self.jegy = 5

x = Dolgozat()
x.max = int(input("A maximum pontszám: "))
x.sajat = int(input("Elér pontszám: "))
x.szazalek = (x.sajat / x.max) * 100
print("Elért százalék {a}%".format(a=x.szazalek))
print("Elért százalék fügvénnyel {a}%".format(a=x.szazalekokfuggveny()))

x.jegy = 0
if x.szazalek <= 24:
    x.jegy = 1
if x.szazalek >= 25 and x.szazalek <= 39:
    x.jegy = 2
if x.szazalek >= 40 and x.szazalek <= 59:
    x.jegy = 3
if x.szazalek >= 60 and x.szazalek <= 79:
    x.jegy = 4
if x.szazalek >= 80:
    x.jegy = 5

print(x.jegy)






