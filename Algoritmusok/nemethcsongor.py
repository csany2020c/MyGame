def binaris(d):
    b = ''
    while True:
        if d == 0:
            break
        elif (d % 2) == 0:
            d = d // 2
            b = '0' + b
        else:
            d = d // 2
            b = '1' + b
    return b


print(binaris(200))
