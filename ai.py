import connect4
import random
import sys


class ai(object):

    def __init__(self, ai):
        self.FOUR_SCORE = 10000
        self.THREE_SCORE = 20
        self.TWO_SCORE = 1
        self.TIE_SCORE = 0
        self.SELF_SCORE = 1
        self.OPPONENT_SCORE = 1
        self.MAX_DEPTH = 3
        self.ai = ai

        if ai == 1:
            self.opponent = 2

        else:
            self.opponent = 1

    def agressive_personality(self):
        self.SELF_SCORE = 20
        self.OPPONENT_SCORE = 1

    def defensive_personality(self):
        self.SELF_SCORE = 1
        self.OPPONENT_SCORE = 20

    def balanced_personality(self):
        self.SELF_SCORE = 1
        self.OPPONENT_SCORE = 1

    def easy_mode(self):
        self.set_THREE_SCORE(0)
        self.set_TWO_SCORE(0)

    def set_MAX_DEPTH(self, depth):
        self.MAX_DEPTH = depth

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


    def analyze_choices(self, depth, player, alpha, beta):

        if depth == 0:
            return [self.evaluate(), -1]

        elif player == self.ai:
            v = -sys.maxint
            maxcolumn = -1

            columns = connect4.open_columns()

            if len(columns) == 0:
                return [self.TIE_SCORE, -1]

            for column in columns:
                win = connect4.drop_piece(column, player)

                if win == True:
                    connect4.undo_piece(column)
                    return [self.FOUR_SCORE * self.SELF_SCORE, column]

                score = self.analyze_choices(depth-1,self.opponent, alpha, beta)[0]
                connect4.undo_piece(column)

                if score > v:
                    v = score
                    maxcolumn = column

                if v > alpha:
                    alpha = v

                if beta <= alpha:
                    break

            return [v, maxcolumn]


        else:
            v = sys.maxint

            mincolumn = -1

            columns = connect4.open_columns()

            if len(columns) == 0:
                return [self.TIE_SCORE, -1]

            for column in columns:
                win = connect4.drop_piece(column, player)

                if win == True:
                    connect4.undo_piece(column)
                    return [self.FOUR_SCORE * self.OPPONENT_SCORE * -1, column]
                score = self.analyze_choices(depth-1,self.ai, alpha, beta)[0]
                connect4.undo_piece(column)

                if score < v:
                    v = score
                    mincolumn = column

                if v < beta:
                    beta = v

                if beta <= alpha:
                    break

            return [v, mincolumn]



    def evaluate(self):
        score = 0

        score += connect4.find_threes(self.ai) * self.THREE_SCORE * self.SELF_SCORE
        score += connect4.find_twos(self.ai) * self.TWO_SCORE * self.SELF_SCORE

        score -= connect4.find_threes(self.opponent) * self.THREE_SCORE * self.OPPONENT_SCORE
        score -= connect4.find_twos(self.opponent) * self.TWO_SCORE * self.OPPONENT_SCORE

        return score
