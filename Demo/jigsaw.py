# ===========Remaining Tasks======== #
#
import sys
import random
import pygame
from pygame.locals import *

class JigsawPuzzle():

	def pointerIsInSurface(mouseX, mouseY, TILE):
		if (TILE[0] <= mouseX <= TILE[2]) and (TILE[1] <= mouseY <= TILE[3]):
			return True
		return False

	image = pygame.image.load("mango.jpg")
	width, height = image.get_size()

	IMAGE_SIZE = (width, height)
	DISPLAY_SIZE = (4*width, 3*height + height//2)

	ver_gap = (height/2)/4
	hor_gap = (width/2)/4

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

	'''screen_middle = Rect((0, TILE_HEIGHT + 5), (2 * width + 50, height - (TILE_HEIGHT + 5)) )
	screen_left = Rect((0, TILE_HEIGHT + 5), (TILE_WIDTH, 2 * height + 50 - (TILE_HEIGHT + 5)) )
	screen_right = Rect((3 * TILE_WIDTH + 1, TILE_HEIGHT + 5), 
					((2 * width + 50 - (3 * TILE_WIDTH + 1)), 2 * height + 50 - (TILE_HEIGHT + 5)) )
	screen_down = Rect((0, 2 * height + 1), (2 * width + 50, 50 - 1))'''

	# black portion of the screen
	screen_middle = Rect((0, height + ver_gap), (4*width, height) )
	screen_left = Rect((0, height + ver_gap), (width + width/2, 2*height + ver_gap)) 
	screen_right = Rect((2*width + (width/2 + 1), height + ver_gap), 
										(width + width/2, 2*height + ver_gap) )
	screen_down = Rect((0, 3*height + (ver_gap + 1)), (4*width, height))


	hor_line = pygame.Surface((width, 1))
	hor_line.fill(BLACK)
	ver_line = pygame.Surface((1, height))
	ver_line.fill(BLACK)

	pygame.init()
	display = pygame.display.set_mode(DISPLAY_SIZE, 0, 32)
	pygame.display.set_caption("JIGSAW PUZZLE : MAKING OBJECT FROM PIECES!")

	image1 = pygame.image.load("IMG-0.jpg")
	image2 = pygame.image.load("IMG-1.jpg")
	image3 = pygame.image.load("IMG-2.jpg")
	image4 = pygame.image.load("IMG-3.jpg")

	display.blit(image, (2*width + 6*hor_gap, ver_gap))
	ver_line.fill(SILVER)
	display.blit(ver_line, (2*width + 5*hor_gap, ver_gap))
	ver_line.fill(BLACK)

	# positions of 4 piece images 
	display.blit(image1, (hor_gap, ver_gap))
	display.blit(image2, (2*hor_gap + TILE_WIDTH, ver_gap))
	display.blit(image3, (3*hor_gap + 2*TILE_WIDTH, ver_gap))
	display.blit(image4, (4*hor_gap + 3*TILE_WIDTH, ver_gap))

	# position of blank tiles to hold 4 pieces of images
	display.blit(silver_rect, (width + width/2, 2*height + ver_gap))
	display.blit(gray_rect, (width + TILE_WIDTH + (width/2+1), 2*height + ver_gap))
	display.blit(gray_rect, (width + width/2, 2*height + ver_gap + TILE_HEIGHT+1))
	display.blit(silver_rect, (width + TILE_WIDTH + (width/2+1), 2*height + ver_gap + TILE_HEIGHT+1))


	# TILE -> (left, top, right, bottom)
	IMAGE1_TILE = (hor_gap, ver_gap, hor_gap + TILE_WIDTH, ver_gap+TILE_HEIGHT)
	IMAGE2_TILE = (2*hor_gap + TILE_WIDTH, ver_gap, 2*hor_gap + 2*TILE_WIDTH, ver_gap+TILE_HEIGHT)
	IMAGE3_TILE = (3*hor_gap + 2*TILE_WIDTH, ver_gap, 3*hor_gap + 3*TILE_WIDTH, ver_gap+TILE_HEIGHT)
	IMAGE4_TILE = (4*hor_gap + 3*TILE_WIDTH, ver_gap, 4*hor_gap + 4*TILE_WIDTH, ver_gap+TILE_HEIGHT)

	BLANK_TILE1 = (width + width/2, 2*height + ver_gap, 
					width + width/2 + TILE_WIDTH, 2*height + ver_gap + TILE_HEIGHT)
	BLANK_TILE2 = (width + TILE_WIDTH + (width/2+1), 2*height + ver_gap, 
					2*width + (width/2+1), 2*height + ver_gap + TILE_HEIGHT)
	BLANK_TILE3 = (width + width/2, 2*height + ver_gap + TILE_HEIGHT+1, 
					width + width/2 + TILE_WIDTH, 2*height + ver_gap + 2*TILE_HEIGHT)
	BLANK_TILE4 = (width + TILE_WIDTH + (width/2+1), 2*height + ver_gap + TILE_HEIGHT+1, 
					2*width + (width/2+1), 2*height + ver_gap + 2*TILE_HEIGHT)

	pygame.display.flip()


	left_button_pressed = False
	mouse_dragged = False

	image1_dragged, image2_dragged, image3_dragged, image4_dragged = False, False, False, False
	image1_placed, image2_placed, image3_placed, image4_placed = False, False, False, False

	clock = pygame.time.Clock()

	while True:

		clock.tick(70)
		for event in pygame.event.get():

			if event.type == QUIT:
				exit()

			elif event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1: 
				left_button_pressed = True

				mouseX, mouseY = pygame.mouse.get_pos()

				if pointerIsInSurface(mouseX, mouseY, IMAGE1_TILE) and image1_placed == False:
					image1_dragged = True
					display.blit(black_rect, (IMAGE1_TILE[0], IMAGE1_TILE[1]))
						
				elif pointerIsInSurface(mouseX, mouseY, IMAGE2_TILE) and image2_placed == False:
						image2_dragged = True
						display.blit(black_rect, (IMAGE2_TILE[0], IMAGE2_TILE[1]))

				elif pointerIsInSurface(mouseX, mouseY, IMAGE3_TILE) and image3_placed == False:
						image3_dragged = True
						display.blit(black_rect, (IMAGE3_TILE[0], IMAGE3_TILE[1]))

				elif pointerIsInSurface(mouseX, mouseY, IMAGE4_TILE) and image4_placed == False:
						image4_dragged = True
						display.blit(black_rect, (IMAGE4_TILE[0], IMAGE4_TILE[1]))

			

			elif mouse_dragged and event.type == pygame.MOUSEBUTTONUP:
				left_button_pressed = False
				mouse_dragged = False

				mouseX, mouseY = pygame.mouse.get_pos()

				if mouseX < width+width/2 and mouseY < 2*height+ver_gap:
					if image1_dragged:
						display.blit(image1, (IMAGE1_TILE[0], IMAGE1_TILE[1]))
						image1_dragged = False

					elif image2_dragged:
						display.blit(image2, (IMAGE2_TILE[0], IMAGE2_TILE[1]))
						image2_dragged = False

					elif image3_dragged:
						display.blit(image3, (IMAGE3_TILE[0], IMAGE3_TILE[1]))
						image3_dragged = False

					elif image4_dragged:
						display.blit(image4, (IMAGE4_TILE[0], IMAGE4_TILE[1]))
						image4_dragged = False

				else:
					if pointerIsInSurface(mouseX, mouseY, BLANK_TILE1):
						if image1_dragged:
							display.blit(image1, (BLANK_TILE1[0], BLANK_TILE1[1]))
							image1_placed = True

					elif pointerIsInSurface(mouseX, mouseY, BLANK_TILE2):
						if image2_dragged:
							display.blit(image2, (BLANK_TILE2[0], BLANK_TILE2[1]))
							image2_placed = True

					elif pointerIsInSurface(mouseX, mouseY, BLANK_TILE3):
						if image3_dragged:
							display.blit(image3, (BLANK_TILE3[0], BLANK_TILE3[1]))
							image3_placed = True

					elif pointerIsInSurface(mouseX, mouseY, BLANK_TILE4):
						if image4_dragged:
							display.blit(image4, (BLANK_TILE4[0], BLANK_TILE4[1]))
							image4_placed = True

					if image1_placed == False:
						display.blit(image1, (IMAGE1_TILE[0], IMAGE1_TILE[1]))

					if image2_placed == False:
						display.blit(image2, (IMAGE2_TILE[0], IMAGE2_TILE[1]))

					if image3_placed == False:
						display.blit(image3, (IMAGE3_TILE[0], IMAGE3_TILE[1]))

					if image4_placed == False:
						display.blit(image4, (IMAGE4_TILE[0], IMAGE4_TILE[1]))

					image1_dragged = False
					image2_dragged = False
					image3_dragged = False
					image4_dragged = False




			elif left_button_pressed and event.type == pygame.MOUSEMOTION:
				mouse_dragged = True

				mouseX, mouseY = pygame.mouse.get_pos()
				mouseX -= TILE_WIDTH / 2
				mouseY -= TILE_HEIGHT / 2

				if mouseY  > height + ver_gap:
					if image1_dragged:
						display.blit(image1, (mouseX, mouseY))

					elif image2_dragged:
						display.blit(image2, (mouseX, mouseY))

					elif image3_dragged:
						display.blit(image3, (mouseX, mouseY))

					elif image4_dragged:
						display.blit(image4, (mouseX, mouseY))



			pygame.display.flip()
			display.fill(BLACK, screen_middle)
			display.fill(BLACK, screen_left)
			display.fill(BLACK, screen_right)
			display.fill(BLACK, screen_down)

			display.blit(hor_line, (width + width/2, 2*height + ver_gap + TILE_HEIGHT))
			display.blit(ver_line, (width + width/2 + TILE_WIDTH, 2*height + ver_gap))

			if image1_placed:
				display.blit(image1, (BLANK_TILE1[0], BLANK_TILE1[1]))
			else:
				display.blit(silver_rect, (BLANK_TILE1[0], BLANK_TILE1[1]))

			if image2_placed:
				display.blit(image2, (BLANK_TILE2[0], BLANK_TILE2[1]))
			else:
				display.blit(gray_rect, (BLANK_TILE2[0], BLANK_TILE2[1]))

			if image3_placed:
				display.blit(image3, (BLANK_TILE3[0], BLANK_TILE3[1])) 
			else:  
				display.blit(gray_rect, (BLANK_TILE3[0], BLANK_TILE3[1]))

			if image4_placed:
				display.blit(image4, (BLANK_TILE4[0], BLANK_TILE4[1]))
			else:
				display.blit(silver_rect, (BLANK_TILE4[0], BLANK_TILE4[1]))


if __name__ == "__main__":
	jigsaw = JigsawPuzzle()
