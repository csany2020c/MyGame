import game
import pygame

class hatter_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class havazas(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")


    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 0.2 * delta_time
        self.y += 110 * delta_time

class f_stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = hatter_actor()
        self.hopehely = havazas()
        self.add_actor(self.bg)
        self.add_actor(self.hopehely)
        self.bg.set_on_key_down_listener(self.key_down)
        self.hopehely.w = 70



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

