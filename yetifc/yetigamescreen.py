import game
import pygame

class Character(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/character.png")

class GameBG(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/gamebg.png")

class Revolver(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/revolver.png")

class Shotgun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/shotgun.png")

class BulletCount(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Bullets:")

class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

class GameStage(game.scene2d.MyStage):
    def __init__(self):
        self.ronstage : bool = True
        self.sonstage : bool = False
        super().__init__()
        self.character = Character()
        self.gamebg = GameBG()
        self.revolver = Revolver()
        self.shotgun = Shotgun()
        self.bulletcount = BulletCount()
        self.add_actor(self.gamebg)
        self.add_actor(self.character)
        self.add_actor(self.bulletcount)
        self.character.width = 200
        self.gamebg.z_index = 0
        self.character.z_index = 1
        self.revolver.z_index = 2
        self.shotgun.z_index = 2
        self.revolver.y = 410
        self.revolver.x = 70
        self.shotgun.y = 400
        self.shotgun.x = 30
        self.add_actor(self.revolver)
        self.character.y = 400
        self.set_on_key_press_listener(self.key_down)
        self.set_on_key_down_listener(self.weapon_switch)



    def key_down(self, sender, event):
        if event.key == pygame.K_d:
            self.character.x = self.character.x + 10
            self.revolver.x = self.revolver.x + 10
            self.shotgun.x = self.shotgun.x + 10

        if event.key == pygame.K_a:
            self.character.x = self.character.x - 10
            self.revolver.x = self.revolver.x - 10
            self.shotgun.x = self.shotgun.x - 10

    def weapon_switch(self, sender, event):
        if event.key == pygame.K_2:
            if self.ronstage == True:
                self.remove_actor(self.revolver)
                self.ronstage = False
                pygame.mixer.music.load("Images/shotgun.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
            self.add_actor(self.shotgun)
            self.sonstage = True


        if event.key == pygame.K_1:
            if self.sonstage == True:
                self.remove_actor(self.shotgun)
                self.sonstage = False
                pygame.mixer.music.load("Images/shotgun.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
            self.add_actor(self.revolver)
            self.ronstage = True


        if event.key == pygame.K_SPACE:
            self.character.x = self.character.x -30
            self.shotgun.x = self.shotgun.x -30
            self.revolver.x = self.revolver.x -30






