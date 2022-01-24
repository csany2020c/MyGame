import game
from Kancsalmate27megilyenek.Enemys import *

class EnemyActor(game.scene2d.MyActor):

    def __init__(self,index:int,x:int, y:int):
        super().__init__("Heroamijó_1.png")
        self.enemyC = Enemys()
        for i in range(len(self.enemyC.enemys)):
            if self.enemyC.enemys[index]:
                self.ellenseg = self.enemyC.enemys[index]
                break
            else:
                self.ellenseg = None
        self.x = x
        self.y = y
        self.image_url = self.ellenseg.image
        self.damage:int = int(self.ellenseg.damage)
        self.hp:int = int(self.ellenseg.hp)
        self.maxHP:int = int(self.ellenseg.hp)
