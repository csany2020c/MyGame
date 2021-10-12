from Weathersim.Mandli_Ivett.havazos import *
from Weathersim.Mandli_Ivett.esos import *
from Weathersim.Mandli_Ivett.havasesos import *
from Weathersim.Mandli_Ivett.napsuteses import *
import pygame


def key_down(self, sender, event):
    if event.key == pygame.key_1:
        self.screen = HavazosScreen()


def key_down(self, sender, event):
    if event.key == pygame.key_2:
        self.screen = NapsutesesScreen()


def key_down(self, sender, event):
    if event.key == pygame.key_3:
        self.screen = HavasesosScreen()


def key_down(self, sender, event):
    if event.key == pygame.key_4:
        self.screen = EsosScreen()