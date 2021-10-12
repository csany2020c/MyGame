import game
import pygame

class napActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 20 * delta_time
        self.x += 32 * delta_time

class hatteractor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/sunny.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class hatteractor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class myscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(gamestage())


class gamestage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.nap = napActor()
        self.hatter = hatteractor()
        self.hatter2 = hatteractor2()
        self.add_actor(self.hatter)
        self.add_actor(self.nap)
        self.add_actor(self.hatter2)
        self.nap.z_index = 1
        self.hatter.z_index = 0
        self.hatter2.z_index = 2
        self.nap.y = -100
        self.nap.x = 100

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class kep(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.set_screen(myscreen())
        self.run()






kep()