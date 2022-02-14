from typing import List
# szam = 69
# xd = False
# if szam > 1:
#     for i in range(2, szam):
#         if (szam % i) == 0:
#             xd = True
#             break
#
# if xd:
#     print(szam, "nem prímszám")
# else:
#     print(szam, "egy prínmszám")

# from sympy import *
# print(isprime(2))

# n = 234
# for i in range(2, n+1):
#     if n % i == 0:
#         ertek = 1
#         for k in range(2, (i//2)+1):
#             if(i % k == 0):
#                 ertek = 0
#                 break
#         if(ertek == 1):
#             print(i)

# be = int(256)
# if be % 2 == 0:
#    print("{0} páros".format(be))
# else:
#    print("{0} páratlan".format(be))
#


# list = [10, 21, 4, 43, 66, 100]
# for i in list:
#     if i % 2 == 0:
#         print(i)


def parosak(belist: List['int']) -> List['int']:
    kilist: List['int'] = list()
    for i in belist:
        if i % 2 == 0:
            kilist.append(i)
    return kilist

l3 = [3, 6, 8, 2, 3, 1, 4]
l9 = [333, 4, 0, 44]
l4 = parosak(l3)
l5 = parosak(l9)
print(l4)
print(l5)


