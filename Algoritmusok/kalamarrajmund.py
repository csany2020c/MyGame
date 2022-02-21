from typing import List



# a = 1
# b = 1
#
# def faktorialis():
#     a = b * 1
#     a = a * 2
#     a = a * 3
#     a = a * 4
#     a = a * 5
#
#
#
#     print(a)
#
# faktorialis()


# def fakt(n: int) -> int:
#     szorzat = 1
#     for i in range(2, n + 1):
#         szorzat *= i
#     return szorzat
#
# print(fakt(5))

# def osztok():
#     kod = int(input())
#     for i in range(1, kod + 1 ):
#         if kod % i == 0:
#             print(i)
#
#
#
# osztok()

#
# def osztok():
#     kod = int(input())
#     for i in range(1, kod + 1 ):
#         if kod % i == 0:
#             print(i)
#             if i == kod and if i :
#                 print("true")
#             else:
#                 print("false")
#
# osztok()

#
# def osztok(n: int) -> List['int']:
#     l: list['int'] = list()
#     for i in range(1, n + 1 ):
#         if n % i == 0:
#             l.append(i)
#     return(l)
#     for i in osztok(len(osztok)):
#         if len(list) == 2:
#             print("true")
#         else:
#             print("false")
# for i in range(1, 20):
#     print(i)
#     for i in osztok(len(list)):
#         if len(list) == 2:
#             print("true")
#         else:
#             print("false")
# def binaris_osztas() -> List['int']:
#     visszaadja = list()
#     szam: str = int(input())
#     s = ""
#     for i in range(0, 24):
#         if (szam & 0x800000) == 0:
#             s += "0"
#             visszaadja.append(s)
#         else:
#             s += "1"
#         szam <<= 1
#
#         print(visszaadja)
#
#
#     return visszaadja
#


# def hazi(n: List['int'], a: int ) -> List['int']:
#     visszaadottlista: List['int'] = list()
#     for i in n:
#         if i % a == 0:
#             visszaadottlista.append(i)
#
#     return visszaadottlista
#
# print(hazi([1, 2, 3, 4, 5, 6, 7], 3))

# def hazi2(n: List['int']) -> bool:
#     csocs = 0
#     for i in n:
#         if i == 0:
#             csocs += 1
#
#     if csocs > 0:
#         return True
#     else:
#         return False
#
#
# print(hazi2([1,2,3,4,5,6,7,0]))

# def hazi3(a : int, b: int) -> int:
#         if a > b:
#             return b
#         else:
#
#             return a
# print(hazi3(3,5))


# def hazi4(n: List['int']) -> int:
#         a = 900000
#         for i in n:
#             if i < a:
#                 a = i
#
#         return a
#
# print(hazi4([6,2,3,4,5,1,7,8]))


def helyiertek(szam: int) -> List['int']:
    lista: List['int'] = list()

    while szam > 0:
        lista.append(szam % 10)
        szam //= 10
    return lista[::-1]
print(helyiertek(1123))