import connect4
import pygame, sys
import ai
from pygame.locals import *

def set_up_ai(ainum):
	AI = ai.ai(ainum)

	aipersonality = input("Would you like ai player " + str(ainum) + " to be (1)Agressive, (2)Defensive, or (3)Balanced? (1,2,3) \n")

	while aipersonality != 1 and aipersonality != 2 and aipersonality != 3:
		print "ERROR: not a valid input"
		aipersonality = input("Would you like ai player" + str(ainum) + " to be (1)Agressive, (2)Defensive, or (3)Balanced? (1,2,3) \n")

	if aipersonality == 1:
		AI.agressive_personality()

	elif aipersonality == 2:
		AI.defensive_personality()

	aidifficulty = input("Set the difficulty of ai player " + str(ainum)  + " in range(1-6). Note, higher difficulty = more processing time \n")

	while 1 > aidifficulty or 6 < aidifficulty:
		print "ERROR: not a valid input"
		aidifficulty = input("Set the difficulty of ai player " + str(ainum) + " in range(1-6). Note, higher difficulty = more processing time \n")

	AI.set_MAX_DEPTH(aidifficulty)

	aieasymode = input("Easy mode for ai player " + str(ainum) + "? Answer 0 for no, 1 for yes. This setting causes the AI to use a simpler heuristic. \n")

	while aieasymode != 0 and aieasymode != 1:
		print "ERROR: not a valid input"
		aieasymode = input("Easy mode for ai player " + str(ainum) + "? Answer 0 for no, 1 for yes. This setting causes the AI to use a simpler heuristic. \n")

	if aieasymode == 1:
		AI.easy_mode()

	return AI




computers = input("Would you like 1 ai or 2? (1,2)")

while computers != 1 and computers != 2:
	print "ERROR: Not a valid input"
	computers = input("Would you like 1 ai or 2? (1,2)")

if computers == 2:
	ai1 = set_up_ai(1)

ai2 = set_up_ai(2)



pygame.init()

DISPLAYSURF = pygame.display.set_mode((364, 312))
#board = pygame.image.load("c4board.png")
tile = pygame.image.load("boardtile.png")

board_display = [[0 for x in range(7)] for x in range(6)]

for i in range(6):
	for j in range(7):
		board_display[i][j] = tile

for i in range(6):
	for j in range(7):
		DISPLAYSURF.blit(board_display[i][j],(j*52,i*52))
pygame.display.update()


pygame.display.set_caption('Connect 4')

frame = 0
timer = 40
pressable = True
clock = pygame.time.Clock()

winner = False

while True: # main game loop
	frame+=1
	clock.tick(40)



	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	if computers == 2:
		if winner != True:
			column = ai1.analyze_choices(ai1.MAX_DEPTH, 1, -sys.maxint, sys.maxint)[1]
			for i in range(6):
				if connect4.board[i][column] != 0:
					row = i-1
					break
				elif i == 5:
					row = i
					break
			dropped = connect4.drop_piece(column,1)
			if dropped == True:
				font = pygame.font.Font(None, 75)
				text = 'Player 1 Wins!'
				end = font.render("Player 1 Wins!", 0, (255,0,0), None)
				DISPLAYSURF.blit(end,(0,0))
				winner = True
			tile = pygame.image.load("redtile.png")
			board_display[row][column] = tile
			DISPLAYSURF.blit(board_display[row][column],(column*52,row*52))
			pygame.display.update()

			if winner != True:
				column = ai2.analyze_choices(ai2.MAX_DEPTH, 2, -sys.maxint, sys.maxint)[1]
				for i in range(6):
					if connect4.board[i][column] != 0:
						row = i-1
						break
					elif i == 5:
						row = i
						break
				dropped = connect4.drop_piece(column,2)
				if dropped == True:
					yellow = 255, 255, 0
					font = pygame.font.Font(None, 75)
					text = 'Player 2 Wins!'
					end = font.render("Player 2 Wins!", 0, (255,255,0), None)
					DISPLAYSURF.blit(end,(0,0))
					winner = True
				tile = pygame.image.load("yellowtile.png")
				board_display[row][column] = tile
				DISPLAYSURF.blit(board_display[row][column],(column*52,row*52))
				pygame.display.update()



	press=pygame.mouse.get_pressed()
	if pressable and computers == 1:
		if press[0]:
			pressable = False
			column = pygame.mouse.get_pos()[0] / 52

			#print column
			dropped = connect4.drop_piece(column,1)
			tile=0
			tile = pygame.image.load("redtile.png")
			row = 0
			print connect4.board
			if dropped != -1:
				if dropped == True:
					font = pygame.font.Font(None, 75)
					end = font.render("Player 1 Wins!", 0, (255,0,0), None)
					DISPLAYSURF.blit(end,(0,0))
					winner = True
				for i in range(6):
					if connect4.board[i][column] != 0:
						row = i
						break
					elif i == 5:
						row = i
						break

				board_display[row][column] = tile
				DISPLAYSURF.blit(board_display[row][column],(column*52,row*52))
				pygame.display.update()
				connect4.print_board()
				print column
				print row
				if winner != True:
					column = ai2.analyze_choices(ai2.MAX_DEPTH, 2, -sys.maxint, sys.maxint)[1]
					for i in range(6):
						if connect4.board[i][column] != 0:
							row = i-1
							break
						elif i == 5:
							row = i
							break
					dropped = connect4.drop_piece(column,2)
					if dropped == True:
						yellow = 255, 255, 0
						font = pygame.font.Font(None, 75)
						text = 'Player 2 Wins!'
						end = font.render("Player 2 Wins!", 0, (255,255,0), None)
						DISPLAYSURF.blit(end,(0,0))
						winner = True
					tile = pygame.image.load("yellowtile.png")
					board_display[row][column] = tile
					DISPLAYSURF.blit(board_display[row][column],(column*52,row*52))
					pygame.display.update()



	if frame == timer and winner == False:
		frame=0
		pressable=True
