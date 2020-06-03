# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += f"{self.get_exits_string()}"
        return return_string

    def list_items(self):
        print("------------")
        print("|Room items|")
        print("------------")
        if len(self.items) == 0:
            print("The room is empty")
        else:
            for item in self.items:
                print(f'Name: {item.name}')

    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    # def remove_item(self,item):
    #     self.items.remove(item)

    def add_items(self,*args):
        self.items.extend(args)

    

