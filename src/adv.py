from room import Room
from player import Player
from item import Item
from myinput import Input


rooms = {
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

# items = {
#     "water": ,
#     "soda": ,
#     "gun": ,
#     "radio": ,

# }

# rooms["outside"].add_items("water", "soda")
# rooms["foyer"].add_items("gun", "radio")
# rooms["overlook"].add_items("sword", "soda")
# rooms["narrow"].add_items("water")
# rooms["treasure"].add_items("shovel", "rope")


# Link rooms together

rooms["outside"].n_to = rooms["foyer"]
rooms["foyer"].s_to = rooms["outside"]
rooms["foyer"].n_to = rooms["overlook"]
rooms["foyer"].e_to = rooms["narrow"]
rooms["overlook"].s_to = rooms["foyer"]
rooms["narrow"].w_to = rooms["foyer"]
rooms["narrow"].n_to = rooms["treasure"]
rooms["treasure"].s_to = rooms["narrow"]

# adventure_player = AdventureGame.create_player()
# AdventureGame(adventure_player)
def get_name():
    while True:
        name_input = Input("Hey, what's your name?","Please enter a valid name")
        player_name = name_input.run()
        is_valid_name = name_input.check_input(player_name)
        if not(is_valid_name):
            print(name_input.error)
            continue
        return player_name

def get_next_move():
    while True:
        move_input = Input("Hey, where would you like to go next (n,s,e,w?","Not a valid input, try again!",'n','s','w','e')
        next_move = move_input.run()
        is_valid_move = move_input.check_input(next_move)
        if not(is_valid_move):
            print(move_input.error)
            continue
        return next_move

def main():
    ## WELCOMING THE PLAYER
    name = get_name()
    player = Player(name,rooms['outside'])
    player.welcome_player()

    ## ASKING FOR THE NEXT MOVE
    while True:
        player.display_current_room()
        next_move = get_next_move()
        room = player.current_room.traverse_room(next_move)
        player.current_room = room


main()

