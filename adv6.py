from room import Room
from player import Player
from world import World
from util import Queue,Stack
from random import shuffle,choice
import random
from ast import literal_eval


#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
world = World()
map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

world.print_rooms()
player = Player(world.starting_room)

traversal_path = []
connected = {}
visited = set()


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
            return False

        for direction,room in neighbors.items():
            if room not in visited:
                q.enqueue(room)
    
    return True

def reverse_direction(direction):
    if direction == "w":
        return "e"      
    if direction == "e":
        return "w"   
    if direction == "n":
        return "s"         
    if direction == "s":
        return "n"

def find_nearest_unvisited():
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

def check_hidden_islands(grid):
    cache = set()
    rooms = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            room = world.rooms[world.room_grid[i][j]]
            if room not in cache and room not in visited:
                visible = find_hidden_islands(room)
                if visible:
                    cache.add(room)
                else:
                    rooms.append(room)

    return rooms

    
def find_hidden_islands(room):
    s = Stack()
    s.push(room)
    _visited = set()
    while s.size() > 0:
        current = s.pop()
        _visited.add(current)

        if current == player.current_room:
            return False

        neighbors = get_neighbors(current)
        for direction,room in neighbors.items():
            if room not in visited and room not in _visited:
                s.push(room)

    return True



        
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
        for direction,next_room in neighbors.items():
            if next_room not in newly_visited:
                new_path = path + [(next_room,direction)]
                q.enqueue(new_path)
                newly_visited.add(next_room)

    for i in range(1,len(path)):
        player.travel(path[i][1])
        traversal_path.append(path[i][1])
        visited.add(path[i][0])



####################################### MAIN LOGIC ###########################
# check_hidden_islands()
best = []
best_hash = {}
longest = longest_path(player.current_room)
my_graph = world.room_grid[:][:]
pivot_rooms = {}
all_ignore = set()

end_points = get_end_points(world.rooms[0]) #o(n+k)
for end_point in end_points:
    path = get_mother_nodes(end_point)
    last = path[-1][0]
    if last.id not in pivot_rooms:
        pivot_rooms[last.id] = []
    pivot_rooms[last.id].append(path)
    for room in path[:-1]:
        all_ignore.add(room[0])

    

for i in range(len(world.room_grid)):
    for j in range(len(world.room_grid[i])):
        room = world.room_grid[i][j]
        if not room or room in visited:
            my_graph[i][j] = 0
        else:
            my_graph[i][j] = 1


for long_ in longest:
    if len(long_) > len(best):
        best = long_
for i in range(0,len(best) - 1):
    best_hash[best[i][0]] = best[i + 1][1]

for room_id,room in world.rooms.items():
    connected[room_id] = []
    neighbors = get_neighbors(room)
    for direction,next_room in neighbors.items():
        points = 0
        for direction2,next_room2 in neighbors.items():
            if next_room != next_room2:
                alone = get_island_entrance(next_room,next_room2,room)
                if not alone:
                    points += 1
        if not points and room not in all_ignore:
            island = check_connected_islands(next_room,room)
            connected[room_id].append(island)


print(f'{connected[449]} connections')
print(my_graph)
for connections in connected:
    for connection in connected[connections]:
        print("**********")
        print(connections)
        print("**********")
        for room in connection:
            print(room.id)

while len(visited) < len(world.rooms):
    current = player.current_room
    visited.add(current)

    hidden = check_hidden_islands(my_graph)
    for rooms in hidden:
        bft(rooms)
        continue


    


    go_through_connections(player,connected,visited,traversal_path,world)
    if current != player.current_room or len(visited) >= len(world.rooms):
        continue

    unvisited = []
    neighbors = player.current_room.get_exits()

    for neighbor in neighbors:
        room = player.current_room.get_room_in_direction(neighbor)
        if room not in visited:
            unvisited.append(neighbor)

    if player.current_room in best_hash:
        traversal_path.append(best_hash[player.current_room])
        player.travel(best_hash[player.current_room])
        visited.add(player.current_room)
        continue
    if unvisited:
        direction = unvisited.pop()
        player.travel(direction)
        traversal_path.append(direction)
        visited.add(player.current_room)
    else:
        find_nearest_unvisited()







####################################### TESTING ###########################

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    #print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(f"{len(traversal_path)} moves, {len(visited_rooms)} rooms visited")


