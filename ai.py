import connect4
import random

def analyze_choices(depth, player, ai, board):

    clone = connect4.clone_board(board)

    if player == ai:
        top_result = -1000000
        top_column = -1
        minmax = 1

    else:
        top_result = 10000000
        top_column = -1
        minmax = -1


    columns = connect4.open_columns(clone)

    for column in columns:

        win = connect4.drop_piece(column, player, clone)

        if win == True:
            if minmax == 1:
                result = 10000
            else:
                result = -10000

        elif len(connect4.open_columns(clone)) == 0:
            result = 1

        elif depth > 0:
            if player == 1:
                result = analyze_choices(depth-1, 2, ai, clone)[0]
            else:
                result = analyze_choices(depth-1, 1, ai, clone)[0]

        else:
            result = 0

        if minmax == 1 and result > top_result:
            top_result = result
            top_column = column

        elif minmax == -1 and result < top_result:
            top_result = result
            top_column = column

        elif result == top_result:
            if random.randint(0,1) == 1:
                top_result = result
                top_column = column

        connect4.undo_piece(column, clone)

    return [top_result, top_column]
