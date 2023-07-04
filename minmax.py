from morris import baseStaticEstimate, GenerateMovesOpening, GenerateMovesMidgameEndgame, visualize

def maxMin(position, depth, num_eval, phase='opening'):
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
        curr_val = baseStaticEstimate(position).opening_est()
        return position, curr_val, num_eval+1

    min_move = None
    min_val = float('inf')

    children = f(position)
    for move in children:
        curr_move, curr_val, num_eval = maxMin(move, depth-1, num_eval, phase=phase)
        if curr_val < min_val:
            min_val = curr_val
            min_move = move

    return min_move, min_val, num_eval

def writeOutput(output_file, best_move):
    with open(output_file, 'w') as f:
        best_move = "".join(best_move)
        f.write(best_move)

def readInput(input_file):
    with open(input_file, 'r') as f:
        input_position = f.read().strip()

    if len(input_position)!=21:
        raise ValueError("Input position must be 21 characters long")

    return list(input_position)

def MiniMaxOpening(input_file, output_file, depth, visual=False):

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


def MiniMaxGame(input_file, output_file, depth, visual=False):
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


def ABOpening(input,output,depth):
    pass

def ABGame(input,output,depth):
    pass




"""
MaxMin(x):
if x is a leaf return static(x).
else {
set v = −∞
for each child y of x:
v = max(v, MinMax(y))
return v
}
"""
# def MaxMin(x):
#     if x is leaf:
#         return static(x)
#     else:
#         v = -inf
#         for each child y of x:
#             v = max(v, MinMax(y))
#         return v

"""
MinMax(x):
if x is a leaf return static(x).
else {
set v = +∞
for each child y of x:
v = min(v, MaxMin(y))
return v
}"""