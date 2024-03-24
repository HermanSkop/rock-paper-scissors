"""
This module contains the GUI for the game.
"""
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label

from build.services.bot_service import Bot
from build.services.game_service import Game

# Define the output path and assets path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Herman\Desktop\Markov\build\assets\frame0")

# Initialize the bot
bot = Bot()


def relative_to_assets(path: str) -> Path:
    """
    This function returns the absolute path of a file relative to the assets directory.

    :param path: The relative path of the file
    :return: The absolute path of the file
    """
    return ASSETS_PATH / Path(path)


def run_gui(game: Game):
    """
    This function runs the GUI for the game.

    :param game: The game instance
    """
    # Initialize the window
    window = Tk()
    window.geometry("382x715")
    window.configure(bg="#C6D3FF")

    # Initialize the canvas
    canvas = Canvas(
        window,
        bg="#C6D3FF",
        height=715,
        width=382,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Initialize the bot image and button
    bot_image = PhotoImage()
    bot_button = Button(
        image=bot_image,
        state="disabled",
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        relief="flat"
    )
    bot_button.place(
        x=8.0,
        y=0,
        width=366.0,
        height=366.0
    )

    # Initialize the scissors button
    scissors_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    scissors_button = Button(
        image=scissors_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("S"),
        relief="flat"
    )
    scissors_button.place(
        x=8.0,
        y=590.9999969005639,
        width=109.00000309943607,
        height=109.00000309943607
    )

    # Initialize the paper button
    paper_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    paper_button = Button(
        image=paper_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("P"),
        relief="flat"
    )
    paper_button.place(
        x=274.0,
        y=599.0,
        width=93.0,
        height=93.0
    )

    # Initialize the rock button
    rock_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    rock_button = Button(
        image=rock_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("R"),
        relief="flat"
    )
    rock_button.place(
        x=148.0,
        y=599.0,
        width=95.0,
        height=95.0
    )

    # Initialize the round label and counter
    round_label = Label(
        window,
        text="Round:",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    round_label.place(x=140, y=13.0)
    round_counter = Label(
        window,
        text="1",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    round_counter.place(x=212, y=13.0)

    # Initialize the robot label and counter
    robot_label = Label(
        window,
        text="Robots:",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    robot_label.place(x=10, y=13.0)
    robot_counter = Label(
        window,
        text="0",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    robot_counter.place(x=92, y=13.0)

    # Initialize the human label and counter
    human_label = Label(
        window,
        text="Humans:",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    human_label.place(x=250, y=13.0)
    human_counter = Label(
        window,
        text="0",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )
    human_counter.place(x=338, y=13.0)

    # Initialize the winner label
    winner_label = Label(
        window,
        text="Winner: ",
        bg="#C6D3FF",
        fg="#000000",
        font=("LuckiestGuy Regular", 16)
    )

    def reset_game():
        """
        This function resets the game.
        """
        game.reset()
        bot_image.configure(file=resolve_image(bot.get_move()))
        human_counter.configure(text=str(game.user_score))
        robot_counter.configure(text=str(game.bot_score))
        round_counter.configure(text=str(game.round))
        winner_label.configure(text="Winner: ")
        winner_label.place_forget()
        play_again.place_forget()

    # Initialize the play again button
    play_again = Button(
        borderwidth=2,
        highlightthickness=0,
        bg="#7AC7FF",
        activebackground="#51B6FF",
        command=reset_game,
        relief="flat",
        text="Play Again",
    )

    def end_application():
        """
        This function ends the application.
        """
        window.quit()
        window.destroy()
        sys.exit(0)

    def resolve_image(bot_move: str):
        """
        This function returns the image file path for the bot's move.

        :param bot_move: The bot's move
        :return: The image file path
        """
        return relative_to_assets(bot_move + ".png")

    def perform_move(user_move: str):
        """
        This function performs a move in the game.

        :param user_move: The user's move
        """
        bot_move = bot.get_move()
        bot_image.configure(file=resolve_image(bot_move))
        game.turn(user_move, bot_move)
        bot.update_transitions(user_move)

        human_counter.configure(text=str(game.user_score))
        robot_counter.configure(text=str(game.bot_score))
        round_counter.configure(text=str(game.round))

        if game.round == 30 or game.user_score == 10 or game.bot_score == 10:
            game_winner = "bot" if game.bot_score > game.user_score else "user"
            winner_label.configure(text="Winner: " + game_winner)
            winner_label.place(x=0, y=0, width=382, height=715)
            play_again.place(x=113, y=400, width=160, height=70)

    # Set the window close protocol and run the main loop
    window.protocol("WM_DELETE_WINDOW", end_application)
    window.resizable(False, False)
    window.mainloop()
