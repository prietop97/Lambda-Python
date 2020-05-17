from room import Room
from player import Player
from world import World
from util import Queue,Stack
from random import shuffle,choice
import utils

import random
from ast import literal_eval

# Load world
world = World()


map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def reverse_direction(direction):
    if direction == "w":
        return "e"      
    if direction == "e":
        return "w"   
    if direction == "n":
        return "s"         
    if direction == "s":
        return "n"

def get_end_points(player,world):
    my_hash = set()
    q = Queue()
    q.enqueue(player.current_room)
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

my_hash = {}
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


dead_end = get_end_points(player,world)
for room in dead_end:
    path = get_mother_nodes(room)
    last = path[-1][0]
    if last in my_hash:
        my_hash[last].append(path)
    else:
        my_hash[last] = []
        my_hash[last].append(path)




def travel_dead_ends(room,visited):
    if room in my_hash:
        for paths in my_hash[room]:
            print("HWE")
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

                if len(visited) == len(world.rooms):
                    return

                for path in normal:
                    player.travel(path)
                    traversal_path.append(path)
                    visited.add(player.current_room)

                

        my_hash.pop(room)

# def hey():
#     total = 0
#     check1 = utils.get_island_entrance(world.rooms[1],world.rooms[3],world.rooms[0])
#     check2 = utils.get_island_entrance(world.rooms[1],world.rooms[8],world.rooms[0])
#     check3 = utils.get_island_entrance(world.rooms[1],world.rooms[4],world.rooms[0])

#     if check1:
#         total += 1
#     if check2:
#         total += 1
#     if check3:
#         total += 1

#     if total == 0:
#         print("PASSING")
#         return "PASSING"
#     else:
#         print("NOT PASSING")
#         return None

# total_in_check = 0
# times_ran = 0
# for i in range(100):
#     times_ran += 1
#     solution = hey()

#     if solution:
#         total_in_check += 1

# print(f"{total_in_check} passed out of {times_ran} times")

visited = set()
cache = {}
while len(visited) != len(world.rooms):
    current = player.current_room
    unvisited = []
    visited.add(current)
    travel_dead_ends(current,visited)
    possible_paths = utils.get_neighbors(player.current_room)
    end_loops = []  
    others = []      

    for direction,room in possible_paths.items():
        if room not in visited:
            unvisited.append((room,direction))

    if unvisited:
        for room,direction in unvisited:
            total = 0
            possible_paths = utils.get_neighbors(player.current_room)
            if possible_paths and len(possible_paths) > 1:
                for direction2,room2 in possible_paths.items():
                    if room != room2: 
                        check = utils.get_island_entrance(room,room2,player.current_room)
                        if check:
                            total += 1
                            others.append((room,direction))
                            continue
                if total == 0:
                    end_loops.append((room,direction))
        
        if end_loops:
            player.travel(end_loops[0][1])
            traversal_path.append(end_loops[0][1])
            visited.add(end_loops[0][0])
        elif others:
            player.travel(others[0][1])
            traversal_path.append(others[0][1])
            visited.add(others[0][0])
    else:
        utils.bft(player,traversal_path,visited)

    #     print(traversal_path)

                
    # print(player.current_room.id)
    # print(end_loops)





        

 








        
    



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

    

print(player.current_room.id)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print(player.current_room.id)

# print(traversal_path)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    #print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(f"{len(traversal_path)} moves, {len(visited_rooms)} rooms visited")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
