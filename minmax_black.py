from minmax import maxMin
from utils import readInput, writeOutput, visualize, swap

def MiniMaxOpeningBlack(input_file, output_file, depth, visual=False):

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


def MiniMaxGameBlack(input_file, output_file, depth, visual=False):
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

