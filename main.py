import tkinter as tk
from tkinter import messagebox
from ai import ai_move, smart_ai_move

mode = None  # Will be set after selecting a game mode

def select_mode():
    """
    Opens a window to select the game mode: 2 Player or 1 Player (vs AI).
    """
    def set_mode(selected):
        global mode
        mode = selected
        option_win.destroy()
        start_game()
    option_win = tk.Tk()
    option_win.title("TicTacToe - Options")
    label = tk.Label(option_win, text="Select Game Mode:", font=("Arial", 14))
    label.pack(pady=10)
    btn_2p = tk.Button(option_win, text="2 Player", width=20, font=("Arial", 12),
                      command=lambda: set_mode('2P'))
    btn_2p.pack(pady=8)
    btn_1p = tk.Button(option_win, text="1 Player (vs AI)", width=20, font=("Arial", 12),
                      command=lambda: set_mode('1P'))
    btn_1p.pack(pady=8)
    credit_label = tk.Label(option_win, text="Created by Juldah", font=('Arial', 10), fg='gray')
    credit_label.pack(side='bottom', pady=10)
    option_win.mainloop()

def start_game():
    """
    Initializes the TicTacToe game window and board.
    """
    global player, board, buttons, root
    player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    root = tk.Tk()
    root.title("TicTacToe - Created by Juldah")
    # Set a fixed, reasonable window size (e.g., 380x430)
    root.geometry("450x500")
    root.resizable(False, False)  # Prevent resizing

    frame = tk.Frame(root)
    frame.pack()

    for r in range(3):
        for c in range(3):
            buttons[r][c] = tk.Button(
                frame, text='', width=5, height=2, font=('Arial', 32),
                command=lambda row=r, col=c: on_click(row, col), fg="black"
            )
            buttons[r][c].grid(row=r, column=c, padx=5, pady=5)  # Add padding for better look

    reset_button = tk.Button(root, text="New Game", command=new_game, font=('Arial', 14))
    reset_button.pack(pady=10)

    credit_label = tk.Label(root, text="Created by Juldah", font=('Arial', 10), fg='gray')
    credit_label.pack(side='bottom', pady=5)

    root.mainloop()

def new_game():
    """
    Resets the board and variables to start a new game.
    """
    global player, board, buttons
    player = 'X'
    for r in range(3):
        for c in range(3):
            board[r][c] = ''
            buttons[r][c]['text'] = ''
            buttons[r][c]['fg'] = "black"
            buttons[r][c]['state'] = 'normal'

def on_click(row, col):
    """
    Handles button click events on the board.
    """
    global player
    if board[row][col] == '':
        board[row][col] = player
        buttons[row][col]['text'] = player
        buttons[row][col]['fg'] = "red" if player == 'X' else "blue"
        buttons[row][col]['state'] = 'disabled'
        if check_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            disable_all()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_all()
        else:
            if mode == '1P' and player == 'X':
                player = 'O'
                disable_empty_buttons()  # Disable player while AI "thinks"
                root.after(1000, ai_turn)  # AI moves after 1 second
            else:
                player = 'O' if player == 'X' else 'X'

def ai_turn():
    """
    Handles AI's move with smart decision making.
    """
    smart_ai_move(board, buttons)  # AI makes a move
    update_button_colors()
    if check_winner('O'):
        messagebox.showinfo("Game Over", "AI wins!")
        disable_all()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all()
    else:
        global player
        player = 'X'
        enable_empty_buttons()  # Enable player's move

def check_winner(p):
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

def is_draw():
    """
    Checks if the game is a draw (no empty cells left).
    """
    return all(board[r][c] != '' for r in range(3) for c in range(3))

def disable_all():
    """
    Disables all buttons on the board.
    """
    for r in range(3):
        for c in range(3):
            buttons[r][c]['state'] = 'disabled'

def disable_empty_buttons():
    """
    Disables only the empty (unplayed) buttons on the board.
    """
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                buttons[r][c]['state'] = 'disabled'

def enable_empty_buttons():
    """
    Enables only the empty (unplayed) buttons on the board.
    """
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                buttons[r][c]['state'] = 'normal'

def update_button_colors():
    """
    Updates the button text color (red for X, blue for O).
    """
    for r in range(3):
        for c in range(3):
            if buttons[r][c]['text'] == 'X':
                buttons[r][c]['fg'] = "red"
            elif buttons[r][c]['text'] == 'O':
                buttons[r][c]['fg'] = "blue"

if __name__ == '__main__':
    select_mode()
