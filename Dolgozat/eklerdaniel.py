from typing import List
import random
print("1. feladat")

# class egy:
#     a = int(input())
#     b = int(input())
#     c = b-b
#     for c in range(b+1):
#         print(a*c )
# egy()

print("2.feladat")
#
class ketto:
    l: List['ketto'] = list()
    l.append(input())

    while True:
        if input() == "":
            print(random.choice(l))
            break
        else:
            continue
ketto()


print("3. feladat")

class harom:
    def __init__(self):
        super().__init__()
        self.gombokszama  =  0
        self.viszintesgorgo = True
        self.fuggolegesgorgo = False
        self.gyarto = ""


harom()


class harommarom:

    l: List['harommarom'] = list()
    z = harom()
    z.gombokszama = 4
    z.fuggolegesgorgo = True
    z.viszintesgorgo = False
    z.gyarto = "Logitech"
    l.append(z)
    print(l)

harommarom()