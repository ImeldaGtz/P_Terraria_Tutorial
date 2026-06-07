import pygame           # Importa librería para crear juegos
import sys              # Importa librería para manipular el sistema
from globals import *   # Importa el archivo con variables globales

class Game: # Clase principal, de donde funciona todo
    def __init__(self): #? Constructor
        pygame.init()   # Inicia pygame
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # Crea una ventana indicando dimensiones de la misma
        self.clock = pygame.time.Clock()    # Implementa reloj interno

        self.running = True # Al crearse se indica que está corriendo
    def run(self):      #? Para correr
        while self.running: # Mientras, en efecto, esté corriendo...
            self.update()   # Se va a #*actualizar
            self.draw()     # Se va a #*dibujar en pantalla lo que sea necesario
        self.close()        # Si no está corriendo se va a #*cerrar
    def update(self):       #? Para actualizar
        for event in pygame.event.get():    # Por cada evento encontrado en la lista de eventos
            if event.type == pygame.QUIT:   # Si dicho evento es tipo QUIT...
                self.running = False        # Ya no corre
        pygame.display.update()             # Al terminar de verificar el estado de running, se actualiza la pantalla
        self.clock.tick(FPS)                # Se indican los FPS
    def draw(self):         #? Para dibujar
        self.screen.fill('lightblue')   # Por ahora solo llena la pantalla de azul claro...
    def close(self):        #? Para cerrar
        pygame.quit()       # Cierra pygame
        sys.exit()          # Cierra el sistema

if __name__ == "__main__":  # Entiendo que si el nombre del archivo es main...   #? Para ejecutarlo
    game = Game()           # Crea variable de clase Game
    game.run()              # Corre el jueguito