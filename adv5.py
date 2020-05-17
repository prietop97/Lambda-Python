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

# end_points = utils.get_end_points(world.rooms[0]) #o(n+k)
# for end_point in end_points:
#     path = utils.get_mother_nodes(end_point)
#     last = path[-1][0]
#     if last.id not in pivot_rooms:
#         pivot_rooms[last.id] = []
#     pivot_rooms[last.id].append(path)


traversal_path = []
connected = {}
visited = set()


for room_id,room in world.rooms.items():
    connected[room_id] = []
    neighbors = utils.get_neighbors(room)
    if(len(neighbors)) > 1:
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

for connections in connected[1]:
    print(f"Length {len(connected[1])}")
    print('***********')
    for connection in connections:
        print(connection.id)


# connections = connected[0]

# for connection in connections:
#     print(len(connections))
#     print("****")
#     for room in connection:
#         print(room.id)

# while len(visited) < len(world.rooms):
#     current_room = player.current_room
#     connections = connected[current_room.id]
#     visited.add(current_room)
#     print(f'RESETTING?')
#     neighbors = utils.get_neighbors(current_room)
#     if connections:
#         connections.sort(key=len)
#         new_connections = connections[:]
#         for connection in new_connections:
#             first_room = connection[0]
#             if first_room not in visited:
#                 print("***************")
#                 print(f"BEFORE {player.current_room.id}")
#                 for room in connection:
#                     utils.bft(player,room,traversal_path,visited)
#                     print(f"DURING {player.current_room.id}")
#                 print(f"AFTER {player.current_room.id}")

#             #connections.remove(connection)

#     unvisited = {}
#     neighbors = utils.get_neighbors(player.current_room)
#     for neighbor in neighbors:
#         if neighbors[neighbor] not in visited:
#             unvisited[neighbor] = neighbors[neighbor]
#     print(len(visited))
#     if not unvisited:
#         utils.find_nearest_unvisited(visited,player,traversal_path)
#     else:
#         paths = sorted(unvisited.keys())
#         print(f"TRAVELING TO {unvisited[paths[-1]].id}")
#         player.travel(paths[-1])
#         traversal_path.append(paths[-1])
#         visited.add(unvisited[paths[-1]])





# print(traversal_path)
# player.current_room = world.rooms[0]
# for path in traversal_path:
#     print(room.id)
#     room = player.current_room
#     player.travel(path)




# for paths in connected[72]:
#     print("********************")
#     print(paths.id)
#     # for path in paths:
#     #     print(path.id)

# while len(visited) < len(world.rooms):
#     visited.add(player.current_room)
#     #utils.travel_dead_ends(player.current_room,pivot_rooms,visited,traversal_path,player)  
#     unvisited_bridges = []
#     room = player.current_room
#     neighbors = utils.get_neighbors(room)

#     for direction,next_room in neighbors.items():

#         if next_room not in visited:
#             unvisited_bridges.append(direction)

#     if not unvisited_bridges:
#         print("Happening")
#         utils.bft(player,traversal_path,visited)
    
#     connections = connected[player.current_room.id]
    
#     for connection in connections:
#         print(connection.id)
#         print(visited)
#         if connection not in visited:
#             for direction,next_room in neighbors.items():
#                 if next_room == connection:
#                     player.travel(direction)
#                     traversal_path.append(direction)
#                     utils.dft(player,traversal_path,visited,room,direction)

    
#     for direction,next_room in neighbors.items():
#         print(next_room)
#         if next_room not in visited:
#             player.travel(direction)
#             traversal_path.append(direction)
#             visited.add(next_room)
            




















# TRAVERSAL TEST - DO NOT MODIFY
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

    

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# #print(traversal_path)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     #print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
#     print(f"{len(traversal_path)} moves, {len(visited_rooms)} rooms visited")



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
