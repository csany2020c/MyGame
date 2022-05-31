import os
from typing import List

class focilabda:

    def __init__(self):
        super().__init__()
        self.szin: str = ""
        self.meret: int = 0
        self.ar: int = 0
        self.hasznalat: str = ""
        self.hasznose: bool = False

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None

def boolbeolvasas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + "(I vagy N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def meretbeolvas(prompt: str, min: int = 1, max: int = 5) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

def arbeolvas(prompt: str, min: int = 1, max: int = 1000000) -> int:
    while True:
        be: str = input(prompt)
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass

l: List['focilabda'] = list()

fn = "troznairoland2.txt"

fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i: int = 0
while i < len(sorok):
    a = focilabda()
    a.szin = sorok[i]
    i += 1
    a.meret = int(sorok[i])
    i += 1
    a.ar = int(sorok[i])
    i += 1
    a.hasznalat = sorok[i]
    i += 1
    a.hasznose = strtobool(sorok[i])
    i += 1
    l.append(a)
fr.close()

while boolbeolvasas("Szeretne-e focilabdát felvinni a billentyűzettel?: "):
    focilabda4 = focilabda()
    focilabda4.szin = input("A labda színe: ")
    focilabda4.meret = meretbeolvas("Kérem a labda méretét: ")
    focilabda4.ar = arbeolvas("A labda ára forintban: ")
    focilabda4.hasznalat = input("Megfelelő csoport: ")
    focilabda4.hasznose = boolbeolvasas("Hasznos-e a labda? ")
    l.append(focilabda4)

for i in l:
    print(i)

os.remove(fn)
f = open(fn, mode="w", encoding="utf-8")
for i in l:
    f.write(i.__str__() + "\n")
f.close()