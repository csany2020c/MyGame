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
        self.text1 = game.scene2d.MyLabel("A játék lényege, hogy a karakterünkel minél több pontot érjünk el úgy,")
        self.text1.set_color(0, 0, 0)
        self.text1.x = 200
        self.text1.y = 0 + self.text1.get_height()
        self.add_actor(self.text1)
        self.text2 = game.scene2d.MyLabel("hogy a fákat kerülgetjük. A játék ezek mellet tartalmaz még egyéb tárgyakat,")
        self.text2.set_color(0, 0, 0)
        self.text2.x = 200
        self.text2.y = 0 + self.text2.get_height() * 2
        self.add_actor(self.text2)
        self.text3 = game.scene2d.MyLabel("mint például az energiaital, vagy a trap:")
        self.text3.set_color(0, 0, 0)
        self.text3.x = 200
        self.text3.y = 0 + self.text3.get_height() * 3
        self.add_actor(self.text3)
        self.energy = Energy()
        self.energy.x = self.text3.get_x()
        self.energy.y = 0 + self.text3.get_height() * 4
        self.energy.width = 150
        self.energy.height = 150
        self.add_actor(self.energy)
        self.trap = Trap()
        self.trap.x = self.text3.get_x() + self.text3.get_x() * 3
        self.trap.y = 0 + self.text3.get_height() * 4
        self.add_actor(self.trap)
        self.text4 = game.scene2d.MyLabel("A játékost a billentyűzeten lévő 'w', 'a', 's', 'd' gombokkal tudjuk irányítani.")
        self.text4.set_color(0, 0, 0)
        self.text4.x = 200
        self.text4.y = self.height / 2
        self.add_actor(self.text4)
        self.text5 = game.scene2d.MyLabel("Multiplayer módban az egyik karaktert szintén ezekkel a gombokkal, míg a másikat pedig")
        self.text5.set_color(0, 0, 0)
        self.text5.x = 200
        self.text5.y = self.height / 2 + self.text5.get_height()
        self.add_actor(self.text5)
        self.text6 = game.scene2d.MyLabel("a billyentyűzeten lévő nyilakkal. Visszalépés az 'ESC' gombbal történik,")
        self.text6.set_color(0, 0, 0)
        self.text6.x = 200
        self.text6.y = self.height / 2 + self.text5.get_height() * 2
        self.add_actor(self.text6)
        self.text7 = game.scene2d.MyLabel("valamint ez a gomb a menüben a kilépést szolgálja.")
        self.text7.set_color(0, 0, 0)
        self.text7.x = 200
        self.text7.y = self.height / 2 + self.text7.get_height() * 3
        self.add_actor(self.text7)

        self.set_on_key_down_listener(self.katt)

    def katt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())
