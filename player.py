import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple, parameters:dict) -> None:
        super().__init__(groups)
        self.image = image
        # self.image.fill('saddlebrown')
        self.rect = self.image.get_rect(topleft = position)
        self.velocity = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x = -1
        if keys[pygame.K_d]:
            self.velocity.x = 1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = 0

    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def update(self):
        self.input()
        self.move()