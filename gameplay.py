import connect4
import ai
import sys


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



if __name__=='__main__':

    # Set this to 0 for ai vs ai games
    human = 1
	
    ai2 = set_up_ai(human)

    #Tracks if any player has won the game
    winner = False

    currentplayer = 1

    #initalize a player 1 ai if no human
    if human == 0:
        ai1 = ai.ai(1)

    #ai1.set_SELF_SCORE(10)

    #initalize player 2 ai
    #ai2 = ai.ai(2)
	

    #ai2.set_OPPONENT_SCORE(10)

    #while no winner and there are still moves available
    while winner == False and len(connect4.open_columns()) > 0:

        connect4.print_board()

        #Human move
        if currentplayer == 1 and human > 0:

            open_columns = connect4.open_columns()

            print "Open columns: " + str(open_columns)

            column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            while column not in open_columns:
                print "ERROR: " + str(column) + " is not a valid open column"

                print "Open columns: " + str(open_columns)

                column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            winner = connect4.drop_piece(column, currentplayer)
        #ai player 1 move
        elif currentplayer == 1:
            column = ai1.analyze_choices(4, 1, -sys.maxint, sys.maxint)[1]
            print "DROP AT: " + str(column)
            winner = connect4.drop_piece(column, currentplayer)
        #ai player 2 move
        else:
            column = ai2.analyze_choices(4, 2, -sys.maxint, sys.maxint)[1]
            print "DROP AT: " + str(column)
            winner = connect4.drop_piece(column, currentplayer)


        #if no winner, switch players
        if winner != True:
            if currentplayer == 1:
                currentplayer = 2

            else:
                currentplayer = 1

    #if filled board, draw
    if winner == False:
        print "DRAW"
        connect4.print_board()

    #else print player who made the final move
    else:
        print "Player " + str(currentplayer) + " Wins!"
        connect4.print_board()
