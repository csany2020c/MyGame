import Kancsalmate27megilyenek
import game
from Kancsalmate27megilyenek import ArenaStage
from game.scene2d import MyStage


class Enemy(game.scene2d.MyActor):


    def __init__(self, image_url: str = ""):
        super().__init__(image_url)
        self.speed = 0
        self.damage = 0
        self.hp = 0



class getDatas():

    def __init__(self,stage:MyStage,type:str) -> None:
        super().__init__()
        if type == "jani":
            self.damage = 20
            self.hp = 50
            self.speed = 5
            self.image = "Heroamijó_1.png"

        elif type == "cigany":
            self.speed = 60
            self.hp = 20
            self.damage = 20
            self.image = "Heroamijó_2.png"

        stage.add_actor(Enemy(self.image))

    def gethp(self) -> int:
        return self.hp
    def getspeed(self,type) -> int:
        return self.speed
    def getdamage(self,type) -> int:
        return self.damage


