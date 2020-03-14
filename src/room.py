# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None 


    def __repr__(self):
        return f"Room (name: {self.name},description: {self.description})"


    def traverse_room(self, direction):
        new_room = getattr(self, f'{direction}_to')
        if new_room is None:
            print("Hmm, nothing there, play close attention to your environment")
            return self
        else:
            return new_room

    


