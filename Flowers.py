import pygame.sprite


class Flowers(pygame.sprite.DirtySprite):
    def __init__(self):
        super.__init__()
        flower = pygame.image.load("materials/flower.png").convert_alpha()
        flower_rect = flower.get_rect(center = (10,10))
    #метод що ця штука зникає
    #