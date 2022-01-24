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

class Bullet(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/bullet.png")

class Hud(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/hud.png")


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

class GameStage(game.scene2d.MyStage):
    def __init__(self):
        self.ronstage : bool = True
        self.sonstage : bool = False
        self.kpushed : bool = False
        self.revolock : bool = False
        self.slock : bool = False
        self.kpushed_shotgun : bool = False
        super().__init__()
        self.character = Character()
        self.gamebg = GameBG()
        self.revolver = Revolver()
        self.shotgun = Shotgun()
        self.bulletcount = BulletCount()
        self.bullet = Bullet()
        self.bullet2 = Bullet()
        self.bullet3 = Bullet()
        self.hud = Hud()
        self.add_actor(self.gamebg)
        self.add_actor(self.character)
        #self.add_actor(self.bulletcount)
        self.add_actor(self.hud)
        self.character.width = 200
        self.gamebg.z_index = 0
        self.character.z_index = 1
        self.revolver.z_index = 2
        self.shotgun.z_index = 2
        self.bullet.z_index = 2
        self.hud.y = - 130
        self.revolver.y = 410
        self.revolver.x = 70
        self.shotgun.y = 400
        self.shotgun.x = 30
        self.add_actor(self.revolver)
        self.bullet.width = 100
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
                reload = pygame.mixer.Sound("Images/shotgun.wav")
                reload.play()
            self.add_actor(self.shotgun)
            self.shotgun.x = self.character.x + 30
            self.sonstage = True


        if event.key == pygame.K_1:
            if self.sonstage == True:
                self.remove_actor(self.shotgun)
                self.sonstage = False
                reload = pygame.mixer.Sound("Images/shotgun.wav")
                reload.play()
            self.add_actor(self.revolver)
            self.ronstage = True
            self.revolver.x = self.character.x + 70


        if event.key == pygame.K_SPACE:
            if self.ronstage == True:
                if self.revolock == False:
                    self.kpushed = True
                    self.revolock = True
                    self.bullet.x = self.revolver.x + 70
                    self.bullet.y = self.revolver.y + 40
                    self.character.x = self.character.x - 30
                    self.revolver.x = self.revolver.x - 30
            if self.sonstage == True:
                if self.slock == False:
                    self.kpushed_shotgun = True
                    self.slock = True
                    self.can_play_reload_shotgun = False
                    self.bullet.x = self.shotgun.x + 70
                    self.bullet.y = self.shotgun.y + 60
                    self.bullet2.x = self.shotgun.x + 60
                    self.bullet2.y = self.shotgun.y + 40
                    self.bullet3.x = self.shotgun.x + 60
                    self.bullet3.y = self.shotgun.y + 80
                    self.character.x = self.character.x - 30
                    self.shotgun.x = self.shotgun.x - 30
                    reload = pygame.mixer.Sound("Images/shotgun.wav")
                    reload.play()




    def act(self, delta_time: float):
        super().act(delta_time)
        if self.bullet.x > 1300:
            self.revolock = False

        if self.bullet.x > 1300 and self.bullet2.x > 1300 and self.bullet3.x > 1300:
            self.slock = False


        if self.kpushed == True:
            # revolver

            self.add_actor(self.bullet)
            self.bullet.x = self.bullet.x + 20

        if self.kpushed_shotgun == True:
            # shotgun

            self.add_actor(self.bullet)
            self.bullet.x = self.bullet.x + 20
            self.add_actor(self.bullet2)
            self.bullet2.x = self.bullet2.x + 20
            self.add_actor(self.bullet3)
            self.bullet3.x = self.bullet3.x + 20








