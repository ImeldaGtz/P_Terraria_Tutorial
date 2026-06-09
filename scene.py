import pygame
from globals import *
from sprite import Entity

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites])

    def update(self):
        self.sprites.update()
    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)
