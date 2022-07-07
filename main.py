import pygame
from sys import exit
import string

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Словесний сад")
clock = pygame.time.Clock()
start_game = True
actual_game = False


# actual_gamelvl1 = False
# actual_gamelvl2 = False
# actual_gamelvl3 = False
# actual_gamelvl4 = False
# actual_gamelvl5 = False
# finish_game = False

class Button1:
    original_y_pos = 10

    def __init__(self, text, width, height, x, y, elevation, type=1):
        # Core attributes
        self.type = type
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = y
        self.original_x_pos = x
        self.ispressed = False

        # if self.ispressed:
        #     self.top_color = '#D74B4B'
        # top rectangle
        self.top_rect = pygame.Rect(x, y, width, height)
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(x, y, width, height)
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
        if self.type == 1:
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = '#D74B4B'
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elevation = 0
                    self.pressed = True
                else:
                    self.dynamic_elevation = self.dynamic_elevation

            else:
                self.dynamic_elevation = self.elevation
                self.top_color = '#475F77'

        if self.type == 2:
            if self.top_rect.collidepoint(mouse_pos) and not self.ispressed:
                self.top_color = '#475F77'
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elevation = 0
                    self.top_color = '#D74B4B'
                    self.pressed = True
                else:
                    self.dynamic_elevation = self.dynamic_elevation
                if self.pressed:
                    self.dynamic_elevation = self.dynamic_elevation
                else:
                    self.top_color = '#D74B4B'
            else:
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

letters = []
test_start_surface = pygame.image.load("C:/Users/User/Downloads/imgonline-com-ua-Resize-DS4h8DhV2K.jpg")
font1 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 60)
font2 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 30)
font3 = pygame.font.Font("C:/Users/User/Downloads/Adigiana_Extreme.ttf", 40)
text_surface1 = font1.render("Вітаємо у словесному саду!", True, "#edeef3")
text_surface2 = font3.render("Оберіть рівень складності гри", True, "#6d6875")
b1 = Button1('level 1', 140, 60, 50, 300, 10, 1)
b2 = Button1('Level 2', 140, 60, 240, 300, 10, 1)
b3 = Button1('Level 3', 140, 60, 430, 300, 10, 1)
b4 = Button1('Level 4', 140, 60, 620, 300, 10, 1)
b5 = Button1('Level 5', 140, 60, 810, 300, 10, 1)
b6 = Button1('Level 6', 140, 60, 840, 300, 10, 2)

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
x = 100
for i in range(26):
        letter_1 = Button1(alphabet[i], 30, 40, x, 100, 5, 2)
        letters.append(letter_1)
        x += 40


# for i in range(14, 26):
#                 x = 20
#                 letter_2 = Button1(alphabet[i], 30, 40, x, 100, 5, 2)
#                 letters.append(letter_2)
#                 x += 10

def redraw_window():
    for letter in letters:
        letter.draw()
    # pygame.display.update()

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
            # b2.draw()
            # b3.draw()
            # b4.draw()
            # b5.draw()

            if b1.pressed:
                start_game = False
                actual_game = True

        elif actual_game:
            screen.fill("Black")
            redraw_window()
            b6.draw()
        pygame.display.update()
        clock.tick(60)
