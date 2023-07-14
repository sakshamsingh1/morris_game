from utils import visualize, readInput, writeOutput
from minmax_improved import MiniMaxGameImproved, MiniMaxOpeningImproved
from minmax_black import MiniMaxGameBlack, MiniMaxOpeningBlack

def AI_VS_AI():
    input_file = 'sample_input.txt'
    output_file = 'sample_output.txt'

    depth = 3

    init_board = ['x']*21
    writeOutput(input_file, init_board)

    print("Stage 1")
    for i in range(8):

        eval = MiniMaxOpeningImproved(input_file, output_file, depth, False)
        board = readInput(output_file)
        visualize(board)

        if eval == 10000 or eval == -10000:
            print("AI Bot 1 has won!")
            exit(0)

        eval = MiniMaxOpeningBlack(output_file, input_file, depth, False)
        board = readInput(input_file)
        visualize(board)

        if eval == 10000 or eval == -10000:
            print("AI Bot 2 has won!")
            exit(0)
    # return 0
    print("Stage 2")
    while True:

        eval = MiniMaxGameImproved(input_file, output_file, depth, False)
        board = readInput(output_file)
        visualize(board)

        if eval == 10000 or eval == -10000:
            print("AI Bot 1 has won!")
            exit(0)

        eval = MiniMaxGameBlack(output_file, input_file, depth, False)
        board = readInput(input_file)
        visualize(board)

        if eval == 10000 or eval == -10000:
            print("AI Bot 2 has won!")
            exit(0)


if __name__ == "__main__":
    AI_VS_AI()
