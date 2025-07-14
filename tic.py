import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for a win
def check_winner():
    # Check rows and columns
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

# Check for tie
def check_tie():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

# Handle button click
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] == "":
        buttons[row][col]['text'] = current_player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create buttons
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

root.mainloop()