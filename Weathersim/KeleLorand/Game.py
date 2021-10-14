import game
from game.scene2d import *
from game.scene2d.MyScreen import *
import random

class HatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

class MenuHatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/weathersim.png")

class FallHatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/falllandscape.png")

class SnowHatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snowlandscape.png")

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
        super().__init__("A Játékot a billentyűzet nyilaival lehet vezérelni.")

class Leiras2(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Az időjárás a kiválasztott évszak alapján változik.")

class Leiras4(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Az ESCAPE gomb lenyomásával, pedig ki tudsz lépni.")

class Leiras3(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Klikkelj bárhová a képernyőn, hogy elindítsd a játékot!")

class Esocsepp(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

class Esocsepp2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

class Esocsepp3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

class Esocsepp4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

class Esocsepp5(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

class Hopehely(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

class Hopehely2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

class Hopehely3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

class Hopehely4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

class Hopehely5(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

class RightArrow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rightarrow.png")

class LeftArrow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/leftarrow.png")

class SzurkeAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/szurke.png")

class TavaszBackAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/tavaszland.png")

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()


        self.menuhatter = MenuHatterAct()
        self.szurkehatter = SzurkeAct()

        self.leiras1 = Leiras1()
        self.leiras2 = Leiras2()
        self.leiras3 = Leiras3()
        self.leiras4 = Leiras4()

        self.menuhatter.z_index = 2
        self.szurkehatter.z_index = 1

        self.leiras2.y = 100
        self.leiras3.y = 300
        self.leiras4.y = 200
        self.menuhatter.y = 300

        self.add_actor(self.menuhatter)
        self.add_actor(self.leiras1)
        self.add_actor(self.leiras2)
        self.add_actor(self.leiras3)
        self.add_actor(self.leiras4)
        self.add_actor(self.szurkehatter)

        self.hatterset : bool = False

    def act(self, delta_time: float):
        if self.hatterset == False:
            self.menuhatter.y = self.menuhatter.y - 1
        if self.menuhatter.y == 0:
            self.hatterset = True

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
        self.raindrop = Esocsepp()
        self.raindrop2 = Esocsepp2()
        self.raindrop3 = Esocsepp3()
        self.raindrop4 = Esocsepp4()
        self.raindrop5 = Esocsepp5()

        self.hattersnow = SnowHatterAct()
        self.hatterfall = FallHatterAct()
        self.hatterspring = TavaszBackAct()

        self.snow = Hopehely()
        self.snow2 = Hopehely2()
        self.snow3 = Hopehely3()
        self.snow4 = Hopehely4()
        self.snow5 = Hopehely5()

        self.rightArrow = RightArrow()
        self.leftArrow = LeftArrow()

        self.hatterfall.z_index = 6
        self.hattersnow.z_index = 6
        self.hatter_bg.z_index = 6
        self.napos_bg.z_index = 4
        self.nap_bg.z_index = 5
        self.szurke_bg.z_index = 1
        self.leftArrow.z_index = 7
        self.rightArrow.z_index = 7

        self.raindrop.height = 30
        self.raindrop.width = 30

        self.raindrop2.height = 30
        self.raindrop2.width = 30

        self.raindrop3.height = 30
        self.raindrop3.width = 30

        self.raindrop4.height = 30
        self.raindrop4.width = 30

        self.raindrop5.height = 30
        self.raindrop5.width = 30

        self.snow.height = 30
        self.snow.width = 30

        self.snow2.height = 30
        self.snow2.width = 30

        self.snow3.height = 30
        self.snow3.width = 30

        self.snow4.height = 30
        self.snow4.width = 30

        self.snow4.height = 30
        self.snow4.width = 30

        self.snow5.height = 30
        self.snow5.width = 30

        self.rightArrow.height = 500
        self.leftArrow.height = 500

        self.rightArrow.x = 944
        self.leftArrow.x = -200

        self.rightArrow.y = 150
        self.leftArrow.y = 150

        self.nyar_lb.x = 640
        self.oszlab_lb.x = 640
        self.tav_lb.x = 640
        self.tel_lb.x = 640

        self.nap_bg.x = 900
        self.nap_bg.y = -100


        self.add_actor(self.rightArrow)
        self.add_actor(self.leftArrow)



        self.currentTime: int = 1
        self.waitTime = 5
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

        self.havazik : bool = False
        self.esik : bool = False

        self.rainonstage : bool = False

        self.snowonstage : bool = False

        self.rainSet : bool = False
        self.rain2Set : bool = False
        self.rain3Set: bool = False
        self.rain4Set: bool = False
        self.rain5Set: bool = False

        self.snowSet: bool = False
        self.snow2Set: bool = False
        self.snow3Set: bool = False
        self.snow4Set: bool = False
        self.snow5Set: bool = False

        self.havastaj : bool = False
        self.napostaj : bool = False
        self.oszitaj : bool = False
        self.tavasztaj : bool = False

        self.randomSet : bool = False

        self.naple : bool = False

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):

        if event.key == pygame.K_RIGHT:
            self.currentSeason = self.currentSeason + 1
            print(self.currentSeason)
        if event.key == pygame.K_LEFT:
            self.currentSeason = self.currentSeason - 1
            print(self.currentSeason)
        if event.key == pygame.K_ESCAPE:
            quit()

    def act(self, delta_time: float):
        super().act(delta_time)
        print(self.currentSeason)

        if self.currentSeason == 5:
            self.currentSeason = 1

        if self.currentSeason == 0:
            self.currentSeason = 4


        #nyar
        if self.currentSeason == 1:
            if self.oszitaj == True:
                self.remove_actor(self.hatterfall)
                self.oszitaj = False
            self.add_actor(self.hatter_bg)
            self.napostaj = True
            self.summer = True
            self.fall = False
            self.winter = False
            self.spring = False
            self.esik = False
            self.havazik = False

        #osz
        if self.currentSeason == 2:
            if self.napostaj == True:
                self.remove_actor(self.hatter_bg)
                self.napostaj = False
            self.add_actor(self.hatterfall)
            self.napostaj = False
            self.summer = False
            self.fall = True
            self.winter = False
            self.spring = False
            self.esik = True
            self.havazik = False

        #tel
        if self.currentSeason == 3:
            if self.oszitaj == True:
                self.remove_actor(self.hatterfall)
                self.oszitaj = False
            self.add_actor(self.hattersnow)
            self.napostaj = False
            self.summer = False
            self.fall = False
            self.winter = True
            self.spring = False
            self.esik = False
            self.havazik = True

        #tavasz
        if self.currentSeason == 4:
            if self.havastaj == True:
                self.remove_actor(self.hattersnow)
                self.havastaj = False
            self.add_actor(self.hatter_bg)
            self.napostaj = True
            self.summer = False
            self.fall = False
            self.winter = False
            self.spring = True
            self.esik = False
            self.havazik = False

        if self.summer == True:
            self.add_actor(self.napos_bg)
            self.add_actor(self.nap_bg)
            self.add_actor(self.nyar_lb)
            self.napos_bg.onstage = True
            self.nap_bg.onstage = True
            self.nyar_lb.onstage = True
            if self.tavasztaj == True:
                self.remove_actor(self.hatterspring)
                self.tavasztaj = False
            if self.szurke_bg.onstage == True:
                self.remove_actor(self.szurke_bg)
                self.szurke_bg.onstage = False
            if self.oszlab_lb.onstage == True:
                self.remove_actor(self.oszlab_lb)
                self.oszlab_lb.onstage = False
            if self.tav_lb.onstage == True:
                self.remove_actor(self.tav_lb)
                self.tav_lb.onstage = False
            if self.rainSet == True:
                self.remove_actor(self.raindrop)
                self.rainSet = False
            if self.rain2Set == True:
                self.remove_actor(self.raindrop2)
                self.rain2Set = False
            if self.rain3Set == True:
                self.remove_actor(self.raindrop3)
                self.rain3Set = False
            if self.rain4Set == True:
                self.remove_actor(self.raindrop4)
                self.rain4Set = False
            if self.rain5Set == True:
                self.remove_actor(self.raindrop5)
                self.rain5Set = False

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

            if self.snowSet == True:
                self.remove_actor(self.snow)
                self.snowSet = False

            if self.snow2Set == True:
                self.remove_actor(self.snow2)
                self.snow2Set = False

            if self.snow3Set == True:
                self.remove_actor(self.snow3)
                self.snow3Set = False

            if self.snow4Set == True:
                self.remove_actor(self.snow4)
                self.snow4Set = False

            if self.snow5Set == True:
                self.remove_actor(self.snow5)
                self.snow5Set = False

            if self.rainSet == False:
                self.raindrop.x = random.randint(a=0, b=1280)
                self.raindrop.y = random.randint(a=-0, b=0)
                self.add_actor(self.raindrop)
            if self.rain2Set == False:
                self.raindrop2.x = random.randint(a=0, b=1280)
                self.raindrop2.y = random.randint(a=-0, b=0)
                self.add_actor(self.raindrop2)
            if self.rain3Set == False:
                self.raindrop3.x = random.randint(a=0, b=1280)
                self.raindrop3.y = random.randint(a=-0, b=0)
                self.add_actor(self.raindrop3)
            if self.rain4Set == False:
                self.raindrop4.x = random.randint(a=0, b=1280)
                self.raindrop4.y = random.randint(a=-0, b=0)
                self.add_actor(self.raindrop4)
            if self.rain5Set == False:
                self.raindrop5.x = random.randint(a=0, b=1280)
                self.raindrop5.y = random.randint(a=-0, b=0)
                self.add_actor(self.raindrop5)
            for i in range(4):
                self.raindrop.y = self.raindrop.y + 1
            for i in range(3):
                self.raindrop2.y = self.raindrop2.y + 1
            for i in range(5):
                self.raindrop3.y = self.raindrop3.y + 1
            for i in range(4):
                self.raindrop4.y = self.raindrop4.y + 1
            for i in range(3):
                self.raindrop5.y = self.raindrop5.y + 1
            self.rainSet = True
            self.rain2Set = True
            self.rain3Set = True
            self.rain4Set = True
            self.rain5Set = True
            self.rainonstage = True


        if self.winter == True:
            if self.oszlab_lb.onstage == True:
                self.remove_actor(self.oszlab_lb)
                self.oszlab_lb.onstage = False
            self.add_actor(self.tel_lb)
            self.tel_lb.onstage = True
            if self.tavasztaj == True:
                self.remove_actor(self.hatterspring)
                self.tavasztaj = False
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
            if self.rainSet == True:
                self.remove_actor(self.raindrop)
                self.rainSet = False
            if self.rain2Set == True:
                self.remove_actor(self.raindrop2)
                self.rain2Set = False
            if self.rain3Set == True:
                self.remove_actor(self.raindrop3)
                self.rain3Set = False
            if self.rain4Set == True:
                self.remove_actor(self.raindrop4)
                self.rain4Set = False
            if self.rain5Set == True:
                self.remove_actor(self.raindrop5)
                self.rain5Set = False
            if self.snowSet == False:
                self.snow.x = random.randint(a=0, b=1280)
                self.snow.y = random.randint(a=-0, b=0)
                self.add_actor(self.snow)
            if self.snow2Set == False:
                self.snow2.x = random.randint(a=0, b=1280)
                self.snow2.y = random.randint(a=-0, b=0)
                self.add_actor(self.snow2)
            if self.snow3Set == False:
                self.snow3.x = random.randint(a=0, b=1280)
                self.snow3.y = random.randint(a=-0, b=0)
                self.add_actor(self.snow3)
            if self.snow4Set == False:
                self.snow4.x = random.randint(a=0, b=1280)
                self.snow4.y = random.randint(a=-0, b=0)
                self.add_actor(self.snow4)
            if self.snow5Set == False:
                self.snow5.x = random.randint(a=0, b=1280)
                self.snow5.y = random.randint(a=-0, b=0)
                self.add_actor(self.snow5)
            for i in range(4):
                self.snow.y = self.snow.y + 1
            for i in range(3):
                self.snow2.y = self.snow2.y + 1
            for i in range(5):
                self.snow3.y = self.snow3.y + 1
            for i in range(4):
                self.snow4.y = self.snow4.y + 1
            for i in range(3):
                self.snow5.y = self.snow5.y + 1
            self.snowSet = True
            self.snow2Set = True
            self.snow3Set = True
            self.snow4Set = True
            self.snow5Set = True
            self.snowonstage = True


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
            self.add_actor(self.hatterspring)
            self.tavasztaj = True
            self.napos_bg.onstage = True
            self.add_actor(self.nap_bg)
            self.nap_bg.onstage = True
            if self.nyar_lb.onstage == True:
                self.remove_actor(self.nyar_lb)
                self.nyar_lb.onstage = False
            if self.rainSet == True:
                self.remove_actor(self.raindrop)
                self.rainSet = False
            if self.rain2Set == True:
                self.remove_actor(self.raindrop2)
                self.rain2Set = False
            if self.rain3Set == True:
                self.remove_actor(self.raindrop3)
                self.rain3Set = False
            if self.rain4Set == True:
                self.remove_actor(self.raindrop4)
                self.rain4Set = False
            if self.rain5Set == True:
                self.remove_actor(self.raindrop5)
                self.rain5Set = False

            if self.snowSet == True:
                self.remove_actor(self.snow)
                self.snowSet = False

            if self.snow2Set == True:
                self.remove_actor(self.snow2)
                self.snow2Set = False

            if self.snow3Set == True:
                self.remove_actor(self.snow3)
                self.snow3Set = False

            if self.snow4Set == True:
                self.remove_actor(self.snow4)
                self.snow4Set = False

            if self.snow5Set == True:
                self.remove_actor(self.snow5)
                self.snow5Set = False

        if self.raindrop.y == 720:
            self.rainSet = False
        if self.raindrop2.y == 720:
            self.rain2Set = False
        if self.raindrop3.y == 720:
            self.rain3Set = False
        if self.raindrop4.y == 720:
            self.rain4Set = False
        if self.raindrop5.y == 720:
            self.rain5Set = False

        if self.snow.y == 720:
            self.snowSet = False
        if self.snow2.y == 720:
            self.snow2Set = False
        if self.snow3.y == 720:
            self.snow3Set = False
        if self.snow4.y == 720:
            self.snow4Set = False
        if self.snow5.y == 720:
            self.snow5Set = False



        self.nap_bg.rotate_with(1)







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



