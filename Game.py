import pygame
pygame.init()

from configs.Config import *

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        
        self.running = True
        self.dt = 0
        
        self.clock = pygame.time.Clock()
        
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.dt = self.clock.tick(FRAME_RATE) / 1000
            
            pygame.display.update()
            
if __name__ == "__main__":
    game = Game().loop()