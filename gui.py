import connect4
import pygame, sys
import ai
from pygame.locals import *


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

	press=pygame.mouse.get_pressed()
	if pressable:
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
					end = font.render("Player 2 Wins!", 0, (255,0,0), None)
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
				
				ai1 = ai.ai(1)
				column = ai1.analyze_choices(3, 2, -sys.maxint, sys.maxint)[1]
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
		