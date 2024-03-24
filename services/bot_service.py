import json


class Bot:
    last_user_move = "P"

    def get_move(self):
        if not self.last_user_move:
            raise Exception("No last user move recorded")

        transitions = {key: value for key, value in retrieve_transitions().items() if key[0] == self.last_user_move}
        likely_user_move = max(transitions, key=transitions.get)

        if likely_user_move[1] == "P":
            return "S"
        elif likely_user_move[1] == "S":
            return "R"
        else:
            return "P"

    def update_transitions(self, user_move: str):
        print('last_user_move: ', self.last_user_move)

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

        with open("data/transitions.json", "w") as file:
            json.dump(transitions, file)
        self.last_user_move = user_move


def retrieve_transitions():
    return json.load(open("data/transitions.json"))
