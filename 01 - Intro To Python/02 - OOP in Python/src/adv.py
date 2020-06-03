from room import Room
from player import Player
from item import Food
from myinput import Input
import os


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


rooms["outside"].add_items(Food("Watermelon", "It's a watermelon", 20),Food("Rice","It's rice",15),Food("Steak","It's a welldone steak",40))
rooms["foyer"].add_items(Food("Watermelon", "It's a watermelon", 20),Food("Rice","It's rice",15),Food("Steak","It's a welldone steak",40))
rooms["overlook"].add_items(Food("Watermelon", "It's a watermelon", 20),Food("Rice","It's rice",15),Food("Steak","It's a welldone steak",40))
rooms["narrow"].add_items(Food("Watermelon", "It's a watermelon", 20),Food("Rice","It's rice",15),Food("Steak","It's a welldone steak",40))
rooms["treasure"].add_items(Food("Watermelon", "It's a watermelon", 20),Food("Rice","It's rice",15),Food("Steak","It's a welldone steak",40))


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
        name_input = Input("Hey, what is your name","Not a valid input")
        player_name = name_input.run()
        is_valid_name = name_input.check_input(player_name)
        if not(is_valid_name):
            print(name_input.error)
            continue
        return player_name

def get_next_move():
    while True:
        print("Press i to go to the inventory")
        move_input = Input("Hey, where would you like to go next?","Not a valid input, try again!",'n','s','w','e','i','q')
        next_move = move_input.run()
        is_valid_move = move_input.check_input(next_move)
        if not(is_valid_move):
            print(move_input.error)
            continue
        return next_move

def inventory_menu(player1):
    while True:
        player1.list_items()
        player1.current_room.list_items()
        print("Press m to go back")
        move_input = Input("Press m to go back or drop [item] | get [item]","Not a valid input, try again!")
        next_move = move_input.run()
        if next_move is "m":
            break
        else:
            action,item = next_move.split()
            if action not in ("get","drop"):
                print("Wront action")
            elif action == "get":
                player1.get_item(item)
            else:
                player1.drop_item(item)
        os.system('clear')


def main():
    ## WELCOMING THE PLAYER
    name = get_name()
    player = Player(name,rooms['outside'])
    player.welcome_player()
    os.system('clear')
    print(player.current_room)

    ## ASKING FOR THE NEXT MOVE
    while True:
        next_move = get_next_move()
        if next_move == 'i':
            inventory_menu(player)
        player.travel(next_move)
    




main()

