import pygame
from sys import exit
import random
from flowers import Flowers

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

    def __init__(self, back, colorText, text, field, xtext, ytext, xfield, yfield, flowers, type=1):
        self.background = back
        self.text = font1.render(text, True, colorText)
        self.text_rect = pygame.Rect(xtext, ytext, 100, 100)
        self.field = pygame.image.load(field)
        self.field_rect = pygame.Rect(xfield, yfield, 10, 300)
        self.type = type
        self.flowers = flowers

    def draw(self):
        screen.fill(self.background)
        screen.blit(self.field, self.field_rect)
        screen.blit(self.text, self.text_rect)
        if self.type == 1:
            redraw_window()
            go_back_button.draw()
            word.draw_spaced()
            # drawflwrs()
        if self.type == 2:
            play_again_button.draw()
            exit_button.draw()
            word.draw_full()


class Word:
    def __init__(self, level):
        self.level = level
        self.word = self.select_word()
        self.guessed = ''
        self.spaced_word_rect = pygame.Rect(100, 400, 100, 100)
        self.full_word_rect = pygame.Rect(200, 400, 100, 100)
        self.errors = 0

    def draw_spaced(self):
        screen.blit(font1.render(self.space_out_word(), True, "#FFFFFF"), self.spaced_word_rect)

    def draw_full(self):
        screen.blit(font1.render('Слово раунду: ' + self.word, True, "#FFFFFF"), self.full_word_rect)

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
        else:
            self.errors += 1


groupLvl1 = pygame.sprite.Group()
groupLvl2 = pygame.sprite.Group()
groupLvl3 = pygame.sprite.Group()
groupLvl4 = pygame.sprite.Group()
groupLvl5 = pygame.sprite.Group()

x = 40
for i in range(5):
    groupLvl1.add(Flowers(40 + x, 120), Flowers(40 + x, 220), Flowers(40 + x, 320))
    x += 120
x = 40
for i in range(4):
    groupLvl2.add(Flowers(40 + x, 120), Flowers(40 + x, 220), Flowers(40 + x, 320))
    x += 180
x = 40
for i in range(3):
    groupLvl3.add(Flowers(40 + x, 120), Flowers(40 + x, 220), Flowers(40 + x, 320))
    groupLvl4.add(Flowers(40 + x, 120), Flowers(40 + x, 220), Flowers(350, 320))
    x += 270
x = 40
for i in range(2):
    groupLvl5.add(Flowers(40+x, 120), Flowers(40 + x, 300), Flowers(580, 200))
    x += 270


def redraw_window():
    for letter in letter_buttons:
        letter.draw()


# шрифти налаштування
newFont = "materials/Adigiana_Extreme.ttf"
font1 = pygame.font.Font(newFont, 60)
font2 = pygame.font.Font(newFont, 30)
font3 = pygame.font.Font(newFont, 40)

# стартове вікно налаштування
test_start_surface = pygame.image.load("materials/startpic.jpg")
text_surface1 = font1.render("Вітаємо у словесному саду!", True, "#edeef3")
text_surface2 = font3.render("Оберіть рівень складності гри", True, "#6d6875")
level_buttons = list()
level_buttons.append(Button('Рівень 1', 140, 60, 50, 300, 10, 1))
level_buttons.append(Button('Рівень 2', 140, 60, 240, 300, 10, 1))
level_buttons.append(Button('Рівень 3', 140, 60, 430, 300, 10, 1))
level_buttons.append(Button('Рівень 4', 140, 60, 620, 300, 10, 1))
level_buttons.append(Button('Рівень 5', 140, 60, 810, 300, 10, 1))

rules_button = Button('Правила гри', 200, 80, 400, 400, 10, 1)
go_back_button = Button('Назад', 140, 50, 810, 400, 10, 1)
play_again_button = Button('Грати знову', 140, 50, 50, 400, 10, 1)
exit_button = Button('Вийти з гри', 140, 50, 810, 400, 10, 1)

# вікна на рівні
lvl1 = GameWindow("#EAB595", "#79616F", "Рівень 1", "materials/lvl1.1.jpg", 350, 1, 30, 70, 15, 1)
lvl2 = GameWindow("#EAB595", "#79616F", "Рівень 2", "materials/lvl2.1.jpg", 350, 1, 30, 70, 12, 1)
lvl3 = GameWindow("#EAB595", "#79616F", "Рівень 3", "materials/lvl3.1.jpg", 350, 1, 30, 70, 12, 1)
lvl4 = GameWindow("#EAB595", "#79616F", "Рівень 4", "materials/lvl4.1.jpg", 350, 1, 30, 70, 10, 1)
lvl5 = GameWindow("#EAB595", "#79616F", "Рівень 5", "materials/lvl5.1.jpg", 350, 1, 30, 70, 8, 1)
lost1 = GameWindow("#EAB595", "#79616F", "О ні, ви програли((", "materials/lost1.jpg", 350, 1, 0, 0, 2)
won1 = GameWindow("#EAB595", "#79616F", "Вітаю, ви виграли!", "materials/win1.jpg", 300, 1, 0, 0, 2)

# для правил
text_rules1 = font1.render("Правила гри", True, "#edeef3")
rules_array = open('materials/rules.txt', encoding="utf8").readlines()
rules_text = ""
for rule in rules_array:
    rules_text += '\n' + rule
text_rules2 = font2.render(rules_text, True, "#edeef3")
# якось зробити перенос на інший рядок

# кнопки букви розташування
letter_buttons = []
alphabet = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

x_position = 710
y_position = 100

for i in range(7):
    letter_buttons.append(Button(alphabet[i], 30, 40, x_position, y_position, 5, 2))
    letter_buttons.append(Button(alphabet[i + 7], 30, 40, x_position, y_position + 50, 5, 2))
    letter_buttons.append(Button(alphabet[i + 14], 30, 40, x_position, y_position + 100, 5, 2))
    letter_buttons.append(Button(alphabet[i + 21], 30, 40, x_position, y_position + 150, 5, 2))
    if i < 5:
        letter_buttons.append(Button(alphabet[i + 28], 30, 40, x_position, y_position + 200, 5, 2))
    x_position += 40


def reset_window():
    screen.blit(test_start_surface, (0, 0))
    screen.blit(text_surface1, (200, 50))
    screen.blit(text_surface2, (300, 200))
    for level_button in level_buttons:
        level_button.draw()
    rules_button.draw()
    for letter in letter_buttons:
        letter.pressed = False
        letter.dynamic_elevation = 10
        # повернути розмір кнопок

# Сам процес гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if start_game:
            reset_window()
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
                word = Word(3)
            elif level_buttons[3].pressed:
                start_game = False
                level4 = True
                word = Word(4)
            elif level_buttons[4].pressed:
                start_game = False
                level5 = True
                word = Word(5)
            elif rules_button.pressed:
                start_game = False
                rules = True

        elif level1:
            lvl1.draw()
            groupLvl1.draw(screen)
            groupLvl1.update()

            level_buttons[0].pressed = False
            if word.errors >= 15:
                level1 = False
                lost = True

            if '_' not in word.space_out_word():
                level1 = False
                won = True

            if go_back_button.pressed:
                level1 = False
                start_game = True
                reset_window()
                go_back_button.pressed = False

        elif level2:
            lvl2.draw()
            groupLvl2.draw(screen)
            groupLvl2.update()
            level_buttons[1].pressed = False
            if word.errors >= 12:
                level2 = False
                lost = True

            if '_' not in word.space_out_word():
                level2 = False
                won = True

            if go_back_button.pressed:
                level2 = False
                start_game = True
                reset_window()
                go_back_button.pressed = False

        elif level3:
            lvl3.draw()
            groupLvl3.draw(screen)
            groupLvl3.update()
            level_buttons[2].pressed = False
            if word.errors >= 9:
                level3 = False
                lost = True

            if '_' not in word.space_out_word():
                level3 = False
                won = True

            if go_back_button.pressed:
                level3 = False
                start_game = True
                reset_window()
                go_back_button.pressed = False

        elif level4:
            lvl4.draw()
            groupLvl4.draw(screen)
            groupLvl4.update()
            level_buttons[3].pressed = False
            if word.errors >= 7:
                level4 = False
                lost = True

            if '_' not in word.space_out_word():
                level4 = False
                won = True

            if go_back_button.pressed:
                level4 = False
                start_game = True
                reset_window()
                go_back_button.pressed = False

        elif level5:
            lvl5.draw()
            groupLvl5.draw(screen)
            groupLvl5.update()
            level_buttons[4].pressed = False
            if word.errors >= 5:
                level5 = False
                lost = True

            if '_' not in word.space_out_word():
                level5 = False
                won = True

            if go_back_button.pressed:
                level5 = False
                start_game = True
                reset_window()
                go_back_button.pressed = False

        elif lost:
            lost1.draw()
            if play_again_button.pressed:
                lost = False
                start_game = True
                reset_window()
                play_again_button.pressed = False
            if exit_button.pressed:
                pygame.quit()
                exit()

        elif won:
            won1.draw()
            if play_again_button.pressed:
                won = False
                start_game = True
                reset_window()
                play_again_button.pressed = False
            if exit_button.pressed:
                pygame.quit()
                exit()

        elif rules:
            screen.fill("#D87F81")
            screen.blit(text_rules1, (250, 10))
            screen.blit(text_rules2, (50, 80))
            go_back_button.draw()
            if go_back_button.pressed:
                rules = False
                start_game = True
                reset_window()
                rules_button.pressed = False

        pygame.display.update()
        clock.tick(60)
