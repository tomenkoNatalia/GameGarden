import pygame
from sys import exit
import random
from flowers import Flowers
import colours as c

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Словесний сад")
pygame.display.set_icon(pygame.image.load('materials/flowerpos1.png'))
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

newFont = "materials/Adigiana_Extreme.ttf"
font1 = pygame.font.Font(newFont, 60)
font2 = pygame.font.Font(newFont, 30)
font3 = pygame.font.Font(newFont, 40)


class Button:
    def __init__(self, text_button, width_button, height_button, button_x, button_y, elevation, type_button=1):

        self.letter = text_button
        self.type = type_button
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = button_y
        self.original_x_pos = button_x
        self.top_rect = pygame.Rect(button_x, button_y, width_button, height_button)
        self.top_color = c.blue

        self.bottom_rect = pygame.Rect(button_x, button_y, width_button, height_button)
        self.bottom_color = c.darkBlue
        # textx
        self.text_surf = font2.render(text_button, True, c.white)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.clickSound = pygame.mixer.Sound("materials/Sounds/anyButton.wav")

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
                self.top_color = c.coral
                if pygame.mouse.get_pressed()[0]:
                    self.clickSound.play()
                    self.dynamic_elevation = 0
                    self.pressed = True
                else:
                    self.dynamic_elevation = self.dynamic_elevation

            else:
                self.dynamic_elevation = self.elevation
                self.top_color = c.blue

        if self.type == 2:
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = c.blue
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elevation = 0
                    self.top_color = c.coral
                    self.pressed = True
                    word.check_letter(self.letter)
                else:
                    self.dynamic_elevation = self.dynamic_elevation
                if self.pressed:
                    self.dynamic_elevation = self.dynamic_elevation

                else:
                    self.top_color = c.coral
            else:
                self.top_color = c.blue


class GameWindow:

    def __init__(self, back, text_color_gw, text_gw, field, xtext, ytext, xfield, yfield, type_gw=1):
        self.background = back
        self.text = font1.render(text_gw, True, text_color_gw)
        self.text_rect = pygame.Rect(xtext, ytext, 100, 100)
        self.field = pygame.image.load(field)
        self.field_rect = pygame.Rect(xfield, yfield, 10, 300)
        self.type = type_gw

    def draw(self):

        screen.fill(self.background)
        screen.blit(self.field, self.field_rect)
        screen.blit(self.text, self.text_rect)
        if self.type == 1:
            redraw_window()
            go_back_button.draw()
            word.draw_spaced()
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
        self.full_word_rect = pygame.Rect(300, 430, 100, 100)
        self.errors = 0
        self.wrongSound = pygame.mixer.Sound("materials/Sounds/wrongButton.wav")
        self.wrongSound.set_volume(0.3)
        self.correctSound = pygame.mixer.Sound("materials/Sounds/correctButton.wav")
        self.correctSound.set_volume(0.3)

    def draw_spaced(self):
        screen.blit(font1.render(self.space_out_word(), True, c.white), self.spaced_word_rect)

    def draw_full(self):
        screen.blit(font3.render('Слово раунду: ' + self.word, True, c.white), self.full_word_rect)

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
        for l in self.word:
            if l == letter:
                contains = True
        if contains:
            self.guessed += letter
            self.correctSound.play()
        else:
            flowers_group.sprites()[0].kill()
            self.errors += 1
            self.wrongSound.play()


flowers_group = pygame.sprite.Group()


def set_flowers(level):
    x_flowers = 40
    if level == 1:
        for i_flowers in range(5):
            flowers_group.add(Flowers(40 + x_flowers, 120), Flowers(40 + x_flowers, 220), Flowers(40 + x_flowers, 320))
            x_flowers += 140
    if level == 2:
        for i_flowers in range(4):
            flowers_group.add(Flowers(40 + x_flowers, 120), Flowers(40 + x_flowers, 220), Flowers(40 + x_flowers, 320))
            x_flowers += 180
    if level == 3:
        for i_flowers in range(5):
            flowers_group.add(Flowers(40 + x_flowers, 120), Flowers(40 + x_flowers, 300))
            x_flowers += 140
    if level == 4:
        for i_flowers in range(4):
            flowers_group.add(Flowers(40 + x_flowers, 120), Flowers(40 + x_flowers, 300))
            x_flowers += 180
    if level == 5:
        for i_flowers in range(3):
            flowers_group.add(Flowers(40 + x_flowers, 120), Flowers(40 + x_flowers, 300))
            x_flowers += 270


def redraw_window():
    for letter in letter_buttons:
        letter.draw()


# стартове вікно налаштування
test_start_surface = pygame.image.load("materials/startpic.jpg")
text_surface1 = font1.render("Вітаємо у словесному саду!", True, c.milk)
text_surface2 = font3.render("Оберіть рівень складності гри", True, c.bordeaux)

# level buttons
level_buttons = list()
x_lb = 50
for i in range(5):
    level_buttons.append(Button('Рівень ' + str(i + 1), 140, 60, x_lb, 300, 10, 1))
    x_lb += 190

rules_button = Button('Правила гри', 200, 80, 400, 400, 10, 1)
go_back_button = Button('Назад', 140, 50, 810, 400, 10, 1)
play_again_button = Button('Грати знову', 140, 50, 810, 400, 10, 1)
exit_button = Button('Вийти з гри', 140, 50, 50, 400, 10, 1)

# вікна на рівні
lvl1 = GameWindow(c.violet, c.milk, "Рівень 1", "materials/lvl1.1.jpg", 350, 1, 30, 70, 1)
lvl2 = GameWindow(c.sandColour, c.darkViolet, "Рівень 2", "materials/lvl2.1.jpg", 350, 1, 30, 70, 1)
lvl3 = GameWindow(c.lightGreen, c.milkPink, "Рівень 3", "materials/lvl3.1.jpg", 350, 1, 30, 70, 1)
lvl4 = GameWindow(c.lightViolet, c.lightOrange, "Рівень 4", "materials/lvl4.1.jpg", 350, 1, 30, 70, 1)
lvl5 = GameWindow(c.strikingPink, c.sandColour, "Рівень 5", "materials/lvl5.1.jpg", 350, 1, 30, 70, 1)
lost1 = GameWindow(c.sandColour, c.darkViolet, "О ні, ви вбили квіточки((", "materials/lost1.jpg", 250, 1, 0, 0, 2)
won1 = GameWindow(c.sandColour, c.darkViolet, "Вітаю, ви вберегли сад!", "materials/win1.jpg", 250, 1, 0, 0, 2)


def blit_text(surface, text, pos, font):
    global word_height
    x, y = pos
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    for line in text:
        for word_idk in line:
            word_surface = font.render(word_idk, True, c.bordeaux).convert_alpha()
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


text = open("materials/rules.txt", encoding="UTF8").readlines()
text_rules1 = font1.render("Правила гри", True, c.milk)

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
    screen.blit(text_surface1, (190, 50))
    screen.blit(text_surface2, (250, 200))
    for level_button in level_buttons:
        level_button.draw()
    rules_button.draw()
    # exit_button.draw()
    for letter in letter_buttons:
        letter.pressed = False
        letter.dynamic_elevation = 10
    flowers_group.empty()


backMusic = pygame.mixer.Sound("materials/Sounds/backmusic.wav")
backMusic.play(loops=-1)
backMusic.set_volume(0.3)
loseMusic = pygame.mixer.Sound("materials/Sounds/lose.wav")
winMusic = pygame.mixer.Sound("materials/Sounds/win.wav")

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
                set_flowers(1)
                word = Word(1)
            elif level_buttons[1].pressed:
                start_game = False
                level2 = True
                set_flowers(2)
                word = Word(2)
            elif level_buttons[2].pressed:
                start_game = False
                level3 = True
                set_flowers(3)
                word = Word(3)
            elif level_buttons[3].pressed:
                start_game = False
                level4 = True
                set_flowers(4)
                word = Word(4)
            elif level_buttons[4].pressed:
                start_game = False
                level5 = True
                set_flowers(5)
                word = Word(5)
            elif rules_button.pressed:
                start_game = False
                rules = True

        elif level1:
            lvl1.draw()
            flowers_group.draw(screen)
            flowers_group.update()

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
            flowers_group.draw(screen)
            flowers_group.update()

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
            flowers_group.draw(screen)
            flowers_group.update()

            level_buttons[2].pressed = False
            if word.errors >= 10:
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
            flowers_group.draw(screen)
            flowers_group.update()

            level_buttons[3].pressed = False
            if word.errors >= 8:
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
            flowers_group.draw(screen)
            flowers_group.update()

            level_buttons[4].pressed = False
            if word.errors >= 6:
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
            screen.fill(c.lightPink)
            screen.blit(text_rules1, (300, 10))
            blit_text(screen, text, (40, 90), font2)
            go_back_button.draw()
            if go_back_button.pressed:
                rules = False
                start_game = True
                reset_window()
                rules_button.pressed = False

        pygame.display.update()
        clock.tick(60)
