import Kancsalmate27megilyenek
import game
from Kancsalmate27megilyenek import ArenaStage
from game.scene2d import MyStage, MyActor, MyLabel


class Enemy(game.scene2d.MyActor):


    def __init__(self, image_url: str = ""):
        super().__init__(image_url)
        self.damage = 0
        self.hp = 0
        self.label = MyLabel("","system",64)

        # self.label2 = MyLabel("","system",64)
        # self.stage.add_actor(self.label2)
        # self.label2.x = self.get_x() - self.label2.get_width() / 2
        # self.label2.y = self.get_y() + self.get_height()

    def set_damage(self,value:int):
        self.damage = value
    def set_hp(self,value:int):
        self.hp = value

    def drawhp(self,stage:MyStage,x:float,y:float):
        stage.add_actor(self.label)
        self.label.x =x
        self.label.y = y

    def act(self, delta_time: float):
        super().act(delta_time)
        # self.label.set_text("Életerő: " + str(self.hp))


class getDatas():

    def __init__(self,stage:MyStage,type:int) -> None:
        super().__init__()
        if type == 0:
            self.damage = 20
            self.hp = 50
            self.speed = 5
            self.image = "Heroamijó_1.png"

        elif type == 1:
            self.speed = 60
            self.hp = 20
            self.damage = 20
            self.image = "Heroamijó_2.png"


    def gethp(self) -> int:
        return self.hp
    def getspeed(self) -> int:
        return self.speed
    def getdamage(self,type) -> int:
        return self.damage
    def getActor(self) -> Enemy:
        return Enemy(self.image)


