import pygame
from sys import exit

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Словесний сад")
clock = pygame.time.Clock()
start_game = True


# actual_gamelvl1 = False
# actual_gamelvl2 = False
# actual_gamelvl3 = False
# actual_gamelvl4 = False
# actual_gamelvl5 = False
# finish_game = False

class Button1:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text_surf = font2.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
        # if self.pressed == True:
        #     screen.fill("Yellow")

        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


# class GameWindow:
#     def __init__(self, image, text, field, pos):
#         self.back = pygame.image.load(image).convert_alpha()
#         self.text_surf = font2.render(text, True, '#FFFFFF')
#         self.position = pos[1]
#         self.text_rect = pygame.Rect(pos, (100, 100))
#         self.field = pygame.image.load(field).get_rect()
#         self.field_rect = self.field.get_rect()
#         self.lines = font2.render("-", True, '#FFFFFF')
#     def draw(self):
#         #lines logic



test_start_surface = pygame.image.load("C:/Users/User/Downloads/imgonline-com-ua-Resize-DS4h8DhV2K.jpg")
font1 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 60)
font2 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 30)
font3 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 40)
text_surface1 = font1.render("Вітаємо у словесному саду!", True, "#edeef3")
text_surface2 = font3.render("Оберіть рівень складності гри", True, "#6d6875")
b1 = Button1('Level 1', 140, 60, (50, 300), 10)
b2 = Button1('Level 2', 140, 60, (240, 300), 10)
b3 = Button1('Level 3', 140, 60, (430, 300), 10)
b4 = Button1('Level 4', 140, 60, (620, 300), 10)
b5 = Button1('Level 5', 140, 60, (810, 300), 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # draw start window
        # draw game window
        # draw lose and win window
        if start_game:
            screen.blit(test_start_surface, (0, 0))
            screen.blit(text_surface1, (200, 50))
            screen.blit(text_surface2, (300, 200))
            b1.draw()
            b2.draw()
            b3.draw()
            b4.draw()
            b5.draw()

            if b1.pressed:
                start_game = False

        else:
            screen.fill("Yellow")

        pygame.display.update()
        clock.tick(60)
