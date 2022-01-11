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
#         if inp % asd == 0:
#             lista.append(asd)
#         asd = asd + 1
#     print(lista)
# cucc()

def cucc2():
    inp = int(input())
    lista = []
    asd = 1
    asd2 = False
    for i in range(inp):
        if inp % asd == 0:
            lista.append(asd)
        asd = asd + 1
    if len(lista) == 2:
        asd2 = True
    print(lista)
cucc2()