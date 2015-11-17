import connect4
import random


class ai(object):

    def __init__(self, ai):
        self.FOUR_SCORE = 10000000
        self.THREE_SCORE = 2000
        self.TWO_SCORE = 10
        self.TIE_SCORE = 0
        self.SELF_SCORE = 1
        self.OPPONENT_SCORE = 1
        self.ai = ai

        if ai == 1:
            self.opponent = 2

        else:
            self.opponent = 1

    def set_THREE_SCORE(self, score):
        self.THREE_SCORE = score

    def set_TWO_SCORE(self, score):
        self.TWO_SCORE = score

    def set_TIE_SCORE(self, score):
        self.TIE_SCORE = score

    def set_SELF_SCORE(self, score):
        self.SELF_SCORE = score

    def set_OPPONENT_SCORE(self, score):
        self.OPPONENT_SCORE = score



    def analyze_choices(self, depth, player, board):

        if player == self.ai:
            top_score = -1000000000000000
            top_column = -1
            minmax = 1

        else:
            top_score = 100000000000000
            top_column = -1
            minmax = -1


        columns = connect4.open_columns(board)

        for column in columns:

            win = connect4.drop_piece(column, player, board)

            if win == True:
                if player == self.ai:
                    score = self.FOUR_SCORE * self.SELF_SCORE
                    connect4.undo_piece(column, board)
                    return [score, column]

                else:
                    score = self.FOUR_SCORE * -1 * self.OPPONENT_SCORE
                    connect4.undo_piece(column, board)
                    return [score, column]

            elif len(connect4.open_columns(board)) == 0:
                score = TIE_SCORE

            elif depth > 0:
                if player == 1:
                    score = self.analyze_choices(depth-1, 2, board)[0]

                else:
                    score = self.analyze_choices(depth-1, 1, board)[0]

            else:
                score = self.evaluate(board)

            if player == self.ai:
                if score == self.FOUR_SCORE * self.SELF_SCORE:
                    connect4.undo_piece(column, board)
                    return [score, column]

            else:
                if score == self.FOUR_SCORE * -1 * self.OPPONENT_SCORE:

                    connect4.undo_piece(column, board)

                    return [score, column]

            if player == self.ai and score > top_score:
                top_score = score
                top_column = column

            elif player == self.opponent and score < top_score:
                top_score = score
                top_column = column

            elif score == top_score:
                if random.randint(0,1) == 1:
                    top_score = score
                    top_column = column

            #print score

            connect4.undo_piece(column, board)

        return [top_score, top_column]


    def evaluate(self, board):
        score = 0

        score += connect4.find_threes(self.ai, board) * self.THREE_SCORE * self.SELF_SCORE
        score += connect4.find_twos(self.ai, board) * self.TWO_SCORE * self.SELF_SCORE

        score -= connect4.find_threes(self.opponent, board) * self.THREE_SCORE * self.OPPONENT_SCORE
        score -= connect4.find_twos(self.opponent, board) * self.TWO_SCORE * self.OPPONENT_SCORE

        return score
