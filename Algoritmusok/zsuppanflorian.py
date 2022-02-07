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

n = 234
for i in range(2, n+1):
    if n % i == 0:
        ertek = 1
        for k in range(2, (i//2)+1):
            if(i % k == 0):
                ertek = 0
                break
        if(ertek == 1):
            print(i)
