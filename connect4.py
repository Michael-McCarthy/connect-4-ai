
real_board = [[0 for x in xrange(7)] for y in range(6)]


def open_columns(board):

    columns = []
    i = 0
    while i < 7:
        if board[0][i] == 0:
            columns.append(i)
        i += 1
    return columns


def reset_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0

def drop_piece(column, playernum, board):

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

    return check_win(row, column, board)

def undo_piece(column, board):
    for i in range(6):
        if board[i][column] != 0:
            board[i][column] = 0
            return True
    return False


def check_win(row, column, board):
    if board[row][column] == 0:
        return False

    if check_horizontal(row, column, board) == True:
        return True

    if check_vertical(row, column, board) == True:
        return True

    if check_up_diag(row, column, board) == True:
        return True

    if check_down_diag(row, column, board) == True:
        return True

    return False


def check_horizontal(row, column, board):
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


def check_vertical(row,column, board):
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

def check_up_diag(row, column, board):
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

def check_down_diag(row, column, board):
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


def find_threes(player, board):
    threes = [[0, player, player, player],
              [player, 0, player, player],
              [player, player, 0, player],
              [player, player, player, 0]]

    return find_sequences(player, board, threes)

def find_twos(player, board):
    twos = [  [0, 0, player, player],
              [0, player, 0, player],
              [0, player, player, 0],
              [player, 0, 0, player],
              [player, 0, player, 0],
              [player, player, 0, 0]]

    return find_sequences(player, board, twos)

def find_sequences(player, board, sequences):
    total = 0

    for row in board:
        for sequence in sequences:
            if str(sequence).strip("[]") in str(row).strip("[]"):
                total += 1

    for i in range(7):
        column = [row[i] for row in board]
        for sequence in sequences:
            if str(sequence).strip("[]") in str(column).strip("[]"):
                total += 1

    updiags = []

#    testupdiags = []

    for row in range(6):
        i = row
        j = 0
        diag = []
#        tud = []

        while i >= 0 and j < len(board[0]):
            diag.append(board[i][j])
#            tud.append([i,j])
            j = j + 1
            i = i - 1

        updiags.append(diag)

#        testupdiags.append(tud)


    for j in range(7):
        if j == 0:
            continue
        diag = []
        i = 5

#        tud = []

        while j < 7 and i >= 0:
            diag.append(board[i][j])
#            tud.append([i,j])

            j = j + 1
            i = i - 1
        updiags.append(diag)

#        testupdiags.append(tud)



    for updiag in updiags:
        for sequence in sequences:
            if str(sequence).strip("[]") in str(updiag).strip("[]"):
                    total += 1

    downdiags = []

#    testdowndiags = []

    for row in range(6):
        i = row
        j = 6
        diag = []
#        tdd = []

        while i >= 0 and j >= 0:
            diag.append(board[i][j])
#            tdd.append([i,j])
            j = j - 1
            i = i - 1

        downdiags.append(diag)

#        testdowndiags.append(tdd)

    for column in range(7):
        if column == 6:
            continue

        j = column
        diag = []

        i = 5

#        tdd = []

        while j >= 0 and i >= 0:
            diag.append(board[i][j])
#            tdd.append([i,j])
            j = j - 1
            i = i - 1

        downdiags.append(diag)

#        testdowndiags.append(tdd)



    for downdiag in downdiags:
        for sequence in sequences:
            if str(sequence).strip("[]") in str(downdiag).strip("[]"):
                    total += 1


#    print "--------------"
#    for row in testdowndiags:
#        print row
#    print "--------------"

    return total

def print_board(board):

    printer = [['.' for x in xrange(7)] for y in range(6)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                printer[i][j] = 'X'
            elif board[i][j] == 2:
                printer[i][j] = 'O'



    for i in range(6):
        print printer[i]

    columns = ['0','1','2','3','4','5','6']

    print columns

if __name__=='__main__':
    #print board

    print drop_piece(0,1, real_board)
    print drop_piece(1,2, real_board)
    print drop_piece(1,1, real_board)
    print drop_piece(2,2, real_board)
    print drop_piece(3,1, real_board)
    print drop_piece(2,2, real_board)

    print drop_piece(3,2, real_board)
    print drop_piece(3,1, real_board)
    print drop_piece(4,2, real_board)
    print drop_piece(3,1, real_board)
    print drop_piece(2,2, real_board)


    print find_threes(1, real_board)
    print find_threes(2, real_board)

    print_board(real_board)
