from morris import visualize
from minmax import *

def main():
    visual = True
    input_file = 'sample_input.txt'
    output_file = 'sample_output.txt'
    depth = 1
    # MiniMaxOpening(input_file, output_file, depth, visual)
    MiniMaxGame(input_file, output_file, depth, visual)
if __name__ == '__main__':
    main()

