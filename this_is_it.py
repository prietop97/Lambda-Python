from room import Room
from player import Player
from world import World
from util import Queue,Stack
import random
from ast import literal_eval
from this_is_it_utils import get_neighbors,reverse_direction

world = World()
map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
world.print_rooms()
player = Player(world.starting_room)
visited = set()      
traversal_path = []
pivot_points = None



traversal_path = []


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


def get_end_points():
    my_hash = set()
    q = Queue()
    q.enqueue(player.current_room)
    visited = set()
    while q.size() > 0:
        room = q.dequeue()
        visited.add(room)

        if len(room.get_exits()) == 1:
            my_hash.add(room)

        for direction,next_room in get_neighbors(room).items():
            if next_room not in visited:
                q.enqueue(next_room)

    return my_hash

def get_mother_nodes(room,dead_end):
    
    visited = set()
    s = Stack()
    s.push([(room,None)])
    previous = None

    while s.size() > 0:
        path = s.pop()
        current = path[-1][0]
        visited.add(current)

        neighbors = get_neighbors(current)

        if len(neighbors) > 1:
            break

        for direction,next_room in neighbors.items():
            if next_room not in visited:
                new_path = path + [(next_room,direction)]
                s.push(new_path)

    last = path[-1]
    
    if last not in dead_end:
        dead_end[last] = []

    dead_end[last].append(path)

def populate_pivot_points():
    pivot_points = {}
    end_points = get_end_points()
    for end_point in end_points:
        get_mother_nodes(end_point,pivot_points)

    return pivot_points


def travel_dead_ends(room):
    if room in pivot_points:
        for paths in pivot_points[room]:
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



    





pivot_points = populate_pivot_points()
visited.add(player.current_room)

while len(visited) < len(world.rooms):
    print(traversal_path)
    visited.add(player.current_room)
    neighbors = get_neighbors(player.current_room)
    if player.current_room in pivot_points:
        for next_rooms in pivot_points[player.current_room]:
           
            if next_rooms[0] not in visited:  
                print(player.current_room)
                travel_dead_ends(next_rooms[0])
                print(traversal_path)
            break
             

    


print(traversal_path)



# TRAVERSAL TEST - DO NOT MODIFY
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
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



