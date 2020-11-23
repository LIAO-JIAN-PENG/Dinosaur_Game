import pygame
import random
from main import SCREEN_WIDTH, GROUND

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("image/cloud.png")
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(left = SCREEN_WIDTH, bottom = GROUND - random.randint(100, 220))
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() # clean