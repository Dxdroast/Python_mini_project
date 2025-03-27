import tkinter as tk
import random
import webview
import threading

def run_game():
    global window, label, mode_button, restart_button, board, curr_player, game_over, turns, single_player
    playerX, playerO = "X", "O"
    curr_player, single_player = playerX, False
    board = [[None] * 3 for _ in range(3)]
    color_blue, color_yellow, color_gray, color_light_gray = "#4584b6", "#ffde57", "#343434", "#646464"
    game_over, turns = False, 0

    # Tkinter Window Setup
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.resizable(False, False)
    frame = tk.Frame(window)
    label = tk.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_gray, foreground="white")
    label.grid(row=0, column=0, columnspan=3, sticky="we")

    def set_tile(row, column):
        global curr_player, game_over
        if game_over or board[row][column]["text"] != "":
            return
        board[row][column]["text"] = curr_player
        check_winner()
        if not game_over:
            switch_player()
            if single_player and curr_player == playerO:
                ai_move()

    def switch_player():
        global curr_player
        curr_player = playerX if curr_player == playerO else playerO
        label["text"] = curr_player + "'s turn"

    def ai_move():
        empty_tiles = [(r, c) for r in range(3) for c in range(3) if board[r][c]["text"] == ""]
        if empty_tiles:
            row, column = random.choice(empty_tiles)
            set_tile(row, column)

    def check_winner():
        global game_over, turns
        turns += 1
        for row in range(3):
            if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
                highlight_winner([(row, 0), (row, 1), (row, 2)])
                return
        for column in range(3):
            if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
                highlight_winner([(0, column), (1, column), (2, column)])
                return
        if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
            highlight_winner([(0, 0), (1, 1), (2, 2)])
            return
        if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
            highlight_winner([(0, 2), (1, 1), (2, 0)])
            return
        if turns == 9:
            label.config(text="Tie!", foreground=color_yellow)
            game_over = True

    def highlight_winner(positions):
        global game_over
        for row, col in positions:
            board[row][col].config(foreground=color_yellow, background=color_light_gray)
        label.config(text=board[positions[0][0]][positions[0][1]]["text"] + " is the winner!", foreground=color_yellow)
        game_over = True

    def new_game():
        global turns, game_over, curr_player
        turns = 0
        game_over = False
        curr_player = playerX
        label.config(text=curr_player + "'s turn", foreground="white")
        for row in range(3):
            for column in range(3):
                board[row][column].config(text="", foreground=color_blue, background=color_gray)
        if single_player and curr_player == playerO:
            ai_move()

    def toggle_mode():
        global single_player
        single_player = not single_player
        mode_button.config(text="Mode: " + ("Single Player" if single_player else "Two Player"))
        new_game()

    # Create Board
    for row in range(3):
        for column in range(3):
            board[row][column] = tk.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda r=row, c=column: set_tile(r, c))
            board[row][column].grid(row=row+1, column=column)

    mode_button = tk.Button(frame, text="Mode: Two Player", font=("Consolas", 15), background=color_gray, foreground="white", command=toggle_mode)
    mode_button.grid(row=4, column=0, columnspan=3, sticky="we")

    restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray, foreground="white", command=new_game)
    restart_button.grid(row=5, column=0, columnspan=3, sticky="we")

    frame.pack()
    window.update()
    window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{(window.winfo_screenwidth()//2)-(window.winfo_width()//2)}+{(window.winfo_screenheight()//2)-(window.winfo_height()//2)}")

    window.mainloop()

# Run the Tkinter game in a separate thread
def start_tkinter():
    threading.Thread(target=run_game, daemon=True).start()

# Webview setup with a button to launch the game
html_content = """
<html>
<head>
    <title>Tic-Tac-Toe</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        h1 {
            font-size: 36px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        button {
            font-size: 18px;
            padding: 12px 24px;
            background: #ffcc29;
            border: none;
            border-radius: 8px;
            color: black;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        button:hover {
            background: #ffb700;
            transform: scale(1.05);
        }
    </style>
    <script>
        function startGame() {
            window.pywebview.api.start_tkinter();
        }
    </script>
</head>
<body>
    <h1>Welcome to Tic-Tac-Toe</h1>
    <button onclick="startGame()">Start Game</button>
</body>
</html>
"""


# API for webview
class API:
    def start_tkinter(self):
        start_tkinter()

api = API()

# Launch the webview window
webview.create_window("Tic-Tac-Toe", html=html_content, js_api=api)
webview.start()
