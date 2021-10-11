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

class Start(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Start")

class Leiras1(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("A Játékot a nyilakkal lehet vezérelni.")

class Leiras2(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Az időjárás a kiválasztott évszak alapján változik.")

class Leiras3(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Klikkelj bárhová a képernyőn, hogy elindítsd a játékot!")


class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()


        self.hatter = HatterAct()
        self.napos = NaposAct()

        self.leiras1 = Leiras1()
        self.leiras2 = Leiras2()
        self.leiras3 = Leiras3()

        self.hatter.z_index = 6
        self.napos.z_index = 4

        self.leiras2.y = 100
        self.leiras3.y = 200

        self.add_actor(self.hatter)
        self.add_actor(self.napos)
        self.add_actor(self.leiras1)
        self.add_actor(self.leiras2)
        self.add_actor(self.leiras3)

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
        self.szurke_bg.z_index = 1

        self.nyar_lb.x = 640
        self.oszlab_lb.x = 640
        self.tav_lb.x = 640
        self.tel_lb.x = 640

        self.nap_bg.x = 900
        self.nap_bg.y = -100


        #alap
        self.add_actor(self.hatter_bg)




        self.currentSeason: int = 1

        self.summer : bool = False
        self.fall : bool = False
        self.winter : bool = False
        self.spring : bool = False

        self.napos_bg.onstage : bool = False
        self.nap_bg.onstage : bool = False
        self.tav_lb.onstage : bool = False
        self.nyar_lb.onstage : bool = False
        self.szurke_bg.onstage : bool = False
        self.oszlab_lb.onstage : bool = False
        self.tel_lb.onstage : bool = False




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

        if self.currentSeason == 5:
            self.currentSeason = 1

        if self.currentSeason == 0:
            self.currentSeason = 4


        #nyar
        if self.currentSeason == 1:
            self.summer = True
            self.fall = False
            self.winter = False
            self.spring = False


        #osz
        if self.currentSeason == 2:
            self.summer = False
            self.fall = True
            self.winter = False
            self.spring = False


        #tel
        if self.currentSeason == 3:
            self.summer = False
            self.fall = False
            self.winter = True
            self.spring = False


        #tavasz
        if self.currentSeason == 4:
            self.summer = False
            self.fall = False
            self.winter = False
            self.spring = True

        if self.summer == True:
            self.add_actor(self.napos_bg)
            self.add_actor(self.nap_bg)
            self.add_actor(self.nyar_lb)
            self.napos_bg.onstage = True
            self.nap_bg.onstage = True
            self.nyar_lb.onstage = True
            if self.szurke_bg.onstage == True:
                self.remove_actor(self.szurke_bg)
                self.szurke_bg.onstage = False
            if self.oszlab_lb.onstage == True:
                self.remove_actor(self.oszlab_lb)
                self.oszlab_lb.onstage = False
            if self.tav_lb.onstage == True:
                self.remove_actor(self.tav_lb)
                self.tav_lb.onstage = False



        if self.fall == True:
            if self.nyar_lb.onstage == True:
                self.remove_actor(self.nyar_lb)
                self.nyar_lb.onstage = False
            if self.nap_bg.onstage == True:
                self.remove_actor(self.nap_bg)
                self.nap_bg.onstage = False
            if self.napos_bg.onstage == True:
                self.remove_actor(self.napos_bg)
                self.napos_bg.onstage = False
            self.add_actor(self.szurke_bg)
            self.szurke_bg.onstage = True
            self.add_actor(self.oszlab_lb)
            self.oszlab_lb.onstage = True
            if self.tel_lb.onstage == True:
                self.remove_actor(self.tel_lb)
                self.tel_lb.onstage = False

        if self.winter == True:
            if self.oszlab_lb.onstage == True:
                self.remove_actor(self.oszlab_lb)
                self.oszlab_lb.onstage = False
            self.add_actor(self.tel_lb)
            self.tel_lb.onstage = True
            if self.tav_lb.onstage == True:
                self.remove_actor(self.tav_lb)
                self.tav_lb.onstage = False
            if self.nap_bg.onstage == True:
                self.remove_actor(self.nap_bg)
                self.nap_bg.onstage = False
            if self.napos_bg.onstage == True:
                self.remove_actor(self.napos_bg)
                self.napos_bg.onstage = False
            self.add_actor(self.szurke_bg)
            self.szurke_bg.onstage = True

        if self.spring == True:
            if self.tel_lb.onstage == True:
                self.remove_actor(self.tel_lb)
                self.tel_lb.onstage = False
            self.add_actor(self.tav_lb)
            self.tav_lb.onstage = True
            if self.szurke_bg.onstage == True:
                self.remove_actor(self.szurke_bg)
                self.szurke_bg.onstage = False
            self.add_actor(self.napos_bg)
            self.napos_bg.onstage = True
            self.add_actor(self.nap_bg)
            self.nap_bg.onstage = True
            if self.nyar_lb.onstage == True:
                self.remove_actor(self.nyar_lb)
                self.nyar_lb.onstage = False


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())

        self.set_on_mouse_down_listener(self.on_mouse_down)

        self.buttonpressed : bool = False
        self.stageadded : bool = False

    def on_mouse_down(self, sender, event):
        if self.stageadded == False:
            self.add_stage(GameStage())
            self.stageadded = True







class GameSelf(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = GameScreen()



GameSelf().run()



