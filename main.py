import argparse

from minmax import MiniMaxGame, MiniMaxOpening
from alpha_beta_pruning import ABGame, ABOpening
from minmax_black import MiniMaxGameBlack, MiniMaxOpeningBlack
from minmax_improved import MiniMaxGameImproved, MiniMaxOpeningImproved

def main(args):
    visual = args.visual
    input_file = args.input_file
    output_file = args.output_file
    depth = args.depth

    if args.function == 'MiniMaxOpening':
        MiniMaxOpening(input_file, output_file, depth, visual)

    elif args.function == 'MiniMaxGame':
        MiniMaxGame(input_file, output_file, depth, visual)

    elif args.function == 'ABOpening':
        ABOpening(input_file, output_file, depth, visual)

    elif args.function == 'ABGame':
        ABGame(input_file, output_file, depth, visual)

    elif args.function == 'MiniMaxOpeningBlack':
        MiniMaxOpeningBlack(input_file, output_file, depth, visual)

    elif args.function == 'MiniMaxGameBlack':
        MiniMaxGameBlack(input_file, output_file, depth, visual)

    elif args.function == 'MiniMaxOpeningImproved':
        MiniMaxOpeningImproved(input_file, output_file, depth, visual)

    elif args.function == 'MiniMaxGameImproved':
        MiniMaxGameImproved(input_file, output_file, depth, visual)

    else:
        print("Invalid function name")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parameter Processing')
    parser.add_argument('--input_file', type=str, default='sample_input.txt', help='input file name')
    parser.add_argument('--output_file', type=str, default='sample_output.txt', help='output file name')
    parser.add_argument('--depth', type=int, default=2, help='depth of search tree')
    parser.add_argument('--visual', type=bool, default=False, help='visualize the game')
    parser.add_argument('--function', type=str, default='MiniMaxGameImproved', help='function to run')

    args = parser.parse_args()
    main(args)


