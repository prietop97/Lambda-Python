from room import Room
from player import Player
from world import World
from util import Queue,Stack
from random import shuffle,choice

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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

# def bft(room):
#     q = Queue()
#     q.enqueue([room])
#     all_paths = []
#     visited = set()
#     while q.size() > 0:
#         path = q.dequeue()
#         current = path[-1]
#         visited.add(current)
        
#         all_paths.append(path)

#         for next_v in current.get_exits():
#             next_room = current.get_room_in_direction(next_v)
#             if next_room not in visited:
#                 new_path = path + [next_room]
#                 q.enqueue(new_path)
    
#     return all_paths
    # for i in range(1,len(path)):
    #     traversal_path.append(path[i][1])
    #     player.travel(path[i][1])


# rooms = {}
# def get_end_points():
#     my_hash = set()
#     q = Queue()
#     q.enqueue(player.current_room)
#     visited = set()
#     while q.size() > 0:
#         room = q.dequeue()
#         visited.add(room)
#         rooms[room.id] = room
#         if len(room.get_exits()) == 1:
#             my_hash.add(room)

#         for direction in room.get_exits():
#             next_room = room.get_room_in_direction(direction)
#             if next_room not in visited:
#                 q.enqueue(next_room)

#     return my_hash

# end_points = get_end_points()
# # print(rooms)

# cache = {}
# room274_paths = bft(rooms[274])
# for path in room274_paths:
#     print("****************")
#     for room in path:
#         print(room.id)


def dft(room):
    paths = []
    visited = set()
    s = Stack()
    s.push([room])

    while s.size() > 0:
        path = s.pop()
        current = path[-1]
        if current not in visited:      
            possible_paths = current.get_exits()
            visited.add(current)

            for direction in possible_paths:
                if current.get_room_in_direction(direction) not in visited:
                    paths.append(path)
                    new_path = path + [current.get_room_in_direction(direction)]
                    s.push(new_path)
    
    return paths

def bft(room):
    q = Queue()
    q.enqueue([room])
    all_paths = []
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        visited.add(current)
        
        all_paths.append(path)

        for next_v in current.get_exits():
            next_room = current.get_room_in_direction(next_v)
            if next_room not in visited:
                new_path = path + [next_room]
                q.enqueue(new_path)
    
    return all_paths

player.travel("e")
paths = dft(player.current_room)
print(world.room_grid)
def get_longest_play(goal,room,direction,actual_visited):

    s = Stack()
    best = [(room,None)]
    s.push([(room,None)])

    while s.size() > 0:
        path = s.pop()
        current_room = path[-1][0]
        
        possible_paths = current_room.get_exits()
    
        unvisited = set()
        if current_room == goal:
            return path

        visited.add(current_room)

        vertices_ = set()
        for vertices in path:
            vertices_.add(vertices[0])
        for direction in current_room.get_exits():
            next_room = current_room.get_room_in_direction(direction)
            if next_room not in vertices_ and next_room not in actual_visited:
                unvisited.add(next_room)
                new_path = path + [(next_room,direction)]
                s.push(new_path)

        if current_room not in actual_visited and current_room not in all_ignores:
            total_unvisited = 0
            for vertice in path:
                if vertice[0] not in actual_visited:
                    total_unvisited += 1
            if total_unvisited / len(path) > best_unvisited / len(best):
                print("HEY")
                best_unvisited = total_unvisited
                best = path



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

    

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

print(traversal_path)

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
