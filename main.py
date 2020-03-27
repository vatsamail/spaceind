import pygame
import time
import os
import sys

"""
Initializations
"""
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# initialize game window variable
running = True

#title
pygame.display.set_caption("backspace")
icon = pygame.image.load(os.path.join(os.getcwd(), 'static', 'astronaut.png'))
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load(os.path.join(os.getcwd(), 'static', 'our_spaceship.png'))
player_x = 370
player_y = 480

# alien


# methods
def player():
    screen.blit(player_image, (player_x, player_y))

"""
Game Loop
"""
while running:
    screen.fill((10,20,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()
