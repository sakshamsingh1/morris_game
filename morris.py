from utils import closeMill, neighbors, swap
from copy import deepcopy

def GenerateMovesOpening(board, player="W", opponent="B"):
    return GenerateAdd(board, player, opponent)

def GenerateAdd(board, player="W", opponent="B"):
    L = []
    for i in range(len(board)):
        if board[i] == "x":
            b = deepcopy(board)
            b[i] = player
            if closeMill(i, b):
                L = GenerateRemove(b, L, opponent)
            else:
                L.append(b)
    return L

def GenerateRemove(board, L, opponent):
    count_removed = 0
    for i in range(len(board)):
        if board[i] == opponent:
            if not closeMill(i, board):
                count_removed += 1
                b = deepcopy(board)
                b[i] = "x"
                L.append(b)
    if count_removed == 0:
        L.append(board)
    return L


def GenerateMove(board, player, opponent):
    L = []
    for i in range(len(board)):
        if board[i] == player:
            n = neighbors(i)
            for j in n:
                if board[j] == "x":
                    b = deepcopy(board)
                    b[i] = "x"
                    b[j] = player
                    if closeMill(j, b):
                        L = GenerateRemove(b, L, opponent)
                    else:
                        L.append(b)
    return L

def GenerateHopping(board, player, opponent):
    L = []
    for alpha in range(len(board)):
        if board[alpha] == player:
            for beta in range(len(board)):
                if board[beta] == "x":
                    b = deepcopy(board)
                    b[alpha] = "x"
                    b[beta] = player
                    if closeMill(beta, b):
                        L = GenerateRemove(b, L, opponent)
                    else:
                        L.append(b)
    return L

def GenerateMovesMidgameEndgame(board, player="W", opponent="B"):
    if board.count(player) == 3:
        return GenerateHopping(board, player, opponent)
    else:
        return GenerateMove(board, player, opponent)

def blackGenerateMovesMidgameEndgame(board):
    board = swap(board)
    cand_pos = GenerateMovesMidgameEndgame(board, player='W', opponent='B')
    return [swap(b) for b in cand_pos]

class baseStaticEstimate():
    def __init__(self, board, player, opponent):
        self.num_white = board.count(player)
        self.num_black = board.count(opponent)
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

class improvedStaticEstimate():
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