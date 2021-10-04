import pygame
import game
import pygame

class bruhActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/legokatona.jpg")

        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_RIGHT:
                self.x += 4
            if event.key == pygame.K_UP:
                self.y -= 4
            if event.key == pygame.K_LEFT:
                self.x -= 4
            if event.key == pygame.K_DOWN:
                self.y += 4

        self.set_on_key_press_listener(key_down)

class enemy1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/katona.jpg")


class horthy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/horthy.jpg")
        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_d:
                self.x += 4
            if event.key == pygame.K_w:
                self.y -= 4
            if event.key == pygame.K_a:
                self.x -= 4
            if event.key == pygame.K_s:
                self.y += 4
        self.set_on_key_press_listener(key_down)

class enemy2 (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/bumsteve.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100