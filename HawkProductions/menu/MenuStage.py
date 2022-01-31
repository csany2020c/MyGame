import HawkProductions.Game.GameScreen
from HawkProductions.Info.InfoScreen import *
import HawkProductions.Select.SelectScreen
import HawkProductions.Music


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Nixon.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.t = Title()
        self.h1 = Startb()
        self.h2 = Exit()
        self.b = Gabriola()
        self.b2 = Anything()
        self.add_actor(self.t)
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.add_actor(self.b)
        self.add_actor(self.b2)

        self.t.width = 1300

        self.h1.x = 525
        self.h1.y = 250
        self.h1.w = 200

        self.h2.x = 525
        self.h2.y = 550
        self.h2.w = 200

        self.b.set_text("A Hawk Productions game")
        self.b.x = 500
        self.b.y = 50
        self.b.set_size(250, 50)

        self.b2.set_text("Flappy D")
        self.b2.x = 500
        self.b2.y = 100

        self.i = Info()
        self.add_actor(self.i)
        self.i.y = 400
        self.i.x = 523

        self.h1.set_on_mouse_down_listener(self.click3)

        self.set_on_key_down_listener(self.key_down)
        self.h2.set_on_mouse_down_listener(self.click)
        self.i.set_on_mouse_down_listener(self.click2)
        self.b.set_on_mouse_down_listener(self.click4)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("kilépés")
            quit()
        if event.key == pygame.K_SPACE:
            print("Elindul a játék")
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())
        if event.key == pygame.K_i:
            self.screen.game.set_screen(IScreen())

    def click(self, sender, event):
        if event.button == 1:
            quit()

    def click1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(IScreen())
            pygame.mixer.init()
            pygame.mixer.music.load("../HawkProductions/Music/Info.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)

    def click3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())
            pygame.mixer.init()
            pygame.mixer.music.load("../HawkProductions/Music/Sel.wav")
            pygame.mixer.music.play(-1)

    def click4(self, sender, event):
        if event.button == 1:
            print("Hawk Production's Flappy D")
