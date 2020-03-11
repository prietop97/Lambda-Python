from room import Room
from player import Player
from colors import Bcolors

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# player1 = Player(room['outside'])
directions = {"N": "n_to", "S": "s_to", "E": "e_to", "W": "w_to"}


def validate_if_node_exist(room, input_direction):
    return hasattr(room, directions[input_direction])


def change_player_position(player, input_direction):
    next_room = getattr(player.position, directions[input_direction])
    player.position = next_room
    return True


def print_colored_text(text, bcolor):
    return f"{bcolor} {text} {Bcolors.ENDC}"


def print_dots():
    return "..................................................."


user_name = input(print_colored_text("Hey! What is your name? :", Bcolors.OKBLUE))
player = Player(user_name, room["outside"])

print(print_dots())
print(print_colored_text(f"Welcome {player.name}", Bcolors.WARNING))

while True:
    print(
        print_colored_text(
            f"You are currently in the {player.position.name}", Bcolors.WARNING
        )
    )
    print(print_colored_text(f"{player.position.description}", Bcolors.WARNING))
    print(print_dots())
    next_step = input(
        print_colored_text(
            "Where would you like to go next? (N,S,E,W):", Bcolors.OKBLUE
        )
    )
    print(print_dots())
    if validate_if_node_exist(player.position, next_step):
        change_player_position(player, next_step)
    else:
        print(print_colored_text("Looks like a dead end, pay close attention to the clues!", Bcolors.FAIL))
        print(print_dots())


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
