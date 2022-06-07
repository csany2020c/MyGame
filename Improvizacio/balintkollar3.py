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
print("Elért százalék:" "\033[0;33;48m {a}% \033[0m".format(a=x.szazalek))
print("Elért százalék fügvénnyel:""\033[0;33;48m {a}% \033[0m".format(a=x.szazalekokfuggveny()))

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

print("Jegyek a százalék alapján: ""\033[0;33;48m{a}".format(a=x.jegy))







