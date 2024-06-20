# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:47:03 2024

@author: User
"""

import pygame
import sys

# Инициализация PyGame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Простой игровой интерфейс")

# Загрузка изображения кнопки
button_image = pygame.image.load("button.png")
button_rect = button_image.get_rect(center=(400, 400))

# Инициализация счета и улучшения
score = 0
click_multiplier = 1

# Создание объекта шрифта
font = pygame.font.Font(None, 36)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия на кнопку "Клик"
            if button_rect.collidepoint(event.pos):
                score += 1 * click_multiplier

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Отображение кнопки "Клик"
    screen.blit(button_image, button_rect)

    # Обновление экрана
    pygame.display.flip()


pygame.quit()