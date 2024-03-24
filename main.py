"""This is the main file, it runs the game by creating a Game object and running the GUI with it."""
from build import gui
from build.services.game_service import Game

if __name__ == "__main__":
    game = Game()
    gui.run_gui(game)
