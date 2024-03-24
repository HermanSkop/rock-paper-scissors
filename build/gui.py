# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import sys
import services.bot_service as bot
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Variable, Label
from services.game_service import Game

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Herman\Desktop\Markov\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def run_gui(game: Game):
    window = Tk()
    window.geometry("382x715")
    window.configure(bg="#C6D3FF")

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

    scissors_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    scissors_button = Button(
        image=scissors_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("scissors"),
        relief="flat"
    )
    scissors_button.place(
        x=8.0,
        y=590.9999969005639,
        width=109.00000309943607,
        height=109.00000309943607
    )

    paper_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    paper_button = Button(
        image=paper_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("paper"),
        relief="flat"
    )
    paper_button.place(
        x=274.0,
        y=599.0,
        width=93.0,
        height=93.0
    )

    rock_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    rock_button = Button(
        image=rock_image,
        borderwidth=0,
        highlightthickness=0,
        bg="#C6D3FF",
        activebackground="#C6D3FF",
        command=lambda: perform_move("rock"),
        relief="flat"
    )
    rock_button.place(
        x=148.0,
        y=599.0,
        width=95.0,
        height=95.0
    )
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

    def end_application():
        window.quit()
        window.destroy()
        sys.exit(0)

    def resolve_image(bot_move: str):
        return relative_to_assets(bot_move + "_bot.png")

    def perform_move(user_move: str):
        bot_move = bot.move(user_move)
        bot_image.configure(file=resolve_image(bot_move))
        winner = game.turn(user_move, bot_move)

        human_counter.configure(text=str(game.user_score))
        robot_counter.configure(text=str(game.bot_score))
        round_counter.configure(text=str(game.round))

        print(winner)

    window.protocol("WM_DELETE_WINDOW", end_application)
    window.resizable(False, False)
    window.mainloop()
