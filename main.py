import pygame           
import sys              
from globals import *   
from scene import Scene   

class Game: 
    def __init__(self): #? Constructor
        pygame.init()   
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("Py-rraria")
        
        self.clock = pygame.time.Clock()

        self.running = True
        self.scene = Scene(self)

    def run(self):      #? Para correr
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):       #? Para actualizar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.scene.update()
        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):         #? Para dibujar
        self.scene.draw()
        
    def close(self):        #? Para cerrar
        pygame.quit()
        sys.exit()

if __name__ == "__main__":  #? Para ejecutarlo
    game = Game()
    game.run()