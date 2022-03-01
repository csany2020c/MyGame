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
#
# def szamitas(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def relativprim(a, b):
#     return szamitas(a, b) == 1
#
# print(relativprim(8,9))
# print(relativprim(1,2))
# print(relativprim(45,67))
# print(relativprim(583,596))
# print(relativprim(696,798))
# print(relativprim(182,458))
# print(relativprim(559,5438))
# print(relativprim(583,697))
# print(relativprim(646,749))
# print(relativprim(69,797))
# print(relativprim(69420, 9))


def relativprim(a: int, b: int) -> bool:
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print(relativprim(45,67))
print(relativprim(583,596))
print(relativprim(696,798))