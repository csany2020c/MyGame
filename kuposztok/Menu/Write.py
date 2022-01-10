from kuposztok.Menu.MenuStage import MenuStage
def write():
    with open('../kuposztok/palya1.txt', 'w') as file:
        money = MenuStage.getMenuMoney()
        money2 = money + 1
        file.write(money2)
        print(money2)
