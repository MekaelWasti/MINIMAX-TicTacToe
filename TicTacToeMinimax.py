import numpy as np
from pyrsistent import b


board = np.array([
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
])

# board = np.array([
#     ["c","c","X"],
#     ["O","x","f"],
#     ["X","f","S"],
# ])

print(f'{board} \n')




def selectPosition(board, position:int, player:str):
    if position in range(0,10,1):
        row = int((position-1) /3)
        column = (position-1)%3
        board[row,column] = player
    else:
        print("\nInvalid Position\n")
        return

def has_won(board, player:str):
    win = None
    for move in range(3):
        checkColumn = board[:,move] == player
        checkRow = board[move,:] == player
        # print(f'CHECK ROW: {checkRow}')
        # print(f'CHECK Column: {checkColumn}')
        if checkColumn.all() or checkRow.all():
            win = True
            break
        else:
            continue    

    
    #Diagonal Check
    for check in range(0,3):
        if board[check,check] != player:
            win == False
            break
        if check == 2:
            win = True    
            
    for check in range(0,3):
        if board[check,abs(check-2)] != player:
            win == False
            break
        if check == 2:
            win = True     

    #Final Win Check 
    if win:
        print(f"{player} has won!")
    else:
        print(f"{player} has not won.")
    return
            

def availableMoves(board):
    moves = []
    for row in board:
        for column in row:
            if column != "O" and column != "X":
                moves.append(column) 
    return moves

def isTie(board):
    if not has_won(board,"X") and not has_won(board,"O") and len(availableMoves(board)) == 0:
        return True
    else:
        return False

def evaluateBoard(board):
    if not has_won(board,"X") and not has_won(board,"O") and len(availableMoves(board)) == 0:
        return True
    else:
        return False

def minimax(board, is_maximizing):
    
    if is_maximizing:
        value = 1
        player = "X"
    else:
        player = "O"
        value = -1

    # Base Case
    if has_won(board, "X") or has_won(board, "O") or isTie(board):
        return value

    for move in availableMoves:


        best_value = value
        best_move = move

print(f'{board} \n')
has_won(board,"X")

selectPosition(board,1,"X")
print(f'{board} \n')
has_won(board,"X")

selectPosition(board,2,"O")
print(f'{board} \n')
has_won(board,"X")

selectPosition(board,5,"X")
print(f'{board} \n')
has_won(board,"X")

selectPosition(board,6,"O")
print(f'{board} \n')
has_won(board,"X")

selectPosition(board,9,"X")
print(f'{board} \n')
has_won(board,"X")

# print(isTie(board))