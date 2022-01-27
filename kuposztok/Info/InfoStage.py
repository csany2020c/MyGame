import game
import pygame
from kuposztok.Info.InfoActors import *
import kuposztok

class InfoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.add_actor(self.bg)
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/infomusica.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.text1 = game.scene2d.MyLabel("A játék lényege, hogy a karakterünkel minél több")
        self.text1.set_color(0, 0, 0)
        self.text1.x = 100
        self.text1.y = 0 + self.text1.get_height()
        self.add_actor(self.text1)
        self.text2 = game.scene2d.MyLabel("pontot érjünk el úgy, hogy a fákat kerülgetjük.")
        self.text2.set_color(0, 0, 0)
        self.text2.x = 100
        self.text2.y = 0 + self.text2.get_height() * 2
        self.add_actor(self.text2)
        self.text3 = game.scene2d.MyLabel("A játék ezek mellet tartalmaz még egyéb tárgyakat,")
        self.text3.set_color(0, 0, 0)
        self.text3.x = 100
        self.text3.y = 0 + self.text3.get_height() * 3
        self.add_actor(self.text3)
        self.text31 = game.scene2d.MyLabel("mint például az energiaital, vagy a trap:")
        self.text31.set_color(0, 0, 0)
        self.text31.x = 100
        self.text31.y = 0 + self.text31.get_height() * 4
        self.add_actor(self.text31)
        self.energy = Energy()
        self.energy.x = self.text3.get_x()
        self.energy.y = 0 + self.text3.get_height() * 5
        self.energy.width = 150
        self.energy.height = 150
        self.add_actor(self.energy)
        self.trap = Trap()
        self.trap.x = self.text3.get_x() + self.text3.get_x() * 3
        self.trap.y = 0 + self.text3.get_height() * 5
        self.add_actor(self.trap)
        self.text4 = game.scene2d.MyLabel("A játékost a billentyűzeten lévő 'w', 'a', 's', 'd' gombokkal")
        self.text4.set_color(0, 0, 0)
        self.text4.x = 100
        self.text4.y = self.height / 2 + self.text4.get_height()
        self.add_actor(self.text4)
        self.text5 = game.scene2d.MyLabel("tudjuk irányítani. Multiplayer módban az egyik karaktert")
        self.text5.set_color(0, 0, 0)
        self.text5.x = 100
        self.text5.y = self.height / 2 + self.text5.get_height() * 2
        self.add_actor(self.text5)
        self.text6 = game.scene2d.MyLabel("szintén ezekkel a gombokkal, míg a másikat pedig a ")
        self.text6.set_color(0, 0, 0)
        self.text6.x = 100
        self.text6.y = self.height / 2 + self.text5.get_height() * 3
        self.add_actor(self.text6)
        self.text7 = game.scene2d.MyLabel("billyentyűzeten lévő nyilakkal. Visszalépés ")
        self.text7.set_color(0, 0, 0)
        self.text7.x = 100
        self.text7.y = self.height / 2 + self.text7.get_height() * 4
        self.add_actor(self.text7)
        self.text71 = game.scene2d.MyLabel("az 'ESC' gombbal történik, valamint ez a gomb a menüben")
        self.text71.set_color(0, 0, 0)
        self.text71.x = 100
        self.text71.y = self.height / 2 + self.text71.get_height() * 5
        self.add_actor(self.text71)
        self.text72 = game.scene2d.MyLabel("a kilépést szolgálja.")
        self.text72.set_color(0, 0, 0)
        self.text72.x = 100
        self.text72.y = self.height / 2 + self.text72.get_height() * 6
        self.add_actor(self.text72)
        self.back = Back()
        self.add_actor(self.back)
        self.back.x = self.width - self.back.get_width()
        self.back.y = self.height - self.back.get_height()

        self.set_on_key_down_listener(self.katt)
        self.back.set_on_mouse_down_listener(self.Back)

    def katt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Back(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())
