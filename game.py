import pygame
from pygame.locals import *
from dinosaur import Dinosaur
from tree import Tree
from main import SCREEN_HEIGHT, SCREEN_WIDTH
import random

# basic initialize
pygame.init()

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# clock speed
clock = pygame.time.Clock()

# object appearing frequency
ADDTREE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDTREE, 1200)


# Object
dinosaur = Dinosaur()
trees = pygame.sprite.Group()

## object container
all_sprites = pygame.sprite.Group()
all_sprites.add(dinosaur)

# game running
# running set
running = True

while running:
    for event in pygame.event.get():
        # press key case
        if event.type == KEYDOWN:
            # esc
            if event.key == K_ESCAPE:
                running = False
        # leave
        elif event.type == QUIT:
            running = False
        # ADD Frequency
        elif event.type == ADDTREE:
            # Create new tree per ADDTREE time
            new_tree = Tree()
            trees.add(new_tree)
            all_sprites.add(new_tree)
    
    # object update
    pressed_keys = pygame.key.get_pressed()
    # Update
    dinosaur.update(pressed_keys)
    trees.update()
    
    # screen update
    screen.fill((255, 255, 255))

    dinosaur.show()

    # screen blit
    # screen.blit(dinosaur.surf, dinosaur.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip() # update screen

    clock.tick(60)
