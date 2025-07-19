import tkinter as tk
import main

def open_game(selected_mode):
    root.destroy()
    main.start_game(selected_mode)

root = tk.Tk()
root.title("TicTacToe - Options")

label = tk.Label(root, text="Select Game Mode:", font=("Arial", 14))
label.pack(pady=10)

btn_2p = tk.Button(root, text="2 Player", width=20, font=("Arial", 12),
                   command=lambda: open_game('2P'))
btn_2p.pack(pady=8)

btn_1p = tk.Button(root, text="1 Player (vs AI)", width=20, font=("Arial", 12),
                   command=lambda: open_game('1P'))
btn_1p.pack(pady=8)

credit_label = tk.Label(root, text="Created by Juldah", font=('Arial', 10), fg='gray')
credit_label.pack(side='bottom', pady=10)

root.mainloop()
