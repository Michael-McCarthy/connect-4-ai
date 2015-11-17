import connect4
import ai

if __name__=='__main__':

    # Set this to 0 for ai vs ai games
    human = 1


    #Tracks if any player has won the game
    winner = False

    currentplayer = 1

    board = connect4.real_board

    #initalize a player 1 ai if no human
    if human == 0:
        ai1 = ai.ai(1)

    #ai1.set_SELF_SCORE(10)

    #initalize player 2 ai
    ai2 = ai.ai(2)

    #ai2.set_OPPONENT_SCORE(10)

    #while no winner and there are still moves available
    while winner == False and len(connect4.open_columns(board)) > 0:

        connect4.print_board(board)

        #Human move
        if currentplayer == 1 and human > 0:

            open_columns = connect4.open_columns(board)

            print "Open columns: " + str(open_columns)

            column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            while column not in open_columns:
                print "ERROR: " + str(column) + " is not a valid open column"

                print "Open columns: " + str(open_columns)

                column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            winner = connect4.drop_piece(column, currentplayer, board)
        #ai player 1 move
        elif currentplayer == 1:
            column = ai1.analyze_choices(3, 1, board)[1]
            print "DROP AT: " + str(column)
            winner = connect4.drop_piece(column, currentplayer, board)
        #ai player 2 move
        else:
            column = ai2.analyze_choices(3, 2, board)[1]
            print "DROP AT: " + str(column)
            winner = connect4.drop_piece(column, currentplayer, board)


        #if no winner, switch players
        if winner != True:
            if currentplayer == 1:
                currentplayer = 2

            else:
                currentplayer = 1

    #if filled board, draw
    if winner == False:
        print "DRAW"
        connect4.print_board(board)

    #else print player who made the final move
    else:
        print "Player " + str(currentplayer) + " Wins!"
        connect4.print_board(board)
