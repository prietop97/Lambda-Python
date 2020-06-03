from util import Queue,Stack
from collections import deque
from random import shuffle

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

def check_hidden_islands(starting,exce,actual_visited,temp=None,visited=None):
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

    # friend = temp[-1]
    # for neighbor in neighbors:
    #     if neighbor != friend and neighbor in temp:
    #         temp.clear()

    return temp

# def check_connected_islands(starting,exce):
#     visited = set()
#     s = Stack()
#     s.push([starting])
#     best = []

#     while s.size() > 0:
#         path = s.pop()
#         current = path[-1]
#         neighbors = get_neighbors(current,exce)
#         visited.add(current)
#         print("RUNNING")

#         if len(path) > len(best):
#             best = path
#         for neighbor in neighbors:
#             if neighbors[neighbor] not in visited:
#                 new_path = path + [neighbors[neighbor]]
                
#                 s.push(new_path)

    # friend = temp[-1]
    # for neighbor in neighbors:
    #     if neighbor != friend and neighbor in temp:
    #         temp.clear()

    return best

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

def find_nearest_unvisited(visited,player,traversal_path,world):
    q = Queue()
    room = player.current_room
    q.enqueue([(room,None)])
    new_visited = set()
    new_visited.add(room)
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1][0]
        
        if current not in visited:
            break
        
        neighboors = get_neighbors(current)

        for direction,next_room in neighboors.items():
            if next_room not in new_visited:
                new_path = path + [(next_room,direction)]
                q.enqueue(new_path)
                new_visited.add(next_room)
    enum = len(path)
    if len(visited) + len(path) - 1 >= len(world.rooms):
        enum = len(world.rooms) - len(visited)
    for i in range(1,len(path)):
        player.travel(path[i][1])
        traversal_path.append(path[i][1])
        visited.add(path[i][0])


def bft(destination):
    q = Queue()
    q.enqueue([(player.current_room,None)])
    newly_visited = set()
    newly_visited.add(player.current_room)
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1][0]
        if current == destination:
            break
        neighbors = get_neighbors(current)
        neighbors = list(neighbors).sort(reverse=True)
        for direction,next_room in neighbors:
            if next_room not in newly_visited:
                new_path = path + [(next_room,direction)]
                q.enqueue(new_path)
                newly_visited.add(next_room)

    for i in range(1,len(path)):
        player.travel(path[i][1])
        traversal_path.append(path[i][1])
        visited.add(path[i][0])
# def dfs(player,room,destination,traversal_path,visited):
    

def longest_path(v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [(v,None)]

    seen.append(v)
    paths = []
    neighbors = get_neighbors(v)
    for t in neighbors:
        if neighbors[t] not in seen:
            t_path = path + [(neighbors[t],t)]
            paths.append(tuple(t_path))
            paths.extend(longest_path(neighbors[t], seen[:], t_path))
    return paths

def go_through_connections(player,connected,visited,traversal_path,world):
    current_room = player.current_room
    connections = connected[player.current_room.id]
    connections.sort(reverse=True,key=len)

    if not connections or not connections[0]:
        return

    connection = connections[0]
    next_room = connection[0]

    if next_room not in visited:
        direction = current_room.get_direction_by_room(next_room)
        player.travel(direction)
        traversal_path.append(direction)
        visited.add(player.current_room)
        
def fully_visited(visited,world):
    if len(visited) >= len(world.rooms):
        return True
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
            exits = current.get_exits()
            exits.sort(reverse=True)
            for next_v in exits:
                if current.get_room_in_direction(next_v) not in currently_visited:
                    new_path = path + [(current.get_room_in_direction(next_v),next_v)]
                    q.enqueue(new_path)
    
    if len(visited) == 500:
        return
    for i in range(1,len(path)):
        traversal_path.append(path[i][1])
        player.travel(path[i][1])


