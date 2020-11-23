import pygame

class Animate:
    def __init__(self, images, width, height):
        self.images = []
        self.width = width
        self.height = height

        for image in images:
            surf = pygame.image.load(image)
            surf = pygame.transform.scale(surf, (self.width, self.height))
            self.images.append(surf)
    
    def animate(self, flip):
        if flip >= len(self.images):
            return self.images[0]
        return self.images[flip]
        