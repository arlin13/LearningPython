from Player import *


class FootballPlayer(Player):
    is_offense = None

    def __init__(self, name, last_name, is_offense):
        self.name = name
        self.last_name = last_name
        self.is_offense = is_offense

    def get_sport(self):
        return "Football"

    def is_offense(self):
        return self.is_offense

    def get_type_of_player(self):
        return "Type of player: " + ("Offense" if self.is_offense else "Defense")
