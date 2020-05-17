from util import Queue,Stack

def get_neighbors(room,exce=None):
    neighbors = {}
    exits = room.get_exits()
    for way in exits:
        next_room = room.get_room_in_direction(way)
        if next_room != exce:
            neighbors[way] = next_room

    return neighbors

def check_connected_islands(starting,exce,temp=None,visited=None):
    
    if not visited:
        visited = set()

    if not temp:
        temp = []

    temp.append(starting)
    visited.add(starting)
    neighbors = get_neighbors(starting,exce)

    for neighbor in neighbors:
        if neighbors[neighbor] not in visited:
            temp = check_connected_islands(neighbors[neighbor],exce,temp,visited)
    

    return temp

def get_island_entrance(starting,ending,exce):
    q = Queue()
    q.enqueue(starting)
    visited = set()
    while q.size() > 0:
        current = q.dequeue()
        visited.add(current)
        neighbors = get_neighbors(current,exce)

        if current == ending:
            return True

        for direction,room in neighbors.items():
            if room not in visited:
                q.enqueue(room)
    
    return False
        



    
def reverse_direction(direction):
    if direction == "w":
        return "e"      
    if direction == "e":
        return "w"   
    if direction == "n":
        return "s"         
    if direction == "s":
        return "n"

def get_end_points(room):
    my_hash = set()
    q = Queue()
    q.enqueue(room)
    visited = set()
    while q.size() > 0:
        room = q.dequeue()
        visited.add(room)

        if len(room.get_exits()) == 1:
            my_hash.add(room)

        for direction in room.get_exits():
            next_room = room.get_room_in_direction(direction)
            if next_room not in visited:
                q.enqueue(next_room)

    return my_hash


def get_mother_nodes(room):
    
    visited = set()
    s = Stack()
    s.push([(room,None)])

    while s.size() > 0:
        path = s.pop()
        current = path[-1][0]
        neighboors = current.get_exits()

        visited.add(current)

        for direction in neighboors:
            next_room = current.get_room_in_direction(direction)
            if next_room in visited:
                neighboors.remove(direction)

        if len(neighboors) > 1:
            return path


        for direction in neighboors:
            next_room = current.get_room_in_direction(direction)
            new_path = path + [(next_room,direction)]
            s.push(new_path)

def travel_dead_ends(room,my_hash,visited,traversal_path,player):
    if room.id in my_hash:
        for paths in my_hash[room.id]:
            if paths[0][0] not in visited:
                reverse = []
                normal = []
                for i in range(len(paths) - 1,-1,-1):
                    path = paths[i]
                    direction = path[1]
                    if direction:
                        reverse_path = reverse_direction(direction)
                        reverse.append(reverse_path)
                        normal.append(direction)
                    
                normal.reverse()
                for path in reverse:
                    player.travel(path)
                    traversal_path.append(path)
                    visited.add(player.current_room)

                for path in normal:
                    player.travel(path)
                    traversal_path.append(path)
                    visited.add(player.current_room)

        my_hash.pop(room.id)

def dft(player,traversal_path,visited,last_room,last_direction):
    
    s = Stack()
    s.push([(player.current_room,None)])

    while s.size() > 0:
        path = s.pop()
        room = path[-1][0]
        visited.add(room)
        neighbors = get_neighbors(room)
        if path[-1][1] and path[-1][0] == last_room:
            break

        for direction,next_room in neighbors.items():
            if next_room not in visited:
                new_path = path + [(next_room,direction)]
                s.push(new_path)
    

    path.pop(0) 
    for travel in path:
        player.travel(travel[1])
        traversal_path.append(travel[1])

 




def bft(player,traversal_path,visited):
    q = Queue()
    q.enqueue([(player.current_room,None)])
    currently_visited = set()
    while q.size() > 0:

        path = q.dequeue()
        current = path[-1][0]
        currently_visited.add(current)
  
        if current not in visited:
            break
        else:
            for next_v in current.get_exits():
                if current.get_room_in_direction(next_v) not in currently_visited:
                    new_path = path + [(current.get_room_in_direction(next_v),next_v)]
                    q.enqueue(new_path)
    
    if len(visited) == 500:
        return
    for i in range(1,len(path)):
        traversal_path.append(path[i][1])
        player.travel(path[i][1])
