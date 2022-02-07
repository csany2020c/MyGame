a = input('')
a = int(a)

def asd(binary):
    binary = binary[::-1]
    a = 0
    power = 0
    for i in binary:
        a += int(i) * (2 ** power)
        power += 1
    return a
print(asd('a'))



