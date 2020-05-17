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
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

end_points = None
# maze = world.room_grid
pivot_rooms = {}

end_points = utils.get_end_points(world.rooms[0]) #o(n+k)
for end_point in end_points:
    path = utils.get_mother_nodes(end_point)
    last = path[-1][0]
    if last.id not in pivot_rooms:
        pivot_rooms[last.id] = []
    pivot_rooms[last.id].append(path)


traversal_path = []
connected = {}
visited = set()


for room_id,room in world.rooms.items():
    connected[room_id] = []
    neighbors = utils.get_neighbors(room)
    for direction,next_room in neighbors.items():
        points = 0
        for direction2,next_room2 in neighbors.items():
            if next_room != next_room2:
                alone = utils.get_island_entrance(next_room,next_room2,room)
                if not alone:
                    points += 1
        if not points:
            island = utils.check_connected_islands(next_room,room)
            connected[room_id].append(island)

best = []
best_hash = {}
longest = utils.longest_path(player.current_room)
for long_ in longest:
    if len(long_) > len(best):
        best = long_
for i in range(0,len(best) - 1):
    best_hash[best[i][0]] = best[i + 1][1]


print(best)

while len(visited) < len(world.rooms):
    current = player.current_room
    visited.add(current)

    utils.go_through_connections(player,connected,visited,traversal_path,world)
    if current != player.current_room or utils.fully_visited(visited,world):
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
        utils.find_nearest_unvisited(visited,player,traversal_path,world)


        



print(traversal_path)
player.current_room = world.rooms[0]
for path in traversal_path:
    print(room.id)
    room = player.current_room
    player.travel(path)




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
