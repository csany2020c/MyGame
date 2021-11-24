import game
import kuposztok
from kuposztok.Game.GameActor import *
from game.scene2d import MyIntervalTimer


class Car1StageMultiP(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        self.bg.y = 0
        self.bg.z_index = 1
        self.add_actor(self.bg)
        self.bg2 = BgActor2()
        self.bg2.y = -1080
        self.bg2.z_index = 1
        self.bg2.width = 2400
        self.bg2.height = 1400
        self.add_actor(self.bg2)
        self.button1 = Visszagomb()
        self.button1.z_index = 101
        self.add_actor(self.button1)
        self.button1.width = 95
        self.button1.height = 45
        self.button1.y = 0
        self.button1.x = 0
        self.t = MyIntervalTimer(func=self.Timer, start_time=0, stop_time=9223372036854775807)
        self.add_timer(self.t)

        self.score = 0
        self.scorelabel = game.scene2d.MyLabel("Score:" + str(self.score))
        self.add_actor(self.scorelabel)
        self.scorelabel.x = self.width - 250
        self.scorelabel.y = self.height - 50
        self.scorelabel.set_color(0, 0, 0)
        self.scorelabel.width = 100
        self.scorelabel.height = 50
        self.scorelabel.z_index = 5

        self.vesztettel = vesztettel()
        self.vesztettel.z_index = 99
        self.vesztettel.x = 0
        self.vesztettel.y = 0
        self.vesztettel.width = self.width
        self.vesztettel.height = self.height

        self.joseph = SnowMobile()
        self.add_actor(self.joseph)
        self.joseph.width = 100
        self.joseph.z_index = 5
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500
        self.joseph.hitbox_scale_w = 0.4
        self.joseph.hitbox_scale_h = 0.4
        self.joseph.hitbox_shape = game.simpleworld.ShapeType.Circle

        self.joseph2 = SnowMobile()
        self.add_actor(self.joseph2)
        self.joseph2.width = 100
        self.joseph2.z_index = 5
        self.joseph2.height = 200
        self.joseph2.x = 400
        self.joseph2.y = 500
        self.joseph2.hitbox_scale_w = 0.4
        self.joseph2.hitbox_scale_h = 0.4
        self.joseph2.hitbox_shape = game.simpleworld.ShapeType.Circle

        self.newgame = Newgame()
        self.newgame.x = self.width - 300
        self.newgame.y = self.height - self.height + 250

        for i in range(5):
            self.enemy = Enemy()
            self.add_actor(self.enemy)
            self.enemy.width = 100
            self.enemy.height = 100
            self.enemy.z_index = 5
            self.enemy.x = random.Random().randint(0, 1080)
            self.enemy.y = random.Random().randint(-1080, 0)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_press_listener(self.iranyitas)
        self.joseph2.set_on_key_press_listener(self.iranyitas2)
        self.newgame.set_on_mouse_down_listener(self.NewG)

    def Timer(self, sender):
        self.score = self.score + 1
        self.scorelabel.set_text("Score:" + str(self.score))
        self.vesztettellabel = game.scene2d.MyLabel("Sajnálom a játék végetért számodra, az elért pontszámod:" + str(self.score))
        self.vesztettellabel.x = self.width / 18
        self.vesztettellabel.y = 200
        self.vesztettellabel.set_font_size(55)
        self.vesztettellabel.z_index = 100

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.joseph.overlaps(self.enemy):
            self.score = self.score - self.score
            self.add_actor(self.vesztettel)
            self.add_actor(self.vesztettellabel)
            self.add_actor(self.newgame)
        if self.joseph.overlaps(self.joseph2):
            self.score = self.score - self.score
            self.add_actor(self.vesztettel)
            self.add_actor(self.vesztettellabel)
            self.add_actor(self.newgame)
        if self.joseph2.overlaps(self.enemy):
            self.score = self.score - self.score
            self.add_actor(self.vesztettel)
            self.add_actor(self.vesztettellabel)
            self.add_actor(self.newgame)

    def iranyitas(self, sender, event, a=10):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_d:
            if self.joseph.x < self.width - 200:
                self.joseph.x += a
        if event.key == pygame.K_a:
            if self.joseph.x > 200:
                self.joseph.x -= a
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def iranyitas2(self, sender, event, a=10):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_RIGHT:
            if self.joseph2.x < self.width - 200:
                self.joseph2.x += a
        if event.key == pygame.K_LEFT:
            if self.joseph2.x > 200:
                self.joseph2.x -= a

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def NewG(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car1Multi.Car1ScreenMultiP.Car1ScreenMultiP())





