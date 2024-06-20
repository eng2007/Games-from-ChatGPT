import pygame
import sys
import random

# Инициализация PyGame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Избегай препятствий")

# Загрузка изображения персонажа и препятствия
player_image = pygame.image.load("player.png")
obstacle_image = pygame.image.load("obstacle.png")

# Инициализация игровых объектов
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.velocity = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 600:  # Прыжок при нажатии пробела
            self.velocity = -7

        self.velocity += 0.1  # Гравитация
        self.rect.y += self.velocity

        # Проверка, чтобы не уходить за экран
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.velocity = 0

        if keys[pygame.K_LEFT] and self.rect.left > 0:  # Движение влево
            self.rect.x -= 2
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # Движение вправо
            self.rect.x += 2

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(800, 1600), random.randint(500, 550))

    def update(self):
        self.rect.x -= 1  # Скорость движения препятствий влево
        if self.rect.right < 0:
            self.rect.center = (random.randint(800, 1600), random.randint(500, 550))

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Создание персонажа
player = Player()
all_sprites.add(player)

# Создание препятствий
for _ in range(1):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление персонажа и препятствий
    all_sprites.update()

    # Обнаружение коллизий между персонажем и препятствиями
    collisions = pygame.sprite.spritecollide(player, obstacles, False)
    if collisions:
        pygame.quit()
        sys.exit()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отображение персонажа и препятствий
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()
