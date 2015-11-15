
board = [[0 for x in xrange(7)] for y in range(6)]


def open_columns():

    columns = []
    i = 0
    while i < 7:
        if board[0][i] == 0:
            columns.append(i)
        i += 1
    return columns


def reset_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0

def drop_piece(column, playernum):

    row = 0
    for i in range(6):
        if board[i][column] != 0:
            if i == 0:
                print "ERROR: Column already full"
                return -1
            board[i-1][column] = playernum
            row = i-1
            break
        elif i == 5:
            board[i][column] = playernum
            row = i
            break

    return check_win(row, column)

def check_win(row, column):
    if board[row][column] == 0:
        return False

    if check_horizontal(row, column) == True:
        return True

    if check_vertical(row, column) == True:
        return True

    if check_up_diag(row, column) == True:
        return True

    if check_down_diag(row, column) == True:
        return True

    return False


def check_horizontal(row, column):
    player = board[row][column]

    horizontal = 1

    right = board[row][column]

    right_counter = 0

    while column + right_counter < 6 and right == player:
        right = board[row][column + 1 + right_counter]
        if right == player:
            right_counter += 1

    horizontal += right_counter

    if horizontal >= 4:
        return True

    left = board[row][column]

    left_counter = 0

    while column - left_counter > 0 and left == player:
        left = board[row][column - 1 - left_counter]
        if left == player:
            left_counter += 1

    horizontal += left_counter

    if horizontal >= 4:
        return True

    return False


def check_vertical(row,column):
    player = board[row][column]


    vertical = 1

    up = board[row][column]

    up_counter = 0

    while row - up_counter > 0 and up == player:
        up = board[row - 1 - up_counter][column]
        if up == player:
            up_counter += 1

    vertical += up_counter

    if vertical >= 4:
        return True


    down = board[row][column]

    down_counter = 0

    while row + down_counter < 5 and down == player:
        down = board[row + 1 + down_counter][column]
        if down == player:
            down_counter += 1

    vertical += down_counter

    if vertical >= 4:
        return True

    return False

def check_up_diag(row, column):
    player = board[row][column]


    diag = 1

    up = board[row][column]

    up_counter = 0

    while row - up_counter > 0 and column + up_counter < 6 and up == player:
        up = board[row - 1 - up_counter][column + 1 + up_counter]
        if up == player:
            up_counter += 1

    diag += up_counter

    if diag >= 4:
        return True


    down = board[row][column]

    down_counter = 0

    while row + down_counter < 5 and column - down_counter > 0 and down == player:
        down = board[row + 1 + down_counter][column - 1 - down_counter]
        if down == player:
            down_counter += 1

    diag += down_counter

    if diag >= 4:
        return True

    return False

def check_down_diag(row, column):
    player = board[row][column]


    diag = 1

    up = board[row][column]

    up_counter = 0

    while row - up_counter > 0 and column - up_counter > 0 and up == player:
        up = board[row - 1 - up_counter][column - 1 - up_counter]
        if up == player:
            up_counter += 1

    diag += up_counter

    if diag >= 4:
        return True


    down = board[row][column]

    down_counter = 0

    while row + down_counter < 5 and column + down_counter < 6 and down == player:
        down = board[row + 1 + down_counter][column + 1 + down_counter]
        if down == player:
            down_counter += 1

    diag += down_counter

    if diag >= 4:
        return True

    return False





def print_board():
    for i in range(6):
        print board[i]

if __name__=='__main__':
    #print board

    print drop_piece(0,1)
    print drop_piece(1,2)
    print drop_piece(1,1)
    print drop_piece(2,2)
    print drop_piece(3,1)
    print drop_piece(2,2)

    print drop_piece(3,2)
    print drop_piece(3,1)
    print drop_piece(4,2)
    print drop_piece(3,1)
    print drop_piece(2,1)

    print_board()

    reset_board()

    print ""
    print drop_piece(4,1)
    print drop_piece(3,2)
    print drop_piece(2,2)
    print drop_piece(1,1)
    print drop_piece(2,2)
    print drop_piece(2,1)
    print drop_piece(1,2)
    print drop_piece(1,1)
    print drop_piece(0,2)
    print drop_piece(1,1)
    print drop_piece(3,1)

    print_board()
