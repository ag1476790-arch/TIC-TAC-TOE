import math

# Initialize board
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"

def print_board():
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---------")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if winner(AI):
        return 1
    if winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = AI
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = HUMAN
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = AI
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = AI

def human_move():
    move = int(input("Enter your move (0-8): "))
    if board[move] == " ":
        board[move] = HUMAN
    else:
        print("Invalid move!")
        human_move()

# Game loop
print("Welcome to Tic-Tac-Toe!")
print_board()

while True:
    human_move()
    print_board()

    if winner(HUMAN):
        print("You win! 🎉")
        break
    if is_draw():
        print("It's a draw 🤝")
        break

    ai_move()
    print("\nAI move:")
    print_board()

    if winner(AI):
        print("AI wins 🤖")
        break
    if is_draw():
        print("It's a draw 🤝")
        break
