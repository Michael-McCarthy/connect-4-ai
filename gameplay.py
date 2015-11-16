import connect4
import ai

players = [1,2]


if __name__=='__main__':

    print "hi"

    winner = False

    player = 0
    currentplayer = players[0]

    board = connect4.real_board

    while winner == False and len(connect4.open_columns(board)) > 0:

        connect4.print_board(board)

        if currentplayer == 1:

            open_columns = connect4.open_columns(board)

            print "Open columns: " + str(open_columns)

            column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            while column not in open_columns:
                print "ERROR: " + str(column) + " is not a valid open column"

                print "Open columns: " + str(open_columns)

                column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

            winner = connect4.drop_piece(column, currentplayer, board)

        else:
            column = ai.analyze_choices(5, 2, 2, board)[1]
            print "DROP AT: " + str(column)
            winner = connect4.drop_piece(column, currentplayer, board)



        if winner != True:
            if player == 1:
                player = 0

            else:
                player = 1

            currentplayer = players[player]

    if winner == False:
        print "DRAW"
        connect4.print_board(board)

    else:
        print "Player " + str(currentplayer) + " Wins!"
        connect4.print_board(board)
