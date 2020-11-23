import pygame
from pygame.locals import *
from dinosaur import Dinosaur, Contact
from tree import Tree
from bird import Bird
from cloud import Cloud
from background import Ground
from main import SCREEN_HEIGHT, SCREEN_WIDTH
import random

# basic initialize
pygame.init()

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# clock speed
clock = pygame.time.Clock()

# # object appearing frequency
# ADDTREE = pygame.USEREVENT + 1
# pygame.time.set_timer(ADDTREE, 1200)

# # object appearing frequency
# ADDBIRD = pygame.USEREVENT + 3
# pygame.time.set_timer(ADDBIRD, 1200)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1200)

ADDCLOUD = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCLOUD, 3000)

ADDGROUND = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCLOUD, 3600)


# Object
dinosaur = Dinosaur()
contact = Contact()
trees = pygame.sprite.Group()
birds = pygame.sprite.Group()
clouds = pygame.sprite.Group()
grounds = pygame.sprite.Group()

## object container
all_sprites = pygame.sprite.Group()
all_sprites.add(dinosaur)
all_sprites.add(contact)

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
        elif event.type == ADDGROUND:
            new_ground = Ground(SCREEN_WIDTH)
            grounds.add(new_ground)
            all_sprites.add(new_ground)
        elif event.type == ADDENEMY:
            pygame.time.set_timer(ADDENEMY, 1200-int(pygame.time.get_ticks()/1000))
            if random.randint(0, 200) > 40:
                # Create new tree per ADDTREE time
                new_tree = Tree(pygame.time.get_ticks()/50000)
                trees.add(new_tree)
                all_sprites.add(new_tree)
            else:
                new_bird = Bird(pygame.time.get_ticks()/50000)
                birds.add(new_bird)
                all_sprites.add(new_bird)
        if event.type == ADDCLOUD:
            if random.randint(0, 10) > 5:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
            
    
    # object update
    pressed_keys = pygame.key.get_pressed()
    # Update
    if pygame.sprite.spritecollideany(contact, trees):
        dinosaur.die()
    elif  pygame.sprite.spritecollideany(contact, birds):
        dinosaur.die()
    else:
        grounds.update()
        dinosaur.update(pressed_keys)
        contact.update(dinosaur.rect.center[0], dinosaur.rect.bottom, dinosaur.squat)
        trees.update()
        birds.update()
        clouds.update()
    
    # screen update
    screen.fill((255, 255, 255))

    # screen blit
    # screen.blit(dinosaur.surf, dinosaur.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip() # update screen

    clock.tick(60)
