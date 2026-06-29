import pygame
from globals import *
from world.sprite import Entity, Mob
from world.player import Player
from world.texture_data import solo_texture_data, atlas_texture_data
from opensimplex import OpenSimplex
from camera import Camera

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.solo_textures = self.gen_solo_textures()
        self.atlas_textures = self.gen_atlas_textures("res/atlas.png")

        self.sprites = Camera()
        self.blocks = pygame.sprite.Group()
        
        # self.entity = Entity([self.sprites], image=self.atlas_textures['grass'])
        # Entity([self.sprites], position=(100,100) ,image=self.atlas_textures['dirt'])
        # Entity([self.sprites], position=(200, 200) ,image=self.atlas_textures['stone'])

        # # Floor
        # Entity([self.sprites, self.blocks], pygame.Surface((TILESIZE*10, TILESIZE)) , position= (400,550))

        self.player = Player([self.sprites], self.solo_textures['player_static'], (SCREENWIDTH//2, SCREENHEIGHT//9), parameters={'block_group': self.blocks, 'textures': self.atlas_textures})

        Mob([self.sprites], self.solo_textures['zombie_static'], (800, -500), parameters={'block_group': self.blocks, 
                                                                                          'player': self.player})
        self.gen_world()

    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.player, self.app.screen)

    def gen_solo_textures(self) -> dict:
        textures = {}

        for name, data in solo_texture_data.items():
            textures[name] = pygame. transform.scale( pygame.image.load( data['filepath'] ).convert_alpha(), (data['size']))
        
        return textures
    
    def gen_atlas_textures(self, filepath) -> dict:
        textures ={}
        atlas_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(), (TILESIZE*36, TILESIZE*36))

        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(atlas_img, pygame.Rect( data['position'][0]*TILESIZE,
                                                                              data['position'][1]*TILESIZE, 
                                                                              data['size'][0], 
                                                                              data['size'][1] ))
        return textures
    
    def gen_world(self):
        noise_gen = OpenSimplex(seed=32500000)

        heightmap = []
        for y in range(60):
            noise_value = noise_gen.noise2( y * 0.05, 0)
            height = int( (noise_value +1) * 3 + 5 )
            heightmap.append(height)

        for x in range(len(heightmap)):
            for y in range(heightmap[x]):
                offset = 5-y + 5
                texture = self.atlas_textures['dirt']
                if y == heightmap[x] - 1:
                    texture = self.atlas_textures['grass']

                if y < heightmap[x] - 5:
                    texture = self.atlas_textures['stone']
                Entity( [self.sprites, self.blocks], texture, (x*TILESIZE, offset*TILESIZE) )