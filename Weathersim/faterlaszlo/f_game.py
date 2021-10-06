import game
from Weathersim.faterlaszlo.f_screen import *

class f_game(game.scene2d.MyGame):
    def __init__(self, width=1280, height=720):
        super().__init__(width, height)
        self.screen = f_screen_m()

    def set_screen_game(self):
        self.set_screen(f_stage_m)


    def set_screen_game1(self):
        self.set_screen(f_stage1)

    def set_screen_game2(self):
        self.set_screen(f_stage2)

    def set_screen_game3(self):
        self.set_screen(f_stage4)

    def set_screen_game4(self):
        self.set_screen(f_stage4)
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, event, sender):
        print(sender)
        print(event)
        if event.key == pygame.K_1:
            print("Sikeresen be lett zárva")
            quit()
