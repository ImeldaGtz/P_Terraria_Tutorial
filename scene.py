import pygame
from globals import *
from sprite import Entity
from player import Player
from texture_data import solo_texture_data, atlas_texture_data

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.solo_textures = self.gen_solo_textures()
        self.atlas_textures = self.gen_atlas_textures("res/atlas.png")

        self.sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.entity = Entity([self.sprites], image=self.atlas_textures['grass'])
        Entity([self.sprites], position=(100,100) ,image=self.atlas_textures['dirt'])
        Entity([self.sprites], position=(200, 200) ,image=self.atlas_textures['stone'])
        Entity([self.sprites], position=(300, 300), image=self.solo_textures['player_static'])
        self.player = Player([self.sprites])

    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)

    def gen_solo_textures(self) -> dict:
        textures = {}

        for name, data in solo_texture_data.items():
            textures[name] = pygame. transform.scale( pygame.image.load( data['filepath'] ).convert_alpha(), (data['size']))
        
        return textures
    
    def gen_atlas_textures(self, filepath) -> dict:
        textures ={}
        atlas_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(), (TILESIZE*12, TILESIZE*12))

        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(atlas_img, pygame.Rect( data['position'][0]*TILESIZE,
                                                                              data['position'][1]*TILESIZE, 
                                                                              data['size'][0], 
                                                                              data['size'][1] ))
        return textures
    
    def gen_world(self):
        pass