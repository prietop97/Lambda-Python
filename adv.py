from room import Room
from player import Player
from world import World
from util import Queue,Stack

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
def bft(player,visited):
    q = Queue()
    q.enqueue([(player.current_room,None)])

    while q.size() > 0:
        path = q.dequeue()
        current = path[-1][0]
        if current not in visited:
            break
        else:
            for next_v in current.get_exits():
                new_path = path + [(current.get_room_in_direction(next_v),next_v)]
                q.enqueue(new_path)
    
    for i in range(1,len(path)):
        traversal_path.append(path[i][1])
        player.travel(path[i][1])

    


    



def dft(traversal_path,player,world):

    visited = set()

    while len(visited) != len(world.rooms):
        current = player.current_room

        unvisited = []
        possible_paths = current.get_exits()
        visited.add(current)

        for path in possible_paths:
            if current.get_room_in_direction(path) not in visited:
                unvisited.append(path)
        unvisited.sort()

        if unvisited:
            traversal_path.append(unvisited[-1])
            next_v = unvisited.pop()
            player.travel(next_v)
        else:
            if len(visited) == len(world.rooms):
                return
            bft(player,visited)

dft(traversal_path,player,world)
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
