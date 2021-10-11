import Weathersim.marcontamas.NaposScreen
import game
from Weathersim.marcontamas.NaposScreen import NaposScreen

class IdojarasLabel(game.scene2d.MyLabel):
    def __init__(self, string: str = "Időjárás", font_name: str = "system", font_size: int = 64):
        super().__init__(string, font_name, font_size)
        self.x = 640 - 80
        self.y = 360 - 30
        self.set_color(0,100,167)
        self.set_on_mouse_down_listener(self.kattintas)

    def kattintas(self,sender,event):
        if event.button == 1:
            self.stage.screen.game.set_screen(Weathersim.marcontamas.NaposScreen.NaposScreen())