import pygame
from sys import exit
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Словесний сад")
clock = pygame.time.Clock()

test_start_surface = pygame.image.load("C:/Users/User/Downloads/imgonline-com-ua-Resize-DS4h8DhV2K.jpg")
font1 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 60)
font2 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 30)
font3 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 62)
text_surface1 = font1.render("Вітаємо у словесному саду!", True, "#edeef3")
text_surface2 = font2.render("Оберіть рівень складності гри", True, "#6d6875")
text_surface3 = font3.render("Вітаємо у словесному саду!", True, "Black")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# draw start window
# draw game window
# draw lose and win window
        screen.blit(test_start_surface, (0, 0))
        screen.blit(text_surface3, (190, 40))
        screen.blit(text_surface1, (200, 50))
        screen.blit(text_surface2, (330, 200))


        pygame.display.update()
        clock.tick(60)
