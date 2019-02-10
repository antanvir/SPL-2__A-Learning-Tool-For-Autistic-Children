# ===========Remaining Tasks======== #
# Correct Image Tile detect, if incorrect should be placed on top
# Space between Tiles should be black
# Usage incomplete for the image booleans


import sys
import random
import pygame
from pygame.locals import *


image = pygame.image.load("mango.jpg")



width, height = image.get_size()

IMAGE_SIZE = (width, height)
DISPLAY_SIZE = (2 * width + 50, 2 * height + 50)

COLUMNS = 2
ROWS = 2

TILE_WIDTH = int(width / COLUMNS) + 1
TILE_HEIGHT = int(height / ROWS) + 1


SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

silver_rect = pygame.Surface((TILE_WIDTH , TILE_HEIGHT))
silver_rect.fill(SILVER)
gray_rect = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
gray_rect.fill(GRAY)
black_rect = pygame.Surface((TILE_WIDTH , TILE_HEIGHT))
black_rect.fill(BLACK)

screen_middle = Rect((0, TILE_HEIGHT + 5), (2 * width + 50, height - (TILE_HEIGHT + 5)) )
screen_left = Rect((0, TILE_HEIGHT + 5), (TILE_WIDTH, 2 * height + 50 - (TILE_HEIGHT + 5)) )
screen_right = Rect((3 * TILE_WIDTH + 1, TILE_HEIGHT + 5), 
                ((2 * width + 50 - (3 * TILE_WIDTH + 1)), 2 * height + 50 - (TILE_HEIGHT + 5)) )
screen_down = Rect((0, 2 * height + 1), (2 * width + 50, 50 - 1))


pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE, 0, 32)
pygame.display.set_caption("Picture Drag and Drop")

image1 = pygame.image.load("IMG-0.jpg").convert_alpha()
image2 = pygame.image.load("IMG-1.jpg")
image3 = pygame.image.load("IMG-2.jpg")
image4 = pygame.image.load("IMG-3.jpg")

display.blit(image1, (0, 5))
display.blit(image2, (10*2 + TILE_WIDTH, 5))
display.blit(image3, (10*3 + 2*TILE_WIDTH, 5))
display.blit(image4, (10*4 + 3*TILE_WIDTH, 5))


display.blit(silver_rect, (TILE_WIDTH, height))
display.blit(gray_rect, (2 * TILE_WIDTH + 1, height))
display.blit(gray_rect, (TILE_WIDTH, height + TILE_HEIGHT + 1))
display.blit(silver_rect, (2 * TILE_WIDTH + 1, height + TILE_HEIGHT + 1))

pygame.display.flip()


left_button_pressed = False
mouse_dragged = False

image1_placed = False
image2_placed = False
image3_placed = False
image4_placed = False


while True:
    #pass
    #reload()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1:
            left_button_pressed = True
            display.blit(black_rect, (0, 5))

        elif left_button_pressed and event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseX -= TILE_WIDTH / 2
            mouseY -= TILE_HEIGHT / 2
            if mouseY > TILE_HEIGHT + 5:
                display.blit(image1, (mouseX, mouseY))
                display.blit(black_rect, (0, 5))


            mouse_dragged = True

        elif mouse_dragged and event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseX -= TILE_WIDTH / 2
            mouseY -= TILE_HEIGHT / 2
            display.blit(image1, (mouseX, mouseY))
            pygame.display.flip()

            left_button_pressed = False
            mouse_dragged = False

        pygame.display.flip()
        display.fill(BLACK, screen_middle)
        display.fill(BLACK, screen_left)
        display.fill(BLACK, screen_right)
        display.fill(BLACK, screen_down)

        display.blit(silver_rect, (TILE_WIDTH, height))
        display.blit(gray_rect, (2 * TILE_WIDTH + 1, height))
        display.blit(gray_rect, (TILE_WIDTH, height + TILE_HEIGHT + 1))
        display.blit(silver_rect, (2 * TILE_WIDTH + 1, height + TILE_HEIGHT + 1))