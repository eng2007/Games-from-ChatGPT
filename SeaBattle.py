# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:15:17 2022

@author: User
"""

import pygame
import sys
import random

def computer_turn(board):
    """
    Select a random location on the board to fire at.
    """
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    while board[x][y] != 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    return x, y

# Initialize PyGame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 600))

# Set the title of the window
pygame.display.set_caption('SeaBattle')

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game board
board = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    board.append(row)
    
board2 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    board2.append(row)

# Set up the player's ships
player_ships = [[(2,3), (2,4), (2,5)], [(8,2), (8,3), (8,4)]]

# Set up the computer's ships
computer_ships = [[(5,6), (5,7), (5,8)], [(1,9), (2,9), (3,9)]]

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse clicks
            x, y = pygame.mouse.get_pos()
            row = y // 60
            col = x // 60
            if board[row][col] == 0:
                # Player has not yet fired at this location
                board[row][col] = 1
                hit = False
                for ship in computer_ships:
                    if (row, col) in ship:
                        # Player has hit a computer ship
                        hit = True
                        ship.remove((row, col))
                        if len(ship) == 0:
                            # Player has sunk the ship
                            message = font.render('You sank my battleship!', True, WHITE, BLUE)
                            screen.blit(message, (60, 540))
                        else:
                            # Player has hit a ship, but not sunk it
                            message = font.render('Hit!', True, WHITE, BLUE)
                            screen.blit(message, (60, 540))
                if not hit:
                    # Player has missed
                    message = font.render('Miss!', True, WHITE, BLUE)
                    screen.blit(message, (60, 540))
                    
            # Have the computer take its turn
            x, y = computer_turn(board2)
            if board2[x][y] == 0:
                # Computer has not yet fired at this location
                board2[x][y] = 1
                hit = False
                for ship in player_ships:
                    if (x, y) in ship:
                        # Computer has hit a player ship
                        hit = True
                        ship.remove((x, y))
                        if len(ship) == 0:
                            # Computer has sunk the ship
                            message = font.render('I sank your battleship!', True, WHITE, BLUE)
                            screen.blit(message, (360, 540))
                        else:
                            # Computer has hit a ship, but not sunk it
                            message = font.render('Hit!', True, WHITE, BLUE)
                            screen.blit(message, (360, 540))
                if not hit:
                    # Computer has missed
                    message = font.render('Miss!', True, WHITE, BLUE)
                    screen.blit(message, (360, 540))

    # Check if the game is over
    game_over = True
    for ship in player_ships:
        if len(ship) > 0:
            game_over = False
            break
    if game_over:
        message = font.render('Game Over! You lost.', True, WHITE, RED)
        screen.blit(message, (180, 540))
    game_over = True
    for ship in computer_ships:
        if len(ship) > 0:
            game_over = False
            break
    if game_over:
        message = font.render('Game Over! You won.', True, WHITE, RED)
        screen.blit(message, (180, 540))

    # Draw the board
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j*60, i*60, 60, 60))
            else:
                pygame.draw.rect(screen, WHITE, (j*60, i*60, 60, 60))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Shut down PyGame
pygame.quit()
sys.exit()

