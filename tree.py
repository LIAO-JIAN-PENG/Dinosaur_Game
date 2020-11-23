import pygame
import random
from main import SCREEN_WIDTH, GROUND

class Tree(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(Tree, self).__init__()
        self.scales = [(18, 36), (25, 38), (45, 36), (54, 40), (27, 54)]
        self.images = ["cactusSmall0000.png", "cactusSmall0002.png", "cactusSmall0003.png", "cactusSmallMany0000.png", "cactusBig0000.png"]
        self.surfs = []
        for i in range(5):
            surf = pygame.image.load("image/"+self.images[i])
            surf = pygame.transform.scale(surf, self.scales[i])
            self.surfs.append(surf)
        
        self.surf = self.surfs[random.randint(0, 4)]
        self.rect = self.surf.get_rect(left = SCREEN_WIDTH + random.randint(0, 200), bottom = GROUND)
        
        self.speed = 5 + int(speed)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() # clean