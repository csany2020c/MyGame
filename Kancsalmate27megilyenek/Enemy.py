import game

class Enemy(game.scene2d.MyActor):


    def __init__(self, image_url: str = ""):
        super().__init__(image_url)
        self.speed = 0
        self.damage = 0
        self.hp = 0
        self.image = ""
        if type == "jani":
            self.damage = 20
            self.hp = 50
            self.speed = 5
            self.image = "Heroamijó_1.png"
            self.image_url=self.image

        elif type == "cigany":
            self.speed = 60
            self.hp = 20
            self.damage = 20
            self.image = "Heroamijó_2.png"
            self.image_url=self.image
        sta

    def gethp(self) -> int:
        return self.hp
    def getspeed(self,type) -> int:
        return self.speed
    def getdamage(self,type) -> int:
        return self.damage


