import connect4

players = [1,2]


if __name__=='__main__':

    print "hi"

    winner = False

    player = 0
    currentplayer = players[0]

    while winner == False and len(connect4.open_columns()) > 0:

        connect4.print_board()

        open_columns = connect4.open_columns()

        print "Open columns: " + str(open_columns)

        column = input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

        while int(column) not in open_columns:
            print "ERROR: " + str(column) + " is not a valid open column"

            print "Open columns: " + str(open_columns)

            column = raw_input("Player " + str(currentplayer) + " choose an open column to drop your piece in: \n")

        winner = connect4.drop_piece(column, currentplayer)

        if winner != True:
            if player == 1:
                player = 0

            else:
                player = 1

            currentplayer = players[player]

    if winner == False:
        print "DRAW"
        connect4.print_board()

    else:
        print "Player " + str(currentplayer) + " Wins!"
        connect4.print_board()
