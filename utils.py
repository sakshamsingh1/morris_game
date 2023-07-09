
# def swap(board):
#     board = "".join(board)
#     board.replace("W", "B").replace("B", "W")
#     return list(board)

def swap(board):
        invertedboard = []
        for i in board:
            if i == "W":
                invertedboard.append("B")
            elif i == "B":
                invertedboard.append("W")
            else:
                invertedboard.append("x")
        return invertedboard

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

def visualize(board):
    board = list(board)
    for i in range(len(board)):
        if board[i] == "x":
            board[i] = "."

    print(board[18] + "---------------------" + board[19] +
          "---------------------" + board[20] + "")
    print("|                     |                     |")
    print("|       " + board[15] + "-------------" +
          board[16] + "--------------" + board[17] + "      |")
    print("|       |             |              |      |")
    print("|       |         " + board[12] + "---" +
          board[13] + "---" + board[14] + "          |      |")
    print("|       |         |       |          |      |")
    print(board[6] + "-------" + board[7] + "---------" + board[8] + "       " +
          board[9] + "----------" + board[10] + "------" + board[11] + "")
    print("|       |         |       |          |      |")
    print("|       |         " + board[4] + "--" +
          "-" + "----" + board[5] + "          |      |")
    print("|       |                            |      |")
    print("|       " + board[2] + "------------" +
          "-" + "---------------" + board[3] + "      |")
    print("|                                           |")
    print(board[0] + "----------------" + "-" +
          "--------------------------" + board[1] + "")
    print("\n")


def visualizeBig(board):
    board = list(board)
    for i in range(len(board)):
        if board[i] == "x":
            board[i] = "."

    print(board[18] + "---------------------------" + board[19] +
          "---------------------------" + board[20] + "")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + board[15] + "-------------------" +
          board[16] + "--------------------" + board[17] + "      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |         " + board[12] + "---------" +
          board[13] + "---------" + board[14] + "          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[6] + "-------" + board[7] + "---------" + board[8] + "                   " +
          board[9] + "----------" + board[10] + "------" + board[11] + "")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         " + board[4] + "--------" +
          "-" + "----------" + board[5] + "          |      |")
    print("|       |                                        |      |")
    print("|       |                                        |      |")
    print("|       " + board[2] + "------------------" +
          "-" + "---------------------" + board[3] + "      |")
    print("|                                                       |")
    print("|                                                       |")
    print(board[0] + "----------------------------" + "-" +
          "--------------------------" + board[1] + "")
    print("\n")





def visualizeVerbose(board):
    board = list(board)
    for i in range(len(board)):
        if board[i] == "x":
            board[i] = "."

    print(board[18] + "(18)----------------------" + board[19] +
          "(19)----------------------" + board[20] + "(20)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + board[15] + "(15)--------------" +
          board[16] + "(16)--------------" + board[17] + "(17)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + board[12] + "(12)-----" +
          board[13] + "(13)-----" + board[14] + "(14)       |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[6] + "(06)---" + board[7] + "(07)----" + board[8] + "(08)               " +
          board[9] + "(09)----" + board[10] + "(10)---" + board[11] + "(11)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + board[4] + "(04)-----" +
          "-" + "---------" + board[5] + "(05)       |      |")
    print("|       |                                        |      |")
    print("|       |                                        |      |")
    print("|       " + board[2] + "(02)--------------" +
          "-" + "-----------------" + board[3] + "(03)      |")
    print("|                                                       |")
    print("|                                                       |")
    print(board[0] + "(00)----------------------" + "-" +
          "--------------------------" + board[1] + "(01)")
    print("\n")

def neighbors(j):
    if j == 0:
        return [1, 6]
    elif j == 1:
        return [0, 11]
    elif j == 2:
        return [3, 7]
    elif j == 3:
        return [2, 10]
    elif j == 4:
        return [5, 8]
    elif j == 5:
        return [4, 9]
    elif j == 6:
        return [0, 7, 18]
    elif j == 7:
        return [2, 6, 8, 15]
    elif j == 8:
        return [4, 7, 12]
    elif j == 9:
        return [5, 10, 14]
    elif j == 10:
        return [3, 9, 11, 17]
    elif j == 11:
        return [1, 10, 20]
    elif j == 12:
        return [8, 13]
    elif j == 13:
        return [12, 14, 16]
    elif j == 14:
        return [9, 13]
    elif j == 15:
        return [7, 16]
    elif j == 16:
        return [13, 15, 17, 19]
    elif j == 17:
        return [10, 16]
    elif j == 18:
        return [6, 19]
    elif j == 19:
        return [16, 18, 20]
    elif j == 20:
        return [11, 19]
    else:
        raise ValueError(f"Invalid position {j}")

def closeMill(j, b):
    C = b[j]
    if C == "x":
        raise ValueError(f"Board at {j} cannot be empty")
    elif j == 0:
        return ((b[6] == C) and (b[18] == C))
    elif j == 1:
        return (b[11] == C) and b[20] == C
    elif j == 2:
        return (b[7] == C and b[15] == C)
    elif j == 3:
        return b[10] == C and b[17] == C
    elif j == 4:
        return b[8] == C and b[12] == C
    elif j == 5:
        return b[9] == C and b[14] == C
    elif j == 6:
        return (b[0] == C and b[18] == C) or (b[7] == C and b[8] == C)
    elif j == 7:
        return (b[2] == C and b[15] == C) or (b[6] == C and b[8] == C)
    elif j == 8:
        return (b[4] == C and b[12] == C) or (b[6] == C and b[7] == C)
    elif j == 9:
        return (b[10] == C and b[11] == C) or (b[5] == C and b[14] == C)
    elif j == 10:
        return (b[3] == C and b[17] == C) or (b[9] == C and b[11] == C)
    elif j == 11:
        return (b[1] == C and b[20] == C) or (b[9] == C and b[10] == C)
    elif j == 12:
        return (b[13] == C and b[14] == C) or (b[4] == C and b[8] == C)
    elif j == 13:
        return (b[12] == C and b[14] == C) or (b[16] == C and b[19] == C)
    elif j == 14:
        return (b[12] == C and b[13] == C) or (b[5] == C and b[9] == C)
    elif j == 15:
        return (b[2] == C and b[7] == C) or (b[16] == C and b[17] == C)
    elif j == 16:
        return (b[15] == C and b[17] == C) or (b[13] == C and b[19] == C)
    elif j == 17:
        return (b[3] == C and b[10] == C) or (b[15] == C and b[16] == C)
    elif j == 18:
        return (b[0] == C and b[6] == C) or (b[19] == C and b[20] == C)
    elif j == 19:
        return (b[18] == C and b[20] == C) or (b[13] == C and b[16] == C)
    elif j == 20:
        return (b[1] == C and b[11] == C) or (b[18] == C and b[19] == C)
    else:
        raise ValueError(f"Invalid location {j}")







