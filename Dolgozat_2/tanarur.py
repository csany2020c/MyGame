# a = int(input("Kérem az első számot: "))
# b = int(input("Kérem a második számot: "))
# m = min(a,b)
# if m<0:
#     for i in range(0, m -1 , -1):
#         print(i)
# else:
#     for i in range(0, m):
#         print(i)

# elso = True
# elszoszam = 0
# utolsojo = 0
# while True:
#     s = int(input("Kérek egy számot: "))
#     if s < 0:
#         break
#     else:
#         utolsojo = s
#     if elso:
#         elszoszam = s
#         elso = False
# print(elszoszam)
# print(utolsojo)
#
from typing import List


class Listaelem:

    def __init__(self, ar: int, nev: str, tomeg: int) -> None:
        super().__init__()
        self.ar: int = ar
        self.nev: str = nev
        self.tomeg: int = tomeg

list: List['Listaelem'] = list()

list.append(Listaelem(30, "Élesztő", 40))
list.append(Listaelem(300, "Kóla", 500))
list.append(Listaelem(1500, "Sajt", 700))

osszeg: int = 0
for i in list:
    osszeg += i.ar

print(osszeg)