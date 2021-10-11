import game
from game.scene2d import *
from game.scene2d.MyScreen import *



class HatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

class NaposAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sunny.png")

class NapAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")


class SzurkeAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/cloudy.png")

class OszLab(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Ősz")

class TelLab(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Tél")

class TavLab(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Tavasz")

class NyarLab(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Nyár")



class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()




        self.oszlab_lb = OszLab()
        self.tel_lb = TelLab()
        self.tav_lb = TavLab()
        self.nyar_lb = NyarLab()

        self.szurke_bg = SzurkeAct()
        self.hatter_bg = HatterAct()
        self.napos_bg = NaposAct()
        self.nap_bg = NapAct()

        self.hatter_bg.z_index = 6
        self.napos_bg.z_index = 4
        self.nap_bg.z_index = 5

        self.nyar_lb.x = 640
        self.oszlab_lb.x = 640
        self.tav_lb.x = 640
        self.tel_lb.x = 640

        self.nap_bg.x = 900
        self.nap_bg.y = -100

        self.add_actor(self.hatter_bg)


        self.currentSeason: int = 1

        self.summer : bool = False
        self.fall : bool = False
        self.winter : bool = False
        self.spring : bool = False

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):

        if event.key == pygame.K_RIGHT:
            self.currentSeason = self.currentSeason + 1
            print(self.currentSeason)
        if event.key == pygame.K_LEFT:
            self.currentSeason = self.currentSeason - 1
            print(self.currentSeason)

    def act(self, delta_time: float):
        super().act(delta_time)
        print(self.currentSeason)

        if self.currentSeason == 1:
            self.summer = True
        else:
            self.summer = False

        if self.currentSeason == 2:
            self.fall = True
        else:
            self.fall = False

        if self.currentSeason == 3:
            self.winter = True
        else:
            self.winter = False
        if self.currentSeason == 4:
            self.spring = True
        else:
            self.spring = False

        if self.summer == True:
            self.add_actor(self.napos_bg)
            self.add_actor(self.nap_bg)
            self.add_actor(self.nyar_lb)



        if self.fall == True:
            self.add_actor(self.szurke_bg)







class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())



class GameSelf(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = GameScreen()



GameSelf().run()



