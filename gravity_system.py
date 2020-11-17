import pygame
from pygame.locals import *

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 1000


pygame.init()

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# clock speed
clock = pygame.time.Clock()

# ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.grav = 0.7
        self.vel = 0
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 65, 100))
        self.index = 0
        self.rect = self.surf.get_rect(center = (self.x, 0), bottom = SCREEN_HEIGHT)

    def update(self, pressed_key):
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.vel = 0
            self.rect = self.surf.get_rect(center = (self.x, 0), bottom = SCREEN_HEIGHT)
        # animation control
        elif self.rect.bottom != SCREEN_HEIGHT:
            self.vel = self.vel + self.grav
            
        
        if pressed_key[K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT:
                self.vel = 15
            else:
                self.rect = self.surf.get_rect(center = (self.x, 0), bottom = SCREEN_HEIGHT)
                self.rect.bottom = SCREEN_HEIGHT
                self.vel = 0
        elif pressed_key[K_SPACE] or pressed_key[K_UP]:
            if self.vel > 0: # if falling don't jump
                self.vel = self.vel
            elif self.vel > -6 and self.vel < 0:
                self.vel = self.vel
            elif self.rect.bottom > SCREEN_HEIGHT - 80:
                self.vel = -7
            elif self.vel == 0 and self.rect.bottom == SCREEN_HEIGHT - 80:
                self.vel = -12

        self.rect.move_ip(0, self.vel)
        # animation flip
        self.index += 0.3
        self.index %= 6
        

# self
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