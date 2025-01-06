import pygame, os

from configs.Config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.group = self.groups()[0]
        
        self.frame_index = 0
        self.image = self.get_frame()
        
        self.rect = self.image.get_rect()
        
        self.status = "idle"
        
    def get_frame(self):
        return pygame.image.load(os.path.join(CHARACTER_ANIMS_PATH, self.status, str(self.frame_index)))
        
    def animate(self):
        pass
        
    def draw(self, window):
        self.window = window
        self.window.blit(self.image, self.rect)
    
    def move(self):
        pass
    
    def update(self):
        pass