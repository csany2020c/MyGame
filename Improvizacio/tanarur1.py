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

a = Auto()
a.szin = input("Kérem az autó színét: ")
a.marka = input("Kérem az autó márkáját: ")
a.ar = int(input("Kérem az autó árát: "))
a.automatavaltos = boolbeolvas("Automataváltós")

l.append(a)
print("-------")
for i in l:
    print(i)
