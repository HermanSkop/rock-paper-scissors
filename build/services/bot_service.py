"""
This module contains the Bot class, which represents a bot that can play a game against a user.
"""
import json


class Bot:
    """
    This class represents a bot that can play a game against a user. The bot uses a strategy
    based on the user's previous move to decide its next move.
    """

    last_user_move = "P"  # The last move made by the user

    def get_move(self):
        """
        This method returns the bot's next move based on the user's last move.

        :return: The bot's next move ('P', 'S', or 'R')
        :raises Exception: If no last user move is recorded
        """
        if not self.last_user_move:
            raise ValueError("No last user move recorded")

        transitions = {key: value for key, value in retrieve_transitions().items()
                       if key[0] == self.last_user_move}
        likely_user_move = max(transitions, key=transitions.get)

        if likely_user_move[1] == "P":
            return "S"
        if likely_user_move[1] == "S":
            return "R"
        return "P"

    def update_transitions(self, user_move: str):
        """
        This method updates the transition probabilities based on the user's move.

        :param user_move: The move made by the user
        """
        if not self.last_user_move:
            return
        transitions = retrieve_transitions()
        for key in transitions:
            if key == (self.last_user_move + user_move):
                if round(transitions[key] + 0.04, 2) <= 1:
                    transitions[key] = round(transitions[key] + 0.04, 2)
                else:
                    transitions[key] = 1
            elif key[0] == self.last_user_move:
                if round(transitions[key] - 0.02, 2) >= 0:
                    transitions[key] = round(transitions[key] - 0.02, 2)
                else:
                    transitions[key] = 0

        with open("data/transitions.json", "w", encoding='utf-8') as file:
            json.dump(transitions, file)
        self.last_user_move = user_move


def retrieve_transitions():
    """
    This function retrieves the transition probabilities from a JSON file.

    :return: A dictionary of transition probabilities
    """
    return json.load(open("data/transitions.json", encoding='utf-8'))
