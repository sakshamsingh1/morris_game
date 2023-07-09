from minmax import MiniMaxGame, MiniMaxOpening
from alpha_beta_pruning import *

def main():
    visual = False
    input_file = 'sample_input.txt'
    output_file = 'sample_output.txt'
    depth = 2
    # MiniMaxOpening(input_file, output_file, depth, visual)
    MiniMaxGame(input_file, output_file, depth, visual)
    # ABOpening(input_file, output_file, depth, visual)
    # ABGame(input_file, output_file, depth, visual)
if __name__ == '__main__':
    main()

