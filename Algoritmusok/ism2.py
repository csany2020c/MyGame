from typing import List

#range(1, k + 1) == [2,3,4,5,6, ..., k]
def qwert(k: int) -> int:
    osszeg: int = 0
    for asd in range(1, k + 1):
        osszeg = osszeg + asd
        print(asd)
    print("---")
    return osszeg


# print(qwert(10))
# print(qwert(5))
#print(qwert(qwert(qwert(4))))

li: List['int'] = (8, 77, 33, 23)

# for asd in li:
#     print(asd)

print(li[1])