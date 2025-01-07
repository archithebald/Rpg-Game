import pygame, os
from path import Path

from configs.Config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.group = self.groups()[0]
        
        self.frame_index = 0
                
        self.status = "idle"
        self.status_path = os.path.join(CHARACTER_ANIMS_PATH, self.status)
        
        self.image = self.get_frame()
        
        self.resize()
        
        self.rect = self.image.get_rect()
        
    def get_frame(self):
        img_path = os.path.join(self.status_path, f"{self.frame_index}.png")
        return pygame.image.load(img_path)
        
    def resize(self):
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        
    def animate(self):
        if self.frame_index > len(Path(self.status_path).files()):
            self.frame_index = 0
            
        self.frame_index += 1
        
        self.image = self.get_frame()
        
    def draw(self, window):
        self.window = window
        self.window.blit(self.image, self.rect)
    
    def move(self):
        pass
    
    def update(self):
        pass