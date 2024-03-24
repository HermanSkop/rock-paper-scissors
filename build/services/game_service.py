"""
This module contains the Game class which represents a game with rounds and scores
for both the user and the bot.
"""


class Game:
    """
    This class represents a game with rounds and scores for both the user and the bot.
    """

    round = 0  # The current round number
    user_score = 0  # The user's current score
    bot_score = 0  # The bot's current score

    def turn(self, user_move, bot_move):
        """
        This method represents a turn in the game. It increments the round number,
        resolves the winner of the round, and updates the scores accordingly.

        :param user_move: The move made by the user
        :param bot_move: The move made by the bot
        :return: The winner of the round ('user', 'bot', or 'draw')
        """
        self.round += 1
        winner = self.resolve_winner(user_move, bot_move)
        if winner == 'bot':
            self.bot_score += 1
            self.user_score -= 1
        elif winner == 'user':
            self.user_score += 1
            self.bot_score -= 1
        return winner

    @staticmethod
    def resolve_winner(user_move: str, bot_move: str):
        """
        This static method determines the winner of a round based on
        the moves made by the user and the bot.

        :param user_move: The move made by the user
        :param bot_move: The move made by the bot
        :return: The winner of the round ('user', 'bot', or 'draw')
        """
        winner = 'draw'
        if user_move == 'S':
            if bot_move == 'R':
                winner = 'bot'
            if bot_move == 'P':
                winner = 'user'
        if user_move == 'P':
            if bot_move == 'R':
                winner = 'user'
            if bot_move == 'S':
                winner = 'bot'
        if user_move == 'R':
            if bot_move == 'P':
                winner = 'bot'
            if bot_move == 'S':
                winner = 'user'
        return winner

    def reset(self):
        """
        This method resets the game by setting the round number and scores back to zero.
        """
        self.round = 0
        self.user_score = 0
        self.bot_score = 0
