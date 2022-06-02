import os
from typing import List

class Ventilator:
    def __init__(self):
        self.maxzaj: str = "Max zaj: 60Db"
        self.magassag: str = "Magasság: 130cm"
        self.fogyasztas: str = "Fogyasztás: 55W"
        self.ara = 0

    def __str__(self) -> str:
        return self.maxzaj + "\n" + self.magassag + "\n" + str(self.fogyasztas) + "\n" + str(self.ara)

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
            if i >= min and i <= max:
                return i
            else:
                print("Hibás érték! Nem az intervallumba tartozó szám!")
        except:
            print("Hibás érték! Számot kérek!")

s1: Ventilator = Ventilator()
s1.magassag = "Magasság: 140cm"
s1.fogyasztas = "Fogyasztás: 50W"
s1.ara = 10700


s2: Ventilator = Ventilator()
s2.maxzaj = "Max zaj: 75Db"
s2.magassag = "Magasság: 170cm"
s2.fogyasztas = "Fogyasztás: 70W"
s2.ara = 36000


s3: Ventilator = Ventilator()
s3.maxzaj = "Max zaj: 40Db"
s3.magassag = "Magasság: 110cm"
s3.fogyasztas = "Fogyasztás: 35W"
s3.ara = 8000


l: List['Ventilator'] = list()

l.append(s1)
l.append(s2)
l.append(s3)

s = Ventilator()
s.maxzaj = input("Kérem a ventilátor max zaját: ")
s.magassag = input("Kérem a ventilátor magasságát: ")
s.fogyasztas = input("Kérem a ventilátor fogyasztását:")
s.ara = intbeolvas("Kérem a ventilátor árát : ", 8000, 999999999)

l.append(s)
for i in l:
    print(i)

exit()
