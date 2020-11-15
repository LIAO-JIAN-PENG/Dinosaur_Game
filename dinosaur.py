import pygame
from pygame.locals import K_SPACE, K_UP, K_DOWN
from main import SCREEN_HEIGHT, SCREEN_WIDTH

pos_x = 100
pos_y = SCREEN_HEIGHT/2

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super(Dinosaur, self).__init__() # inherit pygame.sprite.Sprite
        self.height = 50
        self.width = 50
        self.surf = pygame.image.load("./image/dinosaur_0.png")
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.rect = self.surf.get_rect(bottom = pos_y, right=pos_x)
        self.action = 0 # UP = 1 STOP = 0 FALL = -1
        self.index = 0
    
    # dinosaur move
    def update(self, pressed_keys):
        self.index = self.index % 10000
        self.surf = pygame.image.load("./image/dinosaur_0.png")
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        
        if self.action == 0:
            self.rect = self.surf.get_rect(bottom = pos_y, right=pos_x)
            # JUMP UP (press SPACE or UP)
            if pressed_keys[K_SPACE] or pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
                self.action = 1 # turn to up state
            elif pressed_keys[K_DOWN]:
                if self.index % 20 < 10:
                    self.surf = pygame.image.load("./image/dinosaur_-1.png")
                    self.surf = pygame.transform.scale(self.surf, (self.width+20, self.height-20))
                    self.rect = self.surf.get_rect(bottom = pos_y+3, right=pos_x+10)
                else:
                    self.surf = pygame.image.load("./image/dinosaur_-2.png")
                    self.surf = pygame.transform.scale(self.surf, (self.width+20, self.height-20))
                    self.rect = self.surf.get_rect(bottom = pos_y+3, right=pos_x+10)
                self.index += 1
            # play animation
            elif self.index % 9 < 3:
                self.surf = pygame.image.load("./image/dinosaur_0.png")
                self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
            elif self.index % 9 < 6:
                self.surf = pygame.image.load("./image/dinosaur_1.png")
                self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
            else:
                self.surf = pygame.image.load("./image/dinosaur_2.png")
                self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
            self.index += 1
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
            action = -1
            if self.rect.bottom >= pos_y:
                self.action = 0 # turn to stop state
        elif self.action == 1:
            # Stay a little time(slow the up speed)
            if self.rect.bottom < pos_y - 64:
                self.rect.move_ip(0, -2)
            else:
                self.rect.move_ip(0, -5)
            
            if self.rect.bottom < pos_y - 80:
                self.action = -1  # turn to down state
        elif self.action == -1:
            self.rect.move_ip(0, 5)
            if self.rect.bottom >= pos_y:
                self.action = 0 # turn to stop state
    def show(self):
        print(self.rect)
        