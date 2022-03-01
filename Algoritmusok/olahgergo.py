from typing import List

# def fakt(n: int) -> int:
#     print("Fakt {c}".format(c=n))
#     szorzat = 1
#     for i in range(2, n + 1):
#         szorzat *= i
#     return szorzat

# for i in range(1, 5600):
#     print(fakt(i))
#
# x = fakt(2) + fakt(3) * 100
# print(x)
#
# print(8 % 3)
# print(100 % 33)
# # if 100 % 33 == 0:

# def cucc():
#     inp = int(input())
#     lista = []
#     asd = 1
#     for i in range(inp):
# #         if inp % asd == 0:
# #             lista.append(asd)
# #         asd = asd + 1
# #     print(lista)
# # cucc()
#
# def cucc2():
#     inp = int(input())
#     lista = []
#     asd = 1
#     asd2 = False
#     for i in range(inp):
#         if inp % asd == 0:
#             lista.append(asd)
#         asd = asd + 1
#     if len(lista) == 2:
#         asd2 = True
#     print(lista)
# cucc2()
#



def helyiertek2(be:int) -> List['int']:
    ki: List['int'] = list()
    for c in str(abs(be)):
        ki.append(int(c))
    return ki

# A lista elemeinek a négyzetének az összege [2,3] 2*2+3*3
def negyzetosszeg(be: List['int']) -> int:
    szam: int = 0
    for i in be:
        szam+=i*i
    return szam

def boldoge(szam: int) -> bool:
    aktualisnegyzetosszeg: int = szam
    szekvencia : List['int'] = list()
    while aktualisnegyzetosszeg != 1 and aktualisnegyzetosszeg not in szekvencia:
        szekvencia.append(aktualisnegyzetosszeg)
        aktualisnegyzetosszeg = negyzetosszeg(helyiertek2(aktualisnegyzetosszeg))
        # print(szekvencia)
    return aktualisnegyzetosszeg == 1


# print(boldoge(-23))

def zsuppanbuta(jani) -> bool:
    sanyi: List['int'] = list()
    for i in range(0, jani):
        if boldoge(i) == True:
            sanyi.append(i)
    return sanyi
print(zsuppanbuta(4859))