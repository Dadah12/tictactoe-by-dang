import random

def ai_move(board, buttons):
    """
    Random AI move for TicTacToe.
    """
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        buttons[row][col]['text'] = 'O'
        buttons[row][col]['state'] = 'disabled'

def smart_ai_move(board, buttons):
    """
    Smarter AI for TicTacToe (tries to win, block, center, corner, then random).
    """
    # Try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = 'O'
                if check_win(board, 'O'):
                    buttons[r][c]['text'] = 'O'
                    buttons[r][c]['state'] = 'disabled'
                    return
                board[r][c] = ''
    # Block X from winning
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = 'X'
                if check_win(board, 'X'):
                    board[r][c] = 'O'
                    buttons[r][c]['text'] = 'O'
                    buttons[r][c]['state'] = 'disabled'
                    return
                board[r][c] = ''
    # Take center if available
    if board[1][1] == '':
        board[1][1] = 'O'
        buttons[1][1]['text'] = 'O'
        buttons[1][1]['state'] = 'disabled'
        return
    # Take a corner if available
    for r, c in [(0,0), (0,2), (2,0), (2,2)]:
        if board[r][c] == '':
            board[r][c] = 'O'
            buttons[r][c]['text'] = 'O'
            buttons[r][c]['state'] = 'disabled'
            return
    # Random move if nothing else
    ai_move(board, buttons)

def check_win(board, p):
    """
    Checks if player 'p' has won.
    """
    for i in range(3):
        if all(board[i][j] == p for j in range(3)):
            return True
        if all(board[j][i] == p for j in range(3)):
            return True
    if all(board[i][i] == p for i in range(3)):
        return True
    if all(board[i][2 - i] == p for i in range(3)):
        return True
    return False
