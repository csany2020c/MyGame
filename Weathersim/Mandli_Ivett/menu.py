from Weathersim.Mandli_Ivett.havazos import *
from Weathersim.Mandli_Ivett.napsuteses import *
from Weathersim.Mandli_Ivett.havasesos import *
from Weathersim.Mandli_Ivett.esos import *


def key_down(self, sender, event):
    if event.key == pygame.K_1:
        self.screen = HavazosScreen()


def key_down(self, sender, event):
    if event.key == pygame.K_2:
        self.screen = NapsutesesScreen()


def key_down(self, sender, event):
    if event.key == pygame.K_3:
        self.screen = HavasesosScreen()


def key_down(self, sender, event):
    if event.key == pygame.K_4:
        self.screen = HavazosScreen()
