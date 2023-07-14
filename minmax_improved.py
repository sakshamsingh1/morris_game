from morris import improvedStaticEstimate, GenerateMovesOpening, GenerateMovesMidgameEndgame
from utils import readInput, writeOutput, visualize, swap


def maxMin(position, depth, num_eval, phase='opening'):
    f = GenerateMovesOpening
    if phase == 'midgame_endgame':
        f = GenerateMovesMidgameEndgame

    if depth == 0:
        curr_obj = improvedStaticEstimate(position, player='W', opponent='B', phase=phase)
        if phase == 'opening':
            curr_val = curr_obj.opening_est()
        else:
            curr_val = curr_obj.midgame_endgame_est()
        # print("Position:", "".join(position), "Value:", curr_val)
        return position, curr_val, num_eval + 1

    max_move = None
    max_val = float('-inf')

    children = f(position, player='W', opponent='B')
    for move in children:
        _, curr_val, num_eval = minMax(move, depth-1, num_eval, phase=phase)
        if curr_val > max_val:
            max_val = curr_val
            max_move = move

    return max_move, max_val, num_eval

def minMax(position, depth, num_eval, phase='opening'):
    f = GenerateMovesOpening
    if phase == 'midgame_endgame':
        f = GenerateMovesMidgameEndgame

    if depth == 0:
        curr_obj = improvedStaticEstimate(position, player='B', opponent='W', phase=phase)
        if phase == 'opening':
            curr_val = curr_obj.opening_est()
        else:
            curr_val = curr_obj.midgame_endgame_est()
        # print("Position:", "".join(position), "Value:", curr_val)
        return position, curr_val, num_eval + 1

    min_move = None
    min_val = float('inf')

    children = f(position, player='B', opponent='W')
    for move in children:
        curr_move, curr_val, num_eval = maxMin(move, depth-1, num_eval, phase=phase)
        if curr_val < min_val:
            min_val = curr_val
            min_move = move

    return min_move, min_val, num_eval



def MiniMaxOpeningImproved(input_file, output_file, depth, visual=False):

    input_position = readInput(input_file)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, depth, num_eval, phase='opening')

    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)

    return best_val


def MiniMaxGameImproved(input_file, output_file, depth, visual=False):
    input_position = readInput(input_file)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, depth, num_eval, phase='midgame_endgame')

    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)

    return best_val

def MiniMaxOpeningImprovedBlack(input_file, output_file, depth, visual=False):

    input_position = readInput(input_file)
    input_position = swap(input_position)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, depth, num_eval, phase='opening')

    best_move = swap(best_move)
    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)

    return best_val

def MiniMaxGameImprovedBlack(input_file, output_file, depth, visual=False):
    input_position = readInput(input_file)
    input_position = swap(input_position)

    num_eval = 0
    best_move, best_val, num_eval = maxMin(input_position, depth, num_eval, phase='midgame_endgame')

    best_move = swap(best_move)
    writeOutput(output_file, best_move)

    # Print the results
    print("Board Position:", "".join(best_move))
    print("Positions evaluated by static estimation:", num_eval)
    print("MINIMAX estimate:", best_val)

    if visual:
        visualize(input_position)
        visualize(best_move)

    return best_val

