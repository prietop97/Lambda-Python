def get_neighbors(room,exce=None):
    neighbors = {}
    exits = room.get_exits()
    for way in exits:
        next_room = room.get_room_in_direction(way)
        if next_room != exce:
            neighbors[way] = next_room

    return neighbors

def reverse_direction(direction):
    if direction == "w":
        return "e"      
    if direction == "e":
        return "w"   
    if direction == "n":
        return "s"         
    if direction == "s":
        return "n"