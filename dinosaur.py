import pygame
from pygame.locals import K_SPACE, K_UP, K_DOWN
from main import SCREEN_HEIGHT, SCREEN_WIDTH, GROUND
from animation import Animate

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super(Dinosaur, self).__init__() # inherit pygame.sprite.Sprite
        # self position
        self.x = 200
        self.y = GROUND/2

        # jump images to animation
        self.run = ["./image/dinosaur_0.png", "./image/dinosaur_1.png", "./image/dinosaur_2.png"]
        self.run_ani = Animate(self.run, 50, 50) # image, width, height
        # squat images to animation
        self.squat = ["./image/dinosaur_-1.png", "./image/dinosaur_-2.png"]
        self.squat_ani = Animate(self.squat, 70, 30) # image, width, height

        # physic attributes
        self.grav = 0.7
        self.vel = 0

        # self squat state for contact detection
        self.squat = False

        # time counter
        self.index = 0
        # initial animation state
        self.surf = self.run_ani.animate(0)
        self.rect = self.surf.get_rect(center = (self.x, 0), bottom = GROUND)
    
    # dinosaur move
    def update(self, pressed_key):
        # for contact detection
        self.squat = False
        
        if self.rect.bottom >= GROUND:
            self.vel = 0
            self.surf = self.run_ani.animate(int(self.index) % 3)
            self.rect = self.surf.get_rect(center = (self.x, 0), bottom = GROUND)
        # animation control
        elif self.rect.bottom != GROUND:
            self.vel = self.vel + self.grav
            self.surf = self.run_ani.animate(0)
            
        
        if pressed_key[K_DOWN]:
            if self.rect.bottom < GROUND:
                self.vel = 10
            else:
                self.surf = self.squat_ani.animate(int(self.index/1.8)%2)
                self.rect = self.surf.get_rect(center = (self.x, 0), bottom = GROUND)
                self.rect.bottom = GROUND
                self.vel = 0
                self.squat = True # contact detection
        elif pressed_key[K_SPACE] or pressed_key[K_UP]:
            if self.vel > 0: # if falling don't jump
                self.vel = self.vel
            elif self.vel > -6 and self.vel < 0:
                self.vel = self.vel
            elif self.rect.bottom > GROUND - 70:
                self.vel = -7
            elif self.vel == 0 and self.rect.bottom == GROUND - 70:
                self.vel = -12
            self.surf = self.run_ani.animate(0)

        self.rect.move_ip(0, self.vel)
        # animation flip
        self.index += 0.3
        self.index %= 6

class Contact(pygame.sprite.Sprite):
    def __init__(self):
        super(Contact, self).__init__() # inherit pygame.sprite.Sprite
        # self position
        self.surf = pygame.Surface((25, 50))
        self.rect = self.surf.get_rect(center = (200, 0), bottom = GROUND)
    def update(self, dino_x, dino_y, squat_state):
        self.rect = self.surf.get_rect(center = (dino_x, 0), bottom = dino_y)
        if squat_state:
            self.surf = pygame.Surface((65, 30))
        else:
            self.surf = pygame.Surface((25, 50))
        self.surf.set_colorkey((0, 0, 0))
          