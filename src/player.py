# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def display_current_room(self):
        print(f"You are currently in the {self.current_room.name}")
        print(f"{self.current_room.description}")
    
                
    def welcome_player(self):
        print(f"Welcome {self.name}")


