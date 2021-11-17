import game
import random
from game.scene2d.MyScreen import *

class Actor(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/spiderman.png"):
        super().__init__(image_url)





class Hatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/hatter.jpg"):
        super().__init__(image_url)


class Stage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()

        self.hatter_bg = Hatter()
        self.actor1_bg = Actor()
        self.add_actor(self.hatter_bg)
        self.add_actor(self.actor1_bg)

        self.actor1_bg.set_on_key_press_listener(self.press)
        self.set_on_key_down_listener(self.key_down)

    def press(self, sender, event):
        if event.key == pygame.K_d:
            sender.x += 10
        if event.key == pygame.K_a:
            sender.x -= 10
        if event.key == pygame.K_w:
            sender.y -= 10
        if event.key == pygame.K_s:
            sender.y += 10

    def interval(self, sender):
        self.actor1_bg.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Kep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Kep().run()

