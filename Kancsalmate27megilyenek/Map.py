import game
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor, DamageActor
from game.scene2d import MyBaseActor
from game.scene2d.MyStage import *
class Map():

    def __init__(self,stage:MyStage,xd:str) -> None:
        super().__init__()

        f = open("../map/" + xd + ".txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "0":
                        stage.water = WaterActor()
                        a = stage.water
                    if c == "1":
                        stage.grass = GrassActor()
                        a = stage.grass
                    if c == "2":
                        stage.sand = SandActor()
                        a = stage.sand
                    if c == "3":
                        stage.stone = StoneActor()
                        a = stage.stone
                    if c == "4":
                        stage.path = PathActor()
                        a = stage.path
                    if c == "5":
                        stage.lava = DamageActor()
                        a = stage.lava

                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        stage.add_actor(a)
                        a.set_z_index(0)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()
