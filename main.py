global SCREEN_WIDTH
global SCREEN_HEIGHT

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400

import pygame
from pygame.locals import *
from animation import Animate

pygame.init()

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# clock speed
clock = pygame.time.Clock()

# ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.images = ["./image/dinosaur_0.png", "./image/dinosaur_1.png", "./image/dinosaur_2.png"]
        self.animation = Animate(self.images)
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.grav = 0.7
        self.vel = 0
        # self.surf = pygame.Surface((50, 50))
        # self.surf.fill((0, 65, 100))
        self.index = 0
        self.surf = self.animation.animate(0)
        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def update(self, pressed_key):
        if self.rect.bottom > SCREEN_HEIGHT:
            self.vel = 0
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.bottom != SCREEN_HEIGHT:
            self.vel = self.vel + self.grav
        
        if pressed_key[K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT:
                ball.vel = 15
            else:
                ball.vel = 0
        elif pressed_key[K_SPACE] or pressed_key[K_UP]:
            if self.vel > 0: # if falling don't jump
                ball.vel = ball.vel
            elif self.vel > -6 and self.vel < 0:
                ball.vel = ball.vel
            elif self.rect.bottom > SCREEN_HEIGHT - 80:
                ball.vel = -7
            elif self.vel == 0 and self.rect.bottom == SCREEN_HEIGHT - 80:
                ball.vel = -12
        

        self.rect.move_ip(0, self.vel)
        self.surf = self.animation.animate(int(self.index))
        self.index += 0.5
        self.index %= 3
        

# Ball
ball = Ball()

running = True

while running:
    for event in pygame.event.get():
        # press key case
        if event.type == KEYDOWN:
            # esc
            if event.key == K_ESCAPE:
                running = False
            # elif event.key == K_SPACE:
            #     ball.vel -= 5
            
        # leave
        elif event.type == QUIT:
            running = False

    # pressed key
    pressed_keys = pygame.key.get_pressed()

    # object
    ball.update(pressed_keys)
    
    # screen update
    screen.fill((255, 255, 255))

    screen.blit(ball.surf, ball.rect)
    
    pygame.display.flip() # update screen

    clock.tick(60)