import sys
import random
import pygame
from pygame.locals import *

#IMAGE_FILE = "mango.jpg"
image = pygame.image.load("mango.jpg")

image1 = pygame.image.load("IMG-0.jpg")
image2 = pygame.image.load("IMG-1.jpg")
image3 = pygame.image.load("IMG-2.jpg")
image4 = pygame.image.load("IMG-3.jpg")

width, height = image.get_size()

IMAGE_SIZE = (width, height)
DISPLAY_SIZE = (2*width+50, 2*height+50)

COLUMNS = 2
ROWS = 2

TILE_WIDTH = int(width / COLUMNS) + 1
TILE_HEIGHT = int(height / ROWS) + 1


#my_font = pygame.font.SysFont("arial", 16)
#text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))
MAGENTA = (255, 0, 255)

hor_border = pygame.Surface((TILE_WIDTH + 1, 1))
hor_border.fill(MAGENTA)
ver_border = pygame.Surface((1, TILE_HEIGHT + 1))
ver_border.fill(MAGENTA)




pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE, 0, 32)
pygame.display.set_caption("Picture Drag and Drop")
#display.blit(image, (0, 0))

display.blit(image1, (10, 5))
display.blit(image2, (10*2 + TILE_WIDTH, 5))
display.blit(image3, (10*3 + 2*TILE_WIDTH, 5))
display.blit(image4, (10*4 + 3*TILE_WIDTH, 5))

for c in range(COLUMNS):
    for r in range(ROWS):
        display.blit(hor_border, ( (r+1) * TILE_WIDTH, height))
        display.blit(hor_border, ( (r+1) *TILE_WIDTH, height + TILE_HEIGHT -1 ))
        display.blit(ver_border, ( (r+1) *TILE_WIDTH, height))
        display.blit(ver_border, ( (r+1) * 2 * TILE_WIDTH -1, height))

while True:
    #pass
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    '''display.blit(image1, (10, 5))
    display.blit(image2, (10*2 + TILE_WIDTH, 5))
    display.blit(image3, (10*3 + 2*TILE_WIDTH, 5))
    display.blit(image4, (10*4 + 3*TILE_WIDTH, 5))'''

    display.blit(hor_border, (TILE_WIDTH, height))
    display.blit(hor_border, (TILE_WIDTH, height + TILE_HEIGHT -1 ))
    display.blit(ver_border, (TILE_WIDTH, height))
    display.blit(ver_border, (2 * TILE_WIDTH -1, height))
    '''for c in range(COLUMNS):
        for r in range(ROWS):
            tile = image.subsurface(
                c * TILE_WIDTH, 0,
                TILE_WIDTH, TILE_HEIGHT)'''


    pygame.display.flip()