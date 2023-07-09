from morris import baseStaticEstimate, GenerateMovesOpening, GenerateMovesMidgameEndgame
from utils import readInput, writeOutput, visualize

def ABOpening(input_file, output_file,depth, visual=False):
    input_position = readInput(input_file)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, float('-inf'), float('inf'), depth, num_eval, phase='opening')

    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)

def ABGame(input_file, output_file, depth, visual=False):
    input_position = readInput(input_file)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, float('-inf'), float('inf'), depth, num_eval, phase='midgame_endgame')

    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)


def maxMin(position, alpha, beta, depth, num_eval, phase='opening'):
    f = GenerateMovesOpening
    if phase == 'midgame_endgame':
        f = GenerateMovesMidgameEndgame

    if depth == 0:
        curr_obj = baseStaticEstimate(position)
        if phase == 'opening':
            curr_val = curr_obj.opening_est()
        else:
            curr_val = curr_obj.midgame_endgame_est()
        return position, curr_val, num_eval + 1

    max_move = None
    max_val = float('-inf')

    children = f(position)
    for move in children:
        _, curr_val, num_eval = minMax(move, alpha, beta, depth-1, num_eval, phase=phase)
        if curr_val > max_val:
            max_val = curr_val
            max_move = move
        if max_val >= beta:
            return max_move, max_val, num_eval
        else:
            alpha = max(max_val, alpha)

    return max_move, max_val, num_eval

def minMax(position, alpha, beta, depth, num_eval, phase='opening'):
    f = GenerateMovesOpening
    if phase == 'midgame_endgame':
        f = GenerateMovesMidgameEndgame

    if depth == 0:
        curr_obj = baseStaticEstimate(position)
        if phase == 'opening':
            curr_val = curr_obj.opening_est()
        else:
            curr_val = curr_obj.midgame_endgame_est()
        return position, curr_val, num_eval + 1

    min_move = None
    min_val = float('inf')

    children = f(position)
    for move in children:
        _, curr_val, num_eval = maxMin(move, alpha, beta, depth-1, num_eval, phase=phase)
        if curr_val < min_val:
            min_val = curr_val
            min_move = move

        if min_val <= alpha:
            return min_move, min_val, num_eval
        else:
            beta = min(min_val, beta)

    return min_move, min_val, num_eval

