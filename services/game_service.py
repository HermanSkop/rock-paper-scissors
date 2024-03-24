class Game:
    round = 0
    user_score = 0
    bot_score = 0

    def turn(self, user_move, bot_move):
        print('user: ', user_move)
        print('user: ', bot_move)
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
        if user_move == 'scissors':
            if bot_move == 'rock':
                return 'bot'
            elif bot_move == 'paper':
                return 'user'
            else:
                return 'draw'
        if user_move == 'paper':
            if bot_move == 'rock':
                return 'user'
            elif bot_move == 'paper':
                return 'draw'
            else:
                return 'bot'
        if user_move == 'rock':
            if bot_move == 'rock':
                return 'draw'
            elif bot_move == 'paper':
                return 'bot'
            else:
                return 'user'
