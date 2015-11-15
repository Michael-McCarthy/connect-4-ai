
board = [[0 for x in xrange(7)] for y in range(6)]


def drop_piece(column, playernum):
    for i in range(6):
        if board[i][column] != 0:
            if i == 0:
                print "ERROR: Column already full"
                break
            board[i-1][column] = playernum
            break
        elif i == 5:
            board[i][column] = playernum
            break

def check_win(row, column):
    if board[row][column] == 0:
        return False
    player = board[row][column]

    horizontal = 0

    right = 0

    right_counter = 0

    if column < 6:
        right = board[row][column+1]
        right_counter++


def print_board():
    for i in range(6):
        print board[i]

if __name__=='__main__':
    #print board

    drop_piece(0,1)
    drop_piece(0,2)
    drop_piece(1,1)
    drop_piece(2,2)

    print_board()
