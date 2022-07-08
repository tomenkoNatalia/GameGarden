import pygame
from sys import exit
import random

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Словесний сад")
clock = pygame.time.Clock()
start_game = True
level1 = False
level2 = False
level3 = False
level4 = False
level5 = False
lost = False
won = False
rules = False


class Button:
    def __init__(self, text, width, height, x, y, elevation, type=1):
        # Core attributes
        self.letter = text
        self.type = type
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = y
        self.original_x_pos = x

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
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = '#475F77'
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elevation = 0
                    self.top_color = '#D74B4B'
                    self.pressed = True
                    word.check_letter(self.letter)
                else:
                    self.dynamic_elevation = self.dynamic_elevation
                if self.pressed:
                    self.dynamic_elevation = self.dynamic_elevation

                else:
                    self.top_color = '#D74B4B'
            else:
                self.top_color = '#475F77'


class GameWindow:
    def __init__(self, back, colorText, text, field, xtext, ytext, xfield, yfield, type=1):
        self.background = back
        self.text = font1.render(text, True, colorText)
        self.text_rect = pygame.Rect(xtext, ytext, 100, 100)
        self.field = pygame.image.load(field)
        self.field_rect = pygame.Rect(xfield, yfield, 10, 300)
        self.type = type

    def draw(self):
        screen.fill(self.background)
        screen.blit(self.field, self.field_rect)
        screen.blit(self.text, self.text_rect)
        word.draw()
        if self.type == 1:
            redraw_window()
            go_back_button.draw()
        if self.type == 2:
            play_again_button.draw()
            exit_button.draw()


class Word:
    def __init__(self, level):
        self.level = level
        self.word = self.select_word()
        self.guessed = ''
        self.word_rect = pygame.Rect(100, 400, 100, 100)

    def draw(self):
        screen.blit(font1.render(self.space_out_word(), True, "#FFFFFF"), self.word_rect)

    def select_word(self):
        if self.level == 1:
            file = open('materials/words5.txt', encoding="utf8")
        elif self.level == 4 or self.level == 5:
            file = open('materials/words12.txt', encoding="utf8")
        else:
            file = open('materials/words8.txt', encoding="utf8")
        f = file.readlines()
        rand = random.randrange(0, len(f) - 1)

        return f[rand][:-1]

    def space_out_word(self):
        spaced_word = ''
        for letter in self.word:
            if letter in self.guessed:
                spaced_word += letter + ' '
            else:
                spaced_word += '_ '
        return spaced_word

    def check_letter(self, letter):
        contains = False
        for x in self.word:
            if x == letter:
                contains = True
        if contains:
            self.guessed += letter
            print(self.guessed)


def redraw_window():
    for letter in letters:
        letter.draw()


# шрифти налаштування
newFont = "materials/Adigiana_Extreme.ttf"
font1 = pygame.font.Font(newFont, 60)
font2 = pygame.font.Font(newFont, 30)
font3 = pygame.font.Font(newFont, 40)

# стартове вікно налаштування (по ідеї там якось можна кнопки об'єднати у групу щоб не виводити кожну окремо)
test_start_surface = pygame.image.load("materials/startpic.jpg")
text_surface1 = font1.render("Вітаємо у словесному саду!", True, "#edeef3")
text_surface2 = font3.render("Оберіть рівень складності гри", True, "#6d6875")
level_buttons = list()
level_buttons.append(Button('Рівень 1', 140, 60, 50, 300, 10, 1))
level_buttons.append(Button('Рівень 2', 140, 60, 240, 300, 10, 1))
level_buttons.append(Button('Рівень 3', 140, 60, 430, 300, 10, 1))
level_buttons.append(Button('Рівень 4', 140, 60, 620, 300, 10, 1))
level_buttons.append(Button('Рівень 5', 140, 60, 810, 300, 10, 1))

rules_button = Button('Правила гри', 200, 80, 700, 400, 10, 1)
go_back_button = Button('Назад', 140, 50, 810, 400, 10, 1)
play_again_button = Button('Грати знову', 140, 50, 50, 400, 10, 1)
exit_button = Button('Вийти з гри', 140, 50, 810, 400, 10, 1)

# вікна на рівні
lvl1 = GameWindow("#EAB595", "#79616F", "Рівень 1", "materials/lvl1.1.jpg", 350, 1, 30, 70, 1)
lvl2 = GameWindow("#EAB595", "#79616F", "Рівень 2", "materials/lvl2.1.jpg", 350, 1, 30, 70, 1)
lvl3 = GameWindow("#EAB595", "#79616F", "Рівень 3", "materials/lvl3.1.jpg", 350, 1, 30, 70, 1)
lvl4 = GameWindow("#EAB595", "#79616F", "Рівень 4", "materials/lvl4.1.jpg", 350, 1, 30, 70, 1)
lvl5 = GameWindow("#EAB595", "#79616F", "Рівень 5", "materials/lvl5.1.jpg", 350, 1, 30, 70, 1)
lost1 = GameWindow("#EAB595", "#79616F", "О ні, ви програли((", "materials/lost1.jpg", 350, 1, 0, 0, 2)
won1 = GameWindow("#EAB595", "#79616F", "Вітаю, ви виграли!", "materials/win1.jpg", 300, 1, 0, 0, 2)
# для правил
text_rules1 = font1.render("Правила гри", True, "#edeef3")
text_rules2 = font2.render("Тут щось буде \n тут щось буде \n тут багато чого буде \n  ураура правила клас", True,
                           "#edeef3")
# кнопки букви розташування
letters = []
alphabet = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

x_position = 710
y_position = 100

for i in range(7):
    letters.append(Button(alphabet[i], 30, 40, x_position, y_position, 5, 2))
    letters.append(Button(alphabet[i + 7], 30, 40, x_position, y_position + 50, 5, 2))
    letters.append(Button(alphabet[i + 14], 30, 40, x_position, y_position + 100, 5, 2))
    letters.append(Button(alphabet[i + 21], 30, 40, x_position, y_position + 150, 5, 2))
    if i < 5:
        letters.append(Button(alphabet[i + 28], 30, 40, x_position, y_position + 200, 5, 2))
    x_position += 40

# Сам процес гри
# можливо його можна оптимізувати, але воно працює і так, і на цьому дякую
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if start_game:
            screen.blit(test_start_surface, (0, 0))
            screen.blit(text_surface1, (200, 50))
            screen.blit(text_surface2, (300, 200))
            for level_button in level_buttons:
                level_button.draw()
            rules_button.draw()

            # won.draw()  перевірка вікна виграшу і програшу
            # lost.draw()
            if level_buttons[0].pressed:
                start_game = False
                level1 = True
                word = Word(1)
            elif level_buttons[1].pressed:
                start_game = False
                level2 = True
                word = Word(2)
            elif level_buttons[2].pressed:
                start_game = False
                level3 = True
            elif level_buttons[3].pressed:
                start_game = False
                level4 = True
                word = Word(3)
            elif level_buttons[4].pressed:
                start_game = False
                level5 = True
                word = Word(4)
            elif rules_button.pressed:
                start_game = False
                rules = True
                word = Word(5)

        elif level1:
            lvl1.draw()

        elif level2:
            lvl2.draw()

        elif level3:
            lvl3.draw()

        elif level4:
            lvl4.draw()

        elif level5:
            lvl5.draw()

        elif lost:
            lost1.draw()

        elif won:
            won1.draw()

        elif rules:
            screen.fill("#D87F81")
            screen.blit(text_rules1, (250, 10))
            screen.blit(text_rules2, (50, 80))
            go_back_button.draw()

        pygame.display.update()
        clock.tick(60)
