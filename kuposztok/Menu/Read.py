with open('../Save/file.txt', 'r') as read:
    moneyin = read.readline()
    print(moneyin)

def getMoney():
    return moneyin
