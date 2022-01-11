from typing import List


# def osszegzesvegjelig():
#     osszeg: int = 0
#     szam: int = 1
#
#     while (szam != 0):
#         szam = int(input())
#         if szam != 0:
#             osszeg += szam
#             print("Az eddigi összeg: {sum}".format(sum=osszeg))
#         print("Az összeg: {sum}".format(sum=osszeg))
#
# osszegzesvegjelig()

# def osszeglista():
#     lista: List['int'] = (6, 5, 4, 6, 3, 4, 7, 8)
#     osszeg:int = 0
#
#
#     for i in range(0, len(lista)):
#         osszeg += lista[i]
#
#     print("Az összeg {sum}" .format(sum=osszeg))
#
#
#
# osszeglista()

def osszegzes(lista: List['int']) -> int:
    osszeg:int = 0

    for i in range(0, len(list)):
        lista:int = int(input())
        osszeg += 1

    return osszeg

lista: List['int'] = (1, 5, 67, 8, 9)
print(osszegzes(lista))