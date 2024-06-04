
# Python's built-in GUI (Graphical User Interface) library.
import tkinter as tk
from tkinter import messagebox

def winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [1,4,7] , [0,3,6] ,[ 2,5,8]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("TIC-TAC-TOE", f"Player {buttons[combo[0]]['text']} wins!")
            return True
    return False

def buttons_click(index):
    if buttons[index]["text"] == "" and not winner():
        buttons[index]["text"] = current_player
        if winner():
            return
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("TIC-TAC-TOE")

buttons = [tk.Button(root, text="", font=("normal",25), width=6, height=2, command=lambda i=i: buttons_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()


# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Explaination:
# Importing Libraries:
# import tkinter as tk: Imports the tkinter module and gives it an alias tk for easier reference.
# from tkinter import messagebox: Imports the messagebox submodule from tkinter, which is used to display various types of message boxes.

# Function Definitions:
# winner(): This function checks for winning combinations on the tic-tac-toe board. It iterates through all possible winning combinations and checks if the buttons at those positions have the same non-empty text (either 'X' or 'O'). If a winning combination is found, it changes the background color of the winning buttons to green, displays a message box indicating the winner, and returns True. Otherwise, it returns False.
# buttons_click(index): This function is called when a button on the tic-tac-toe board is clicked. It takes the index of the clicked button as input. If the clicked button is empty and there is no winner yet, it updates the text of the clicked button with the current player's symbol ('X' or 'O'). Then, it checks if the current move results in a win. If so, it stops the game. Otherwise, it toggles the player.
# toggle_player(): This function toggles the current player between 'X' and 'O'. It updates the label text to indicate whose turn it is next.

# Initializing the Tkinter Window:
# root = tk.Tk(): Creates the main application window.
# root.title("TIC-TAC-TOE"): Sets the title of the window to "TIC-TAC-TOE".

# Creating Buttons:
# Creates a list of 9 buttons using list comprehension, representing the tic-tac-toe grid. Each button is initialized with empty text, a specific font, width, height, and a command to call buttons_click() with the corresponding button index when clicked.

# Displaying Buttons:
# Uses a for loop to iterate over the buttons list and places each button in a grid layout on the tkinter window.

# Initializing Game Variables:
# current_player = "X": Initializes the current player to 'X'.
# Creates a label indicating whose turn it is initially and places it at the bottom of the grid.

# Starting the Tkinter Event Loop:
# root.mainloop(): Starts the event loop, allowing the window to handle user inputs and events.
