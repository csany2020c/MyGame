import game
import pygame


class Actor(game.scene2d.MyActor):

    def __init__(self, x: float, y: float):
        super().__init__("snow.png")
        self.w = 5
        self.x = x
        self.y = y


class MathGraphStage(game.scene2d.MyStage):

    # f(x) = 2x^2 - 5x - 3
    def f(self, x : float) -> float:
        return 2*x*x-5*x-3

    def add_coord(self, x: float, y: float):
        xx= x * self.zoom + game.scene2d.MyGame.get_screen_width() / 2
        yy=-y * self.zoom + game.scene2d.MyGame.get_screen_height() / 2
        if xx >= 0 and yy >= 0 and xx <= game.scene2d.MyGame.get_screen_width() and yy <= game.scene2d.MyGame.get_screen_height():
            self.add_actor(Actor(xx, yy))

    def __init__(self):
        self.zoom: float = 50
        super().__init__()
        x: float = -640 / self.zoom
        while x < 640 / self.zoom:
            self.add_coord(x, self.f(x))
            x += 1 / self.zoom

    def draw(self):
        super().draw()
        x: float = 0
        while x < game.scene2d.MyGame.get_screen_width() / 2:
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27), start_pos=(game.scene2d.MyGame.get_screen_width() / 2 + x, 0), end_pos=(game.scene2d.MyGame.get_screen_width() / 2 + x, game.scene2d.MyGame.get_screen_height()))
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27), start_pos=(game.scene2d.MyGame.get_screen_width() / 2 - x, 0), end_pos=(game.scene2d.MyGame.get_screen_width() / 2 - x, game.scene2d.MyGame.get_screen_height()))
            x += self.zoom

        y: float = 0
        while y < game.scene2d.MyGame.get_screen_height() / 2:
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27),
                             start_pos=(0, game.scene2d.MyGame.get_screen_height() / 2 - y), end_pos=(
                game.scene2d.MyGame.get_screen_width(), game.scene2d.MyGame.get_screen_height() / 2 - y))
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27),
                             start_pos=(0, game.scene2d.MyGame.get_screen_height() / 2 + y), end_pos=(
                game.scene2d.MyGame.get_screen_width(), game.scene2d.MyGame.get_screen_height() / 2 + y))
            y += self.zoom

        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27), start_pos=(0, game.scene2d.MyGame.get_screen_height() / 2), end_pos=(game.scene2d.MyGame.get_screen_width(), game.scene2d.MyGame.get_screen_height() / 2))
        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27), start_pos=(game.scene2d.MyGame.get_screen_width() / 2, 0), end_pos=(game.scene2d.MyGame.get_screen_width() / 2, game.scene2d.MyGame.get_screen_height()))


class X2(MathGraphStage):

    def f(self, x: float) -> float:
        return x * x


class X3(MathGraphStage):

    def f(self, x: float) -> float:
        return x*x*x


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(MathGraphStage())


class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.screen=Screen()