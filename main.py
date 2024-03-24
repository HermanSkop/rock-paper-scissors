from build import gui
from services.game_service import Game

if __name__ == "__main__":
    game = Game()
    gui.run_gui(game)
