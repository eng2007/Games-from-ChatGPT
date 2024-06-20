import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна игры
screen_width = 800
screen_height = 600
play_area_width = 300
play_area_height = 600
play_area_x = (screen_width - play_area_width) // 2
play_area_y = (screen_height - play_area_height)
block_size = 30

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
cyan = (0, 255, 255)

# Список фигур Тетриса
tetrominoes = [
    ("I", [(0, -1), (0, 0), (0, 1), (0, 2)], cyan),
    ("J", [(0, -1), (0, 0), (0, 1), (-1, 1)], blue),
    ("L", [(0, -1), (0, 0), (0, 1), (1, 1)], orange),
    ("O", [(0, 0), (0, 1), (1, 0), (1, 1)], yellow),
    ("S", [(0, 0), (0, 1), (-1, 0), (1, 1)], green),
    ("T", [(0, -1), (0, 0), (0, 1), (1, 0)], purple),
    ("Z", [(0, 0), (0, 1), (1, 0), (-1, 1)], red)
]


# Класс для создания фигур Тетриса
class Tetromino:
    def __init__(self, x, y, tetromino):
        self.x = x
        self.y = y
        self.tetromino = tetromino
        self.color = tetromino[2]
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_blocks(self):
        return [(self.x + offset[0], self.y + offset[1]) for offset in self.tetromino[self.rotation]]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1


# Функция для создания новой фигуры
def new_tetromino():
    tetromino = random.choice(tetrominoes)
    return Tetromino(play_area_width // 2, 0, tetromino)


# Функция для проверки столкновения фигуры с игровым полем
def check_collision(tetromino, game_area):
    blocks = tetromino.get_blocks()
    for block in blocks:
        if block[0] < 0 or block[0] >= len(game_area[0]) or block[1] >= len(game_area) or game_area[block[1]][
            block[0]] != black:
            return True
        return False

#Функция для добавления фигуры на игровое поле

def add_to_game_area(tetromino, game_area):
    blocks = tetromino.get_blocks()
    for block in blocks:
        game_area[block[1]][block[0]] = tetromino.color

#Функция для удаления заполненных строк из игрового поля
def remove_full_rows(game_area):
    rows_removed = 0
    for i in range(len(game_area) - 1, -1, -1):
        if black not in game_area[i]:
            del game_area[i]
            rows_removed += 1
    for i in range(rows_removed):
        game_area.insert(0, [black] * len(game_area[0]))

#Настройки окна Pygame

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

#Игровой цикл

game_area = [[black for _ in range(play_area_width // block_size)] for _ in range(play_area_height // block_size)]
tetromino = new_tetromino()
game_over = False
clock = pygame.time.Clock()
score = 0
while not game_over:
# Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetromino.move_left()
            if check_collision(tetromino, game_area):
                tetromino.move_right()
            elif event.key == pygame.K_RIGHT:
                tetromino.move_right()
            if check_collision(tetromino, game_area):
                tetromino.move_left()
            elif event.key == pygame.K_DOWN:
                tetromino.move_down()
            if check_collision(tetromino, game_area):
                tetromino.move_up()
            elif event.key == pygame.K_UP:
                tetromino.rotate()
            if check_collision(tetromino, game_area):
                tetromino.rotate()

#Вывод результата игры

font = pygame.font.SysFont(None, 50)
if not game_over:
    text = font.render("You won!", True, white)
else:
    text = font.render("Game over!", True, white)
screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
pygame.display.update()
#Задержка перед выходом из игры
pygame.time.delay(2000)
#Выход из Pygame
pygame.quit()
#Вывод результата игры
print("Your score:", score)