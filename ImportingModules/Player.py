class Player:
    name = None
    last_name = None

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_player_capitalized_name(self):
        return self.name.capitalize() + " " + self.last_name.capitalize()

    def get_sport(self):
        raise NotImplementedError

