import pygame
import random
from main import SCREEN_WIDTH, GROUND

class Ground(pygame.sprite.Sprite):
    def __init__(self, loc):
        super(Ground, self).__init__()
        self.surf = pygame.image.load("image/ground.png")
        self.rect = self.surf.get_rect(center=(0, GROUND-23), left = loc)
        self.speed = 5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() # clean