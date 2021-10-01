import game
import pygame


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/fatjordan.png")
        self.life = 5
        self.set_on_key_down_listener(self.key_down)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_f:
            print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
            self.asd.x += 4
