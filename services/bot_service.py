def move(user_move):
    if user_move == "rock":
        return "paper"
    elif user_move == "paper":
        return "scissors"
    elif user_move == "scissors":
        return "rock"
    else:
        raise ValueError("Invalid move")