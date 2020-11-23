import pygame
import random
from main import SCREEN_WIDTH, GROUND
from dinosaur import Dinosaur
from animation import Animate

class Bird(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(Bird, self).__init__()
        # fly images to animation
        self.fly = ["./image/bird_0.png", "./image/bird_1.png"]
        self.fly_ani = Animate(self.fly, 36, 36) # image, width, height

        self.surf = self.fly_ani.animate(1)
        self.rect = self.surf.get_rect(left = SCREEN_WIDTH, bottom = GROUND - (random.randint(0, 2)*40))
        
        self.speed = 5 + speed
        self.index = 0

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        self.surf = self.fly_ani.animate(int(self.index/10)%2)
        self.index += 1
        self.index %= 1000
        if self.rect.right < 0:
            self.kill() # clean