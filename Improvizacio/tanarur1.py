import os
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


def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None


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


# s = Auto()
# s.szin = "Kék"
# s.marka = "Skoda"
# s.automatavaltos = False
# s.ar = 1000000
#
# b = Auto()
# b.szin = "Fekete"
# b.marka = "BMV"
# b.automatavaltos = True
# b.ar = 5000000
#
# z = Auto()
# z.szin = "Piros"
# z.ar = 150000
# z.marka = "Suzuki"
# z.automatavaltos = False


l: List['Auto'] = list()

# l.append(s)
# l.append(b)
# l.append(z)
#
# b.ar = 49999999



# print(s)
# print(b)
# print(z)
fn = "tanarur1.txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    a = Auto()
    a.szin = sorok[i]
    i += 1
    a.marka = sorok[i]
    i += 1
    a.automatavaltos = strtobool(sorok[i])
    i += 1
    a.ar = int(sorok[i])
    i += 1
    l.append(a)
fr.close()

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


os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in l:
    f.write(i.__str__() + "\n")
f.close()
