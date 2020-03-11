# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def change_player_position(self,input_direction):
