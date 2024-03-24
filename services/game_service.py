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
        if user_move == 'S':
            if bot_move == 'R':
                return 'bot'
            elif bot_move == 'P':
                return 'user'
            else:
                return 'draw'
        if user_move == 'P':
            if bot_move == 'R':
                return 'user'
            elif bot_move == 'P':
                return 'draw'
            else:
                return 'bot'
        if user_move == 'R':
            if bot_move == 'R':
                return 'draw'
            elif bot_move == 'P':
                return 'bot'
            else:
                return 'user'

    def reset(self):
        self.round = 0
        self.user_score = 0
        self.bot_score = 0
