import game
import pygame

class SunnyImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sunny.png")

class SunImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sun.png")

class LandscapeImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("landscape.png")

class RainImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("rain.png")
        self.set_width(45)
        self.set_height(45)

class CloudyImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("cloudy.png")

class SnowImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("snow.png")

class NapsutesStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.NapActor1 = SunnyImg()
        self.add_actor(self.NapActor1)
        self.NapActor2 = SunImg()
        self.add_actor(self.NapActor2)
        self.NapActor3 = LandscapeImg()
        self.add_actor(self.NapActor3)
        self.NapActor2.x += 850
        self.NapActor2.y += -110
        self.set_on_key_down_listener(self.key_down)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.NapActor2.rotate_with(delta_time * 25)
        if self.elapsed_time > 0:
            self.NapActor2.x -= delta_time * 75
        if self.elapsed_time > 6:
            self.NapActor2.x += delta_time * 150
        if self.elapsed_time > 13:
            self.NapActor2.x -= delta_time * 150
        if self.elapsed_time > 20:
            self.NapActor2.x += delta_time * 150
        if self.elapsed_time > 25:
            self.NapActor2.x -= delta_time * 75


    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class NapsutesScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapsutesStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = EsoScr()

class MenuSzoveg(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.Kilep = MenuSzoveg()
        self.add_actor(self.Kilep)
        self.Kilep.set_text("Kilépés")
        self.Kilep.set_alpha(500)
        self.Kilep.set_width(65)
        self.Kilep.set_height(65)
        self.Kilep.x += 530
        self.Kilep.y += 450
        self.Kilep.set_on_key_down_listener(self.key_down)
        self.Kilep.set_on_mouse_down_listener(self.click)
        self.szoveg = MenuSzoveg()
        self.add_actor(self.szoveg)
        self.szoveg.set_text(" ")
        self.szoveg.set_alpha(500)
        self.szoveg.set_width(40)
        self.szoveg.set_height(40)
        self.szoveg.x += 400
        self.szoveg.y += 575
        self.Jatek = MenuSzoveg()
        self.add_actor(self.Jatek)
        self.Jatek.set_text("Játék")
        self.Jatek.set_alpha(500)
        self.Jatek.set_width(65)
        self.Jatek.set_height(65)
        self.Jatek.x += 550
        self.Jatek.y += 250
        self.Jatek.set_on_mouse_down_listener(self.click2)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

    def click(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'QUIT'")
                quit()

    def click2(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'PLAY'")


class MenuScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(252, 98, 3)
        self.add_stage(MenuStage())

class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.EsoA = CloudyImg()
        self.add_actor(self.EsoA)
        self.EsoA2 = LandscapeImg()
        self.add_actor(self.EsoA2)
        self.EsoCS = RainImg()
        self.add_actor(self.EsoCS)
        self.EsoCS2 = RainImg()
        self.add_actor(self.EsoCS2)
        self.EsoCS3 = RainImg()
        self.add_actor(self.EsoCS3)
        self.EsoCS4 = RainImg()
        self.add_actor(self.EsoCS4)
        self.EsoCS5 = RainImg()
        self.add_actor(self.EsoCS5)
        self.EsoCS.x += 620
        self.EsoCS.y += 100
        self.EsoCS2.x += 700
        self.EsoCS2.y += 190
        self.EsoCS3.x += 810
        self.EsoCS3.y += 140
        self.EsoCS4.x += 900
        self.EsoCS4.y += 270
        self.EsoCS5.x += 1100
        self.EsoCS5.y += 120
        self.set_on_key_down_listener(self.key_down)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.EsoCS.y += delta_time * 15
            self.EsoCS2.y += delta_time * 14
            self.EsoCS3.y += delta_time * 15
            self.EsoCS4.y += delta_time * 16
            self.EsoCS5.y += delta_time * 13

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class EsoScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = HavazasScr()

class HavazasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.HavA = CloudyImg()
        self.add_actor(self.HavA)
        self.HavA2 = LandscapeImg()
        self.add_actor(self.HavA2)
        self.Ho = SnowImg()
        self.add_actor(self.Ho)
        self.Ho2 = SnowImg()
        self.add_actor(self.Ho2)
        self.Ho3 = SnowImg()
        self.add_actor(self.Ho3)
        self.Ho4 = SnowImg()
        self.add_actor(self.Ho4)
        self.Ho5 = SnowImg()
        self.add_actor(self.Ho5)
        self.Ho6 = SnowImg()
        self.add_actor(self.Ho6)
        self.Ho7 = SnowImg()
        self.add_actor(self.Ho7)
        self.Ho.x += 50
        self.Ho.y +=450
        self.Ho2.x += 175
        self.Ho2.y += 150
        self.Ho2.set_width(90)
        self.Ho2.set_height(90)
        self.Ho3.x += 350
        self.Ho3.y += 300
        self.Ho4.x += 620
        self.Ho4.y += 100
        self.Ho5.x += 700
        self.Ho5.y += 470
        self.Ho5.set_width(90)
        self.Ho5.set_height(90)
        self.Ho6.x += 890
        self.Ho6.y += 300
        self.Ho7.x += 1090
        self.Ho7.y += 150
        self.Ho7.set_width(80)
        self.Ho7.set_height(80)
        self.set_on_key_down_listener(self.key_down)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.Ho.rotate_with(delta_time * 25)
        self.Ho2.rotate_with(delta_time * 20)
        self.Ho3.rotate_with(delta_time * 25)
        self.Ho4.rotate_with(delta_time * 25)
        self.Ho5.rotate_with(delta_time * 20)
        self.Ho6.rotate_with(delta_time * 25)
        self.Ho7.rotate_with(delta_time * 20)
        if self.elapsed_time > 1:
            self.Ho.y += delta_time * 5
            self.Ho2.y += delta_time * 5
            self.Ho3.y += delta_time * 5
            self.Ho4.y += delta_time * 5
            self.Ho5.y += delta_time * 5
            self.Ho6.y += delta_time * 5
            self.Ho7.y += delta_time * 5


    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class HavazasScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavazasStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 15:
            self.game.screen = HavasesoScr()

class HavasesoScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesoStage())

class HavasesoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class Ido(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = NapsutesScr()


Ido().run()



