file = open('../kuposztok/file.txt', 'r')

money = file.readline()

file.close()

def getMoney() -> str:
    return money