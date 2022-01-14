import game

class Read(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        with open('../Save/file.txt', 'r') as read:
            self.moneyin = read.readline()
            print(self.moneyin)

    def getMoney(self):
        return self.moneyin
