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


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
#world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
maze = world.room_grid
my_world = {}
connected = {}
end_points = None
pivot_rooms = {}
visited = set()

for i in range(len(maze)):
    for j in range(len(maze[i])):
        room = maze[i][j]
        if room:
            my_world[room.id] = room


end_points = utils.get_end_points(my_world[0])
for end_point in end_points:
    path = utils.get_mother_nodes(end_point)
    last = path[-1][0]
    if last.id not in pivot_rooms:
        pivot_rooms[last.id] = []
    pivot_rooms[last.id].append(path)

for room_id,room in my_world.items():
    neighbors = utils.get_neighbors(room)
    connected[room_id] = []
    for direction,next_room in neighbors.items():
        times_connected = 0
        for direction2,next_room2 in neighbors.items():
            if next_room != next_room2:
                alone = utils.get_island_entrance(next_room,next_room2,room)
                if not alone:
                    times_connected += 1
        if times_connected == 0:
            connected[room.id].append(next_room)

# for room_id,room in my_world.items():
#     for connection in connections[room_id]:









# for paths in connected[72]:
#     print("********************")
#     print(paths.id)
#     # for path in paths:
#     #     print(path.id)

while len(visited) < len(world.rooms):
    visited.add(player.current_room)
    utils.travel_dead_ends(player.current_room,pivot_rooms,visited,traversal_path,player)  
    unvisited_bridges = []
    room = player.current_room
    neighbors = utils.get_neighbors(room)

    for direction,next_room in neighbors.items():

        if next_room not in visited:
            unvisited_bridges.append(direction)

    if not unvisited_bridges:
        print("Happening")
        utils.bft(player,traversal_path,visited)
    
    connections = connected[player.current_room.id]
    
    for connection in connections:
        print(connection.id)
        print(visited)
        if connection not in visited:
            for direction,next_room in neighbors.items():
                if next_room == connection:
                    player.travel(direction)
                    traversal_path.append(direction)
                    utils.dft(player,traversal_path,visited,room,direction)

    
    for direction,next_room in neighbors.items():
        print(next_room)
        if next_room not in visited:
            player.travel(direction)
            traversal_path.append(direction)
            visited.add(next_room)
            

















# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

    

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

#print(traversal_path)

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
