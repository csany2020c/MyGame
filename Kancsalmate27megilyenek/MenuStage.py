
import game

from Kancsalmate27megilyenek.InGameScreen import *
from Kancsalmate27megilyenek.MenuActor import *
from MusicActor import MusicActor



class Stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h

        self.bg = BgActor()
        self.bg.set_size(self.width,self.height)
        self.add_actor(self.bg)


        self.b = MenuActor2()
        self.b.set_size(300,100)
        self.b.x = self.width / 2 - self.b.width / 2
        self.b.y = self.height - self.height * 0.75
        self.add_actor(self.b)
        self.b.set_on_mouse_down_listener(self.start)



        self.c = MenuActor3()
        self.c.set_size(300,100)
        self.c.x =self.width / 2 - self.c.width / 2
        self.c.y = self.height - self.height * 0.75 + self.b.get_height() + self.height * 0.1
        self.add_actor(self.c)

        self.a = MenuActor1()
        self.a.set_size(300, 100)
        self.a.x = self.width / 2 - self.a.width / 2
        self.a.y = self.height - self.height * 0.75 + self.b.get_height() + self.height * 0.1 + self.c.get_height() + self.height*0.1
        self.add_actor(self.a)
        self.a.set_on_mouse_down_listener(self.exit)

        self.musicActor = MusicActor()
        self.musicActor.set_size(75,45)
        self.musicActor.x = self.width - self.musicActor.get_width() - 10
        self.musicActor.y = self.height - self.musicActor.get_height() - 10
        self.add_actor(self.musicActor)
        self.musicActor.set_on_mouse_down_listener(func=self.handleMusic)




    def exit(self, sender, event):
        print(event)
        if event.button == 1:
            quit()

    def handleMusic(self,sender,event):
        if event.button == 1:
            self.musicActor.changeState()

    def start(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(InScreen())




