import random
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.over.OverScreen
from HawkProductions.font.Font import *


class GameStage(game.scene2d.MyStage):

    def __init__(self, puska: int):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Nixon.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.Bg = Bg() #85. sor utan van a fajlbeolvasas
        self.add_actor(self.Bg)
        self.Bg.set_size(width=1280, height=720)

        self.point: int = 0
        self.pointl = game.scene2d.MyLabel("")
        self.update_point()
        self.add_actor(self.pointl)
        self.pointl.set_color(0, 0, 0)
        self.pointl.width = 100
        self.pointl.height = 50
        # for i in range(100):
        #     self.point += 1
        # print(self.point)


        self.D = None
        if puska == 0:
            self.D = Deagle_2()
        if puska == 1:
            self.D = Deagle_3()
        if puska == 2:
            self.D = Deagle_4()
        if puska == 3:
            self.D = Deagle_5()
        if puska == 4:
            self.D = Deagle()

        self.add_actor(self.D)
        self.D.y = 250
        self.D.x = 350
        self.D.width = 105
        self.D.set_hitbox_scale_w = 0.1
        self.D.set_hitbox_scale_h = 0.1

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)

        self.add_timer(game.scene2d.MyTickTimer(self.add_asd, 5))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd1, 7))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd2, 9))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd3, 11))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd4, 6))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd5, 8))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd6, 10))

        self.set_on_key_down_listener(self.katt)

        self.P1 = Pile_f()
        self.P2 = Pile_a()
        self.P3 = Pile_f()
        self.P4 = Pile_a()
        self.P5 = Pile_f()
        self.P6 = Pile_a()
        self.P7 = Pile_f()
        self.P8 = Pile_a()

        self.C = Coin()
        self.C1 = Coin()
        self.C2 = Coin()

        #f = open("../HawkProductions/eredmenyek/eredmenyek.txt", "r+")
        #content: str = f.readline()
        #f.write("\n" + str(self.point))

    def update_point(self):
        self.pointl.set_text("Point: {point}".format(point=self.point))
        f = open("../HawkProductions/eredmenyek/eredmenyek.txt", "r+")
        #problema: amikor a jatek lefut nem irja uj sorba az eredmenyt, amit a jatakban megszereztunk
        #f.write('\n') # uj sort hoz létre
        #eredmenyek.txt fajlba beirja mindig az utoljára kapott kodot
        f.write(str(self.point))
        #masik megoldas f.write('\n' + str(self.point))
        f.close()

    def add_asd(self, sender):
        print(sender)
        self.add_actor(self.P1)
        self.P1.set_hitbox_scale_h = 0
        self.P1.set_hitbox_scale_w = 0
        self.P1.h = 420
        self.P1.y = -65
        if self.elapsed_time > 15:
            self.P1.y = random.randint(-55, -35)
        if self.elapsed_time > 33:
            self.P1.y = random.randint(-45, -35)

        self.add_actor(self.P2)
        self.P2.h = 420
        self.P2.set_hitbox_scale_h = 0
        self.P2.set_hitbox_scale_w = 0
        self.P2.y = 560
        if self.elapsed_time > 15:
            self.P2.y = random.randint(580, 635)
        if self.elapsed_time > 33:
            self.P2.y = random.randint(575, 670)

    def add_asd1(self, sender):
        print(sender)
        self.add_actor(self.P3)
        self.P3.set_hitbox_scale_h = 0
        self.P3.set_hitbox_scale_w = 0
        self.P3.h = 420
        self.P3.y = -25
        if self.elapsed_time > 18:
            self.P3.y = random.randint(-70, -40)
        if self.elapsed_time > 28:
            self.P3.y = random.randint(-45, -30)

        self.add_actor(self.P4)
        self.P4.h = 420
        self.P4.set_hitbox_scale_h = 0
        self.P4.set_hitbox_scale_w = 0
        self.P4.y = 625
        if self.elapsed_time > 18:
            self.P4.y = random.randint(560, 665)
        if self.elapsed_time > 28:
            self.P4.y = random.randint(590, 600)

    def add_asd2(self, sender):
        print(sender)
        self.add_actor(self.P5)
        self.P5.set_hitbox_scale_h = 0
        self.P5.set_hitbox_scale_w = 0
        self.P5.h = 420
        self.P5.y = -35
        if self.elapsed_time > 25:
            self.P5.y = random.randint(-65, -35)
        if self.elapsed_time > 35:
            self.P5.y = random.randint(-55, -40)

        self.add_actor(self.P6)
        self.P6.h = 420
        self.P6.set_hitbox_scale_h = 0
        self.P6.set_hitbox_scale_w = 0
        self.P6.y = 590
        if self.elapsed_time > 25:
            self.P6.y = random.randint(590, 670)
        if self.elapsed_time > 35:
            self.P6.y = random.randint(580, 675)

    def add_asd3(self, sender):
        print(sender)
        self.add_actor(self.P7)
        self.P7.set_hitbox_scale_h = 0
        self.P7.set_hitbox_scale_w = 0
        self.P7.h = 420
        self.P7.y = -35
        if self.elapsed_time > 45:
            self.P7.y = random.randint(-40, -25)

        self.add_actor(self.P8)
        self.P8.h = 420
        self.P8.set_hitbox_scale_h = 0
        self.P8.set_hitbox_scale_w = 0
        self.P8.y = 590
        if self.elapsed_time > 45:
            self.P7.y = random.randint(655, 700)

    def add_asd4(self, sender):
        print(sender)
        self.add_actor(self.C)
        self.C.x = 1180
        self.C.y = 420
        self.C.width = 50
        self.C.set_hitbox_scale_h = 0.1
        self.C.set_hitbox_scale_w = 0.1

    def add_asd5(self, sender):
        print(sender)
        self.add_actor(self.C1)
        self.C1.x = 1200
        self.C1.y = random.randint(200, 500)
        self.C1.width = 50
        self.C1.set_hitbox_scale_h = 0.1
        self.C1.set_hitbox_scale_w = 0.1

    def add_asd6(self, sender):
        print(sender)
        self.add_actor(self.C2)
        self.C2.x = 1200
        self.C2.y = random.randint(200, 500)
        self.C2.width = 50
        self.C2.set_hitbox_scale_h = 0.1
        self.C2.set_hitbox_scale_w = 0.1

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.D.overlaps(self.P1):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P2):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P3):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P4):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P5):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P6):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P7):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P8):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.C):
            self.point += 1
            self.update_point()
        if self.D.overlaps(self.C1):
            self.point += 1
            self.update_point()
        if self.D.overlaps(self.C2):
            self.point += 1
            self.update_point()

    def click2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_w:
            self.D.y -= 50
            self.D.r -= 7.5
            effect = pygame.mixer.Sound('../Hawkproductions/Music/Shoot.wav')
            effect.play()
        if event.key == pygame.K_s:
            self.D.y += 50
            self.D.r += 7.5
            effect = pygame.mixer.Sound('../Hawkproductions/Music/Shoot.wav')
            effect.play()