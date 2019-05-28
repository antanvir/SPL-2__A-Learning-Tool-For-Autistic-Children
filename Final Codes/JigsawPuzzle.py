import time
import datetime
import sys
import random
import math
import pygame
import mysql.connector
from pygame.locals import *
from time import sleep
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMessageBox,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)


class JigsawPuzzle():

	
	def initGame(self,ObjectID):
		mainImagePath, part1_path, part2_path, part3_path, part4_path = None, None, None, None, None
		
		mydb = mysql.connector.connect(
			host = 'localhost',
			user = "root",
			#passwd = "ant904",
			database="spl"
		)
		myCursor = mydb.cursor(buffered=True)
		sql = "SELECT main_image, image_name_1, image_name_2, image_name_3, image_name_4 \
				FROM game where game_id = %s"
		val = (ObjectID,)
		myCursor.execute(sql, val)
		myresult = myCursor.fetchone()

		mainImagePath = myresult[0]
		part1_path = myresult[1] 
		part2_path = myresult[2]
		part3_path = myresult[3]
		part4_path = myresult[4]

		myCursor.close()
		
		
		pygame.init()
		start_time = datetime.datetime.now().replace(microsecond = 0)

		deviceDisplay = pygame.display.Info()
		#display = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE)
		#display = pygame.display.set_mode((0,0), pygame.RESIZABLE)
		display = pygame.display.set_mode((deviceDisplay.current_w, deviceDisplay.current_h), pygame.RESIZABLE)
		pygame.display.set_caption("JIGSAW PUZZLE : MAKING OBJECT FROM PIECES!")


		image = pygame.image.load(mainImagePath)				# mainImagePath
		width, height = image.get_size()
		print(width, height)

		IMAGE_SIZE = (width, height)
		DISPLAY_SIZE = (4*width, 3*height + height//2)

		#ver_gap = (height/2)/4
		ver_gap = (deviceDisplay.current_h/4)/4
		hor_gap = (width/2)/4
		#hor_gap = (deviceDisplay.current_w/2)/4

		COLUMNS = 2
		ROWS = 2

		TILE_WIDTH = int(width / COLUMNS) + 1
		TILE_HEIGHT = int(height / ROWS) + 1

		SILVER = (192, 192, 192)
		GRAY = (128, 128, 128)
		BLACK = (0, 0, 0)
		CUSTOM_DISPLAY = (54, 75, 109)		#rgb(54, 75, 109)
		FONT_COLOR = (0, 255, 0)

		silver_rect = pygame.Surface((TILE_WIDTH , TILE_HEIGHT))
		silver_rect.fill(SILVER)

		gray_rect = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
		gray_rect.fill(GRAY)

		black_rect = pygame.Surface((TILE_WIDTH , TILE_HEIGHT))
		black_rect.fill(BLACK)

		hor_line = pygame.Surface((width, 1))
		hor_line.fill(BLACK)
		ver_line = pygame.Surface((1, height))
		ver_line.fill(BLACK)

		ver_divider = pygame.Surface((1, deviceDisplay.current_h - 4*ver_gap))
		ver_divider.fill(SILVER)
		

		image1 = pygame.image.load(part1_path)			# part1_path
		image2 = pygame.image.load(part2_path)			# part2_path
		image3 = pygame.image.load(part3_path)			# part3_path
		image4 = pygame.image.load(part4_path)			# part4_path

		# display main picture & main-picture-divider from pieces
		display.fill(CUSTOM_DISPLAY)
		display.blit(image, (5.8*deviceDisplay.current_w/8, ver_gap))   
		display.blit(ver_divider, (5.2*deviceDisplay.current_w/8, ver_gap)) 

		# positions of 4 piece images 
		display.blit(image1, (3*hor_gap, ver_gap))
		display.blit(image2, (4*hor_gap + TILE_WIDTH, ver_gap))
		display.blit(image3, (5*hor_gap + 2*TILE_WIDTH, ver_gap))
		display.blit(image4, (6*hor_gap + 3*TILE_WIDTH, ver_gap))

		# position of blank tiles to hold 4 pieces of images
		display.blit(silver_rect, (4*hor_gap + TILE_WIDTH, 2*height + ver_gap))
		display.blit(gray_rect, (4*hor_gap + 2*TILE_WIDTH + 1, 2*height + ver_gap))
		display.blit(gray_rect, (4*hor_gap + TILE_WIDTH, 2*height + ver_gap + TILE_HEIGHT+1))
		display.blit(silver_rect, (4*hor_gap + 2*TILE_WIDTH + 1, 2*height + ver_gap + TILE_HEIGHT+1))

		# TILE -> (left, top, right, bottom)
		IMAGE1_TILE = (3*hor_gap, ver_gap, 3*hor_gap + TILE_WIDTH, ver_gap+TILE_HEIGHT)
		IMAGE2_TILE = (4*hor_gap + TILE_WIDTH, ver_gap, 4*hor_gap + 2*TILE_WIDTH, ver_gap+TILE_HEIGHT)
		IMAGE3_TILE = (5*hor_gap + 2*TILE_WIDTH, ver_gap, 5*hor_gap + 3*TILE_WIDTH, ver_gap+TILE_HEIGHT)
		IMAGE4_TILE = (6*hor_gap + 3*TILE_WIDTH, ver_gap, 6*hor_gap + 4*TILE_WIDTH, ver_gap+TILE_HEIGHT)

		BLANK_TILE1 = (4*hor_gap + TILE_WIDTH, 2*height + ver_gap, 
						4*hor_gap + 2*TILE_WIDTH, 2*height + ver_gap + TILE_HEIGHT)
		BLANK_TILE2 = (4*hor_gap + 2*TILE_WIDTH + 1, 2*height + ver_gap, 
						4*hor_gap + 3*TILE_WIDTH + 1, 2*height + ver_gap + TILE_HEIGHT)
		BLANK_TILE3 = (4*hor_gap + TILE_WIDTH, 2*height + ver_gap + TILE_HEIGHT+1, 
						4*hor_gap + 2*TILE_WIDTH, 2*height + ver_gap + 2*TILE_HEIGHT)
		BLANK_TILE4 = (4*hor_gap + 2*TILE_WIDTH + 1, 2*height + ver_gap + TILE_HEIGHT+1, 
						4*hor_gap + 3*TILE_WIDTH + 1, 2*height + ver_gap + 2*TILE_HEIGHT)

		# black portion of the screen // Rect((left, top), (width, height))
		screen_middle = Rect((0, IMAGE1_TILE[3]), 
						(5.2*deviceDisplay.current_w/8 , BLANK_TILE1[1]-IMAGE1_TILE[3]) )
		screen_left = Rect((0, IMAGE1_TILE[3]), (BLANK_TILE1[0], deviceDisplay.current_h-IMAGE1_TILE[3])) 
		screen_right = Rect((BLANK_TILE2[2], IMAGE1_TILE[3]), 
						(5.2*deviceDisplay.current_w/8-BLANK_TILE2[2], deviceDisplay.current_h-IMAGE1_TILE[3]))
		screen_down = Rect((0, BLANK_TILE4[3]),
						(5.2*deviceDisplay.current_w/8 , deviceDisplay.current_h-BLANK_TILE4[3]))

		timer_screen = Rect((5.8*deviceDisplay.current_w/8, BLANK_TILE1[1]-ver_gap), (width, TILE_HEIGHT))
		timer = 0

		pygame.font.init()
		gameFont = pygame.font.SysFont('times new roman', 25, True)
		timerText = gameFont.render('TIMER : ' + str(timer), False, FONT_COLOR)
		display.blit(timerText, (6*deviceDisplay.current_w/8, BLANK_TILE1[1]-ver_gap))

		pygame.display.flip()

		left_button_pressed = False
		mouse_dragged = False

		image1_dragged, image2_dragged, image3_dragged, image4_dragged = False, False, False, False
		image1_placed, image2_placed, image3_placed, image4_placed = False, False, False, False

		clock = pygame.time.Clock()

		isQuit = False
		waitFlag = False
		gameOverTime = None
		counter = 0

		while True:

			if isQuit:
				break

			clock.tick(60)
		
			#cur_time = int(time.time()*1000.0)
			cur_time = datetime.datetime.now().replace(microsecond = 0)
			times = cur_time - start_time
			

			if waitFlag == False:
				display.fill(CUSTOM_DISPLAY, timer_screen)

				timerText = gameFont.render('TIMER : ' + str(times), False, FONT_COLOR)
				display.blit(timerText, (6*deviceDisplay.current_w/8, BLANK_TILE1[1]-ver_gap))
				#pygame.display.update()
			else:
				#gameOverTime = str(times)
				display.fill(CUSTOM_DISPLAY, timer_screen)

				gameOverText = gameFont.render('  ** GAME OVER ** ', False, FONT_COLOR)
				timerText = gameFont.render('Elapsed Time : ' + gameOverTime, False, FONT_COLOR)
				display.blit(gameOverText, (6*deviceDisplay.current_w/8, BLANK_TILE1[1]-ver_gap))
				display.blit(timerText, (6*deviceDisplay.current_w/8, BLANK_TILE1[1]))
			

			

			for event in pygame.event.get():

				if event.type == QUIT:
					pygame.quit()
					isQuit = True
					break

				elif event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1: 
					left_button_pressed = True

					mouseX, mouseY = pygame.mouse.get_pos()

					if self.pointerIsInSurface(mouseX, mouseY, IMAGE1_TILE) and image1_placed == False:
						image1_dragged = True
						display.blit(black_rect, (IMAGE1_TILE[0], IMAGE1_TILE[1]))
							
					elif self.pointerIsInSurface(mouseX, mouseY, IMAGE2_TILE) and image2_placed == False:
							image2_dragged = True
							display.blit(black_rect, (IMAGE2_TILE[0], IMAGE2_TILE[1]))

					elif self.pointerIsInSurface(mouseX, mouseY, IMAGE3_TILE) and image3_placed == False:
							image3_dragged = True
							display.blit(black_rect, (IMAGE3_TILE[0], IMAGE3_TILE[1]))

					elif self.pointerIsInSurface(mouseX, mouseY, IMAGE4_TILE) and image4_placed == False:
							image4_dragged = True
							display.blit(black_rect, (IMAGE4_TILE[0], IMAGE4_TILE[1]))

				

				elif mouse_dragged and event.type == pygame.MOUSEBUTTONUP:
					left_button_pressed = False
					mouse_dragged = False

					mouseX, mouseY = pygame.mouse.get_pos()

					if mouseX < BLANK_TILE1[0] and mouseY < BLANK_TILE1[1]:
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
						if self.pointerIsInSurface(mouseX, mouseY, BLANK_TILE1):
							if image1_dragged:
								display.blit(image1, (BLANK_TILE1[0], BLANK_TILE1[1]))
								image1_placed = True

						elif self.pointerIsInSurface(mouseX, mouseY, BLANK_TILE2):
							if image2_dragged:
								display.blit(image2, (BLANK_TILE2[0], BLANK_TILE2[1]))
								image2_placed = True

						elif self.pointerIsInSurface(mouseX, mouseY, BLANK_TILE3):
							if image3_dragged:
								display.blit(image3, (BLANK_TILE3[0], BLANK_TILE3[1]))
								image3_placed = True

						elif self.pointerIsInSurface(mouseX, mouseY, BLANK_TILE4):
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

					if mouseY  > ver_gap + TILE_HEIGHT and mouseX < 5.2*deviceDisplay.current_w/8:
						if image1_dragged:
							display.blit(image1, (mouseX, mouseY))

						elif image2_dragged:
							display.blit(image2, (mouseX, mouseY))

						elif image3_dragged:
							display.blit(image3, (mouseX, mouseY))

						elif image4_dragged:
							display.blit(image4, (mouseX, mouseY))



				pygame.display.flip()

				'''
				if waitFlag == True and counter < 1:
					counter += 1
					title = "Puzzle Game"
					ques = "Want to play another Game?\t"
					reply = QMessageBox.question(None, title, ques, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

					if reply == QtWidgets.QMessageBox.Yes:
						ObjectID += 1
						self.game = JigsawPuzzle()
						self.game.initGame(ObjectID)
				'''
				display.fill(CUSTOM_DISPLAY, screen_middle)
				display.fill(CUSTOM_DISPLAY, screen_left)
				display.fill(CUSTOM_DISPLAY, screen_right)
				display.fill(CUSTOM_DISPLAY, screen_down)


				display.blit(hor_line, (BLANK_TILE1[0], BLANK_TILE1[1]+TILE_HEIGHT))
				display.blit(ver_line, (BLANK_TILE2[0]-1, BLANK_TILE2[1]-1))

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
					

				if waitFlag == True and counter < 1:
					counter += 1
					title = "Puzzle Game"
					ques = "Want to play another Game?\t"
					reply = QMessageBox.question(None, title, ques, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

					if reply == QtWidgets.QMessageBox.Yes:
						ObjectID += 1
						self.game = JigsawPuzzle()
						self.game.initGame(ObjectID)


				if image1_placed and image2_placed and image3_placed and image4_placed and waitFlag == False:

					cur_time = datetime.datetime.now().replace(microsecond = 0)
					times = cur_time - start_time
					gameOverTime = str(times)
					print(times)
					waitFlag = True

					mCursor = mydb.cursor(buffered=True)
					sql = "update game set elapsedTime=%s where game_id=%s"
					val = (gameOverTime,ObjectID,)
					print(ObjectID)
					mCursor.execute(sql, val)
					mydb.commit()
					mCursor.close()	
					mydb.close()




	def pointerIsInSurface(self, mouseX, mouseY, TILE):
		if (TILE[0] <= mouseX <= TILE[2]) and (TILE[1] <= mouseY <= TILE[3]):
			return True
		return False


if __name__ == "__main__":
	jigsaw = JigsawPuzzle()
	ObjectID=1
	jigsaw.initGame(ObjectID)
	#sys.exit(app.exec_())
