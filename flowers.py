import pygame


class Flowers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        flw1 = pygame.image.load("materials/flowerpos1.png").convert_alpha()
        flw2 = pygame.image.load("materials/flowerpos2.png").convert_alpha()
        flw3 = pygame.image.load("materials/flowerpos3.png").convert_alpha()
        flw4 = pygame.image.load("materials/flowerpos4.png").convert_alpha()
        self.flowerAnimation = [flw1, flw2, flw3, flw4]
        self.flowerIndex = 0
        self.x = x
        self.y = y

        self.image = self.flowerAnimation[self.flowerIndex]
        self.rect = self.image.get_rect(center=(x, y))

    def animation(self):
        self.flowerIndex += 0.2
        if self.flowerIndex >= len(self.flowerAnimation):
            self.flowerIndex = 0
        self.image = self.flowerAnimation[int(self.flowerIndex)]

    def update(self):
        self.animation()

    # метод що ця штука зникає
    #
