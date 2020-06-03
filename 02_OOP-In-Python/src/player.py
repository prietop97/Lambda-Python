# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
            print(self.current_room.get_items())
        else:
            print("You cannot move in that direction")

    def welcome_player(self):
        print(f"Welcome {self.name}")

    def get_item(self,item):
        for v in self.current_room.items:
            print(v.name,item)
            if v.name == item:
                self.items.append(v)
                self.current_room.items.remove(v)
            else:
                print("Can't find the item in this room")

    def drop_item(self,item):
        for v in self.items:
            if v.name == item:
                self.current_room.items.append(v)
                self.items.remove(v)
            else:
                print("Can't find the item in your inventory")


    def consume(self,food):
        if food in self.items:
            self.energy += food.calories
            print("Delicious")
        elif food in self.current_room.items:
            self.energy += food.calories
            print("Delicious")
        else:
            print("You can't eat that")

    def list_items(self):
        print("----------")
        print("|Your items|")
        print("----------")
        if len(self.items) == 0:
            print("Your bag is empty")
        else:
            for item in self.items:
                print(f'Name: {item.name}')






