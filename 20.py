# Tic-Tac-Toe winner
def winner(board):
    lines = []
    lines.extend(board)                                              
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  
    lines.append([board[i][i] for i in range(3)])                    
    lines.append([board[i][2 - i] for i in range(3)])                

    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return f"{line[0]} wins"

    if any(" " in row for row in board):
        return "Game still on"
    return "Draw"

board = [["X", "O", "X"],
         ["O", "X", "O"],
         ["O", "X", "X"]]
print(winner(board))   