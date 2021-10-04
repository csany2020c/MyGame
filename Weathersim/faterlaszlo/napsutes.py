import game
import pygame

class hatter_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class napocska(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")


    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 10 * delta_time
        self.x += 1.5 + delta_time


class f_stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = hatter_actor()
        self.sun = napocska()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.sun.set_on_key_down_listener(self.key_down)
        self.sun.x = 5
        self.sun.y = 80
        self.sun.w = 350



    def key_down(self, event, sender):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Sikeresen be lett zárva")
            pygame.quit()


class f_screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 100, 90)
        self.add_stage(f_stage())


class f_game(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.set_screen(f_screen())


f_game().run()

