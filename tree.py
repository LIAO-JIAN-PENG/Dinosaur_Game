import pygame
import random
from main import SCREEN_WIDTH, SCREEN_HEIGHT
from dinosaur import Dinosaur

d = Dinosaur()
d_height = 50
d_width = 50

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super(Tree, self).__init__()
        self.height = random.randint(d_height-30, d_height + 10)
        self.width = random.randint(d_width/2, d_width+10)
        
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(left = SCREEN_WIDTH + random.randint(0, 150), bottom = SCREEN_HEIGHT/2)
        
        self.speed = 5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() # clean