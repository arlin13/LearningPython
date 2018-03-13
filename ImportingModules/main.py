from BasketballPlayer import *
from SoccerPlayer import *
from FootballPlayer import *


class Main:

    arlin = BasketballPlayer("arlin", "grijalba")
    print(arlin.get_player_capitalized_name())
    print(arlin.get_sport())

    print()

    mario = SoccerPlayer("mario", "gomez")
    print(mario.get_player_capitalized_name())
    print(mario.get_sport())

    print()

    waldo = FootballPlayer("waldo", "chavez", True)
    print(waldo.get_player_capitalized_name())
    print(waldo.get_sport())
    print(waldo.is_offense)
    print(waldo.get_type_of_player())

    print()

    joshua = FootballPlayer("joshua", "smith", False)
    print(joshua.get_player_capitalized_name())
    print(joshua.get_sport())
    print(joshua.is_offense)
    # print("Type of player: " + ("Offense" if joshua.is_offense else "Defense"))
    print(joshua.get_type_of_player())
