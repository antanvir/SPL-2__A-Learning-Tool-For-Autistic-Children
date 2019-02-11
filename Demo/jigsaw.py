# ===========Remaining Tasks======== #
# TILE 1 shows after placement if left button clicked
# Space between Tiles should be black
# blinks image


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

image1 = pygame.image.load("IMG-0.jpg")
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

image1_dragged = False
image1_placed = False
image2_dragged = False
image2_placed = False
image3_dragged = False
image3_placed = False
image4_dragged = False
image4_placed = False

clock = pygame.time.Clock()

while True:
	clock.tick(70)

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

		elif event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1: 
			left_button_pressed = True

			mouseX, mouseY = pygame.mouse.get_pos()

			if (0 <= mouseX <= TILE_WIDTH) and (5 <= mouseY <= TILE_HEIGHT + 5):
				image1_dragged = True
				display.blit(black_rect, (0, 5))
					
			elif (10*2 + TILE_WIDTH <= mouseX <= 10*2 + 2*TILE_WIDTH) and (5 <= mouseY <= TILE_HEIGHT + 5):
					image2_dragged = True
					display.blit(black_rect, (10*2 + TILE_WIDTH, 5))

			elif (10*3 + 2*TILE_WIDTH <= mouseX <= 10*2 + 3*TILE_WIDTH) and (5 <= mouseY <= TILE_HEIGHT + 5):
					image3_dragged = True
					display.blit(black_rect, (10*3 + 2*TILE_WIDTH, 5))

			elif (10*4 + 3*TILE_WIDTH <= mouseX <= 10*2 + 4*TILE_WIDTH) and (5 <= mouseY <= TILE_HEIGHT + 5):
					image4_dragged = True
					display.blit(black_rect, (10*4 + 3*TILE_WIDTH, 5))




		elif left_button_pressed and event.type == pygame.MOUSEMOTION:
			mouse_dragged = True

			mouseX, mouseY = pygame.mouse.get_pos()
			mouseX -= TILE_WIDTH / 2
			mouseY -= TILE_HEIGHT / 2
			#display.blit(image1, (mouseX, mouseY))

			if mouseY  > TILE_HEIGHT + 5:
				if image1_dragged:
					display.blit(image1, (mouseX, mouseY))
					#display.blit(black_rect, (0, 5))
				elif image2_dragged:
					display.blit(image2, (mouseX, mouseY))
					#display.blit(black_rect, (10*2 + TILE_WIDTH, 5))
				elif image3_dragged:
					display.blit(image3, (mouseX, mouseY))
					#display.blit(black_rect, (10*3 + 2*TILE_WIDTH, 5))
				elif image4_dragged:
					display.blit(image4, (mouseX, mouseY))
					#display.blit(black_rect, (10*4 + 3*TILE_WIDTH, 5))



			

		elif mouse_dragged and event.type == pygame.MOUSEBUTTONUP:
			print("here")
			mouseX, mouseY = pygame.mouse.get_pos()
			#mouseX -= TILE_WIDTH / 2
			#mouseY -= TILE_HEIGHT / 2

			if mouseX < TILE_WIDTH and mouseY < height:
				mouse_dragged = False
				if image1_dragged:
					display.blit(image1, (0, 5))
					image1_dragged = False
				elif image2_dragged:
					display.blit(image2, (10*2 + TILE_WIDTH, 5))
					image2_dragged = False
				elif image3_dragged:
					display.blit(image3, (10*3 + 2*TILE_WIDTH, 5))
					image3_dragged = False
				elif image4_dragged:
					display.blit(image4, (10*4 + 3*TILE_WIDTH, 5))
					image4_dragged = False

			else:
				left_button_pressed = False
				mouse_dragged = False

				if (TILE_WIDTH <= mouseX <= 2*TILE_WIDTH) and (height <= mouseY <= height + TILE_HEIGHT):
					if image1_dragged:
						display.blit(image1, (TILE_WIDTH, height))
						image1_placed = True
					else:
						image1_dragged = False
				elif (2*TILE_WIDTH + 1 <= mouseX <= 3*TILE_WIDTH) and (height <= mouseY <= height + TILE_HEIGHT):
					if image2_dragged:
						display.blit(image2, (2 * TILE_WIDTH + 1, height))
						image2_placed = True
					else:
						image2_dragged = False
				elif (TILE_WIDTH <= mouseX <= 2*TILE_WIDTH) and (height + TILE_HEIGHT + 1 <= mouseY <= height + 2*TILE_HEIGHT):
					if image3_dragged:
						display.blit(image3, (TILE_WIDTH, height + TILE_HEIGHT + 1))
						image3_placed = True
					else:
						image3_dragged = False
				elif (2*TILE_WIDTH + 1 <= mouseX <= 3*TILE_WIDTH) and (height + TILE_HEIGHT + 1 <= mouseY <= height + 2*TILE_HEIGHT):
					if image4_dragged:
						display.blit(image4, (2 * TILE_WIDTH + 1, height + TILE_HEIGHT + 1))
						image4_placed = True
					else:
						image4_dragged = False

				if image1_placed == False:
					display.blit(image1, (0, 5))
				if image2_placed == False:
					display.blit(image2, (10*2 + TILE_WIDTH, 5))
				if image3_placed == False:
					display.blit(image3, (10*3 + 2*TILE_WIDTH, 5))
				if image4_placed == False:
					display.blit(image4, (10*4 + 3*TILE_WIDTH, 5))





		pygame.display.flip()
		display.fill(BLACK, screen_middle)
		display.fill(BLACK, screen_left)
		display.fill(BLACK, screen_right)
		display.fill(BLACK, screen_down)
		if image1_placed:
			display.blit(image1, (TILE_WIDTH, height))
		else:
			display.blit(silver_rect, (TILE_WIDTH, height))

		if image2_placed:
			display.blit(image2, (2 * TILE_WIDTH + 1, height))
		else:
			display.blit(gray_rect, (2 * TILE_WIDTH + 1, height))

		if image3_placed:
			display.blit(image3, (TILE_WIDTH, height + TILE_HEIGHT + 1)) 
		else:  
			display.blit(gray_rect, (TILE_WIDTH, height + TILE_HEIGHT + 1))

		if image4_placed:
			display.blit(image4, (2 * TILE_WIDTH + 1, height + TILE_HEIGHT + 1))
		else:
			display.blit(silver_rect, (2 * TILE_WIDTH + 1, height + TILE_HEIGHT + 1))
		#pygame.display.flip()
