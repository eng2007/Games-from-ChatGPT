# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:45:13 2022

@author: User
"""

import pygame
import random

# Window size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame
pygame.init()

# Set the window size
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window title
pygame.display.set_caption("Snake")

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Initialize the snake position and direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Initialize the food position
food_pos = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE, 
            random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
food_spawn = True

# Initialize the direction
direction = "RIGHT"
change_to = direction

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('Your score was: ' + str(len(snake_body) - 3), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Validate the direction change
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= SNAKE_SPEED
    if direction == "DOWN":
        snake_pos[1] += SNAKE_SPEED
    if direction == "LEFT":
        snake_pos[0] -= SNAKE_SPEED
    if direction == "RIGHT":
        snake_pos[0] += SNAKE_SPEED

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_pos = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE, 
                    random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
    food_spawn = True
    
    # Background
    screen.fill(BLACK)
    
    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
        
    # Draw the food
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))
    
    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH - SNAKE_SIZE:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT - SNAKE_SIZE:
        game_over()
        
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # Refresh the screen
    pygame.display.update()
    
    # Frame rate
    clock.tick(10)
