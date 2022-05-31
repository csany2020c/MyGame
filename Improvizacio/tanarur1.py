from typing import List

class Auto:

    def __init__(self) -> None:
        super().__init__()
        self.szin: str = ""
        self.marka: str = ""
        self.automatavaltos: bool = False
        self.ar = 0

    def __str__(self) -> str:
        return self.szin + "\n" + self.marka + "\n" + str(self.automatavaltos) + "\n" + str(self.ar)


def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False


def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass


s = Auto()
s.szin = "Kék"
s.marka = "Skoda"
s.automatavaltos = False
s.ar = 1000000

b = Auto()
b.szin = "Fekete"
b.marka = "BMV"
b.automatavaltos = True
b.ar = 5000000

z = Auto()
z.szin = "Piros"
z.ar = 150000
z.marka = "Suzuki"
z.automatavaltos = False


l: List['Auto'] = list()

l.append(s)
l.append(b)
l.append(z)

b.ar = 49999999

# print(s)
# print(b)
# print(z)

while boolbeolvas("Szeretne autót felvinni a billentyűzetről?"):
    a = Auto()
    a.szin = input("Kérem az autó színét: ")
    a.marka = input("Kérem az autó márkáját: ")
    a.ar = intbeolvas("Kérem az autó árát: ")
    a.automatavaltos = boolbeolvas("Automataváltós")
    l.append(a)


print("-------")
for i in l:
    print(i)
