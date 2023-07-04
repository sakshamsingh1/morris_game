from utils import *

def GenerateMovesOpening(board):
    return GenerateAdd(board)

def GenerateAdd(board):
    L = []
    for i in range(len(board)):
        if board[i] == "x":
            b = board.copy()
            b[i] = "W"
            if closeMill(i, b):
                GenerateRemove(b, L)
            else:
                L.append(b)
    return L

def GenerateRemove(board, L):
    count_removed = 0
    for i in range(len(board)):
        if board[i] == "B":
            if not closeMill(i, board):
                count_removed += 1
                b = board[:]
                b[i] = "x"
                L.append(b)
    if count_removed == 0:
        L.append(board)


def GenerateMove(board):
    L = []
    for i in range(len(board)):
        if board[i] == "W":
            n = neighbors(i)
            for j in n:
                if board[j] == "x":
                    b = board[:]
                    b[i] = "x"
                    b[j] = "W"
                    if closeMill(j, b):
                        GenerateRemove(b, L)
                    else:
                        L.append(b)
    return L





def GenerateHopping(board):
    L = []
    for alpha in range(len(board)):
        if board[alpha] == "W":
            for beta in range(len(board)):
                if board[beta] == "x":
                    b = board[:]
                    b[alpha] = "x"
                    b[beta] = "W"
                    if closeMill(beta, b):
                        GenerateRemove(b, L)
                    else:
                        L.append(b)
    return L

def GenerateMovesMidgameEndgame(board):
    if board.count("W") == 3:
        return GenerateHopping(board)
    else:
        return GenerateMove(board)

def swap(board):
    board = "".join(board)
    board.replace("W", "B").replace("B", "W")
    return list(board)

def blackGenerateMovesMidgameEndgame(board):
    board = swap(board)
    cand_pos = GenerateMovesMidgameEndgame(list(board))
    return [swap(b) for b in cand_pos]
class baseStaticEstimate():
    def __init__(self, board):
        self.num_white = board.count("W")
        self.num_black = board.count("B")
        self.num_black_moves = len(blackGenerateMovesMidgameEndgame(board))

    def midgame_endgame_est(self):
        if self.num_black <= 2:
            return 10000
        elif self.num_white <= 2:
            return -10000
        elif self.num_black_moves == 0:
            return 10000
        else:
            return (1000 * (self.num_white - self.num_black)) - self.num_black_moves

    def opening_est(self):
        return self.num_white - self.num_black