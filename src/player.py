# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @name.setter
    def name(self,name):
        if len(name) < 1:
            raise Exception("Provide a valid name")
        self._name = name

    @position.setter
    def position(self,position):
        self._position = position

    
    
