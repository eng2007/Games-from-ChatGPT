# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:42:58 2022

@author: User
"""

import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH = 400
HEIGHT = 400

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Arkanoid")

# Create the ball
ball = pygame.Rect(200, 200, 10, 10)

# Create the paddle
paddle = pygame.Rect(150, 390, 100, 10)

# Create the bricks
bricks = []
for i in range(10):
    for j in range(5):
        bricks.append(pygame.Rect(i*50+30, j*10+30, 50, 10))

# Set the ball movement
ball_movement = [3, -3]

# Set the paddle movement
paddle_movement = 0

# Set the game variables
lives = 3
score = 0

# Main game loop
while len(bricks) > 0 and lives > 0:
    time.sleep(0.01)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_movement = -3
            elif event.key == pygame.K_RIGHT:
                paddle_movement = 3
        elif event.type == pygame.KEYUP:
            paddle_movement = 0

    # Update the ball position
    ball.x += ball_movement[0]
    ball.y += ball_movement[1]

    # Check for collision with walls
    if ball.left < 0 or ball.right > WIDTH:
        ball_movement[0] = -ball_movement[0]
    if ball.top < 0:
        ball_movement[1] = -ball_movement[1]

    # Check for collision with paddle
    if ball.colliderect(paddle):
        ball_movement[1] = -ball_movement[1]

    # Check for collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_movement[1] = -ball_movement[1]
            bricks.remove(brick)
            score += 1

    # Update the paddle position
    paddle.x += paddle_movement

    # Check for ball falling off the screen
    if ball.top > HEIGHT:
        lives -= 1
        ball.x = 200
        ball.y = 200
        ball_movement = [3, -3]
        paddle.x = 150

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.rect(screen, (255, 0, 0), ball)

    # Draw the paddle
    pygame.draw.rect(screen, (0, 0, 255), paddle)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, (0, 255, 0), brick)

    # Update the display
    pygame.display.flip()

# Game over message
if len(bricks) == 0:
    print("Congratulations! You won the game with a score of", score)
else:
    print("Game Over. You lost all your lives.")
    
pygame.quit()
sys.exit()