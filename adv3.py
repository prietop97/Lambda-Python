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
all_ignores = set()
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



# def bft(player,traversal_path,visited):
#     q = Queue()
#     q.enqueue([(player.current_room,None)])
#     paths = {}
#     newly_visited = set()
#     while q.size() > 0:
#         path = q.dequeue()
#         current = path[-1][0]
        
#         if current not in newly_visited and current not in visited:
#             break
            

#         newly_visited.add(current)

#         for next_v in current.get_exits():
#             next_room = current.get_room_in_direction(next_v)
#             if next_room not in newly_visited:
#                 new_path = path + [(next_room,next_v)]
#                 q.enqueue(new_path)

#     #return paths
#     for i in range(1,len(path)):
#         traversal_path.append(path[i][1])
#         player.travel(path[i][1])
#         visited.add(path[i][0])

# # visited = set()
# # travel = bft(player,traversal_path,visited)
# # print(len(travel))
def travel_dead_ends(room,visited):
    if room in my_hash:
        for paths in my_hash[room]:
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

        my_hash.pop(room)

# def dft(traversal_path,player,world):

#     visited = set()
#     counter = 0

#     while len(visited) != len(world.rooms):
#         print(len(visited))
#         current = player.current_room
#         unvisited = []
#         possible_paths = current.get_exits()
#         visited.add(current)
#         travel_dead_ends(current,visited)

#         # for path in possible_paths:
#         #     room = current.get_room_in_direction(path)
#         #     if room not in visited and room in my_hash:
#         #         player.travel(path)
#         #         traversal_path.append(path)
#         #         visited.add(room)
#         #         travel_dead_ends(room,visited)
#         #         reverse = reverse_direction(path)
#         #         player.travel(reverse)
#         #         traversal_path.append(reverse)
                    


#         for path in possible_paths:
#             room = current.get_room_in_direction(path)
#             if room not in visited:
#                 unvisited.append(path)

#         unvisited.sort()

#         if unvisited:
#             random_room = unvisited[-1]
#             traversal_path.append(random_room)
#             player.travel(random_room)
#         else:
#             if len(visited) == len(world.rooms):
#                 break
#             bft(player,traversal_path,visited)


#     return traversal_path
    
# dft(traversal_path,player,world)

# for path in traversal_path:
#     print(path)

# def bft(player,traversal_path,visited):
#     q = Queue()
#     q.enqueue([(player.current_room,None)])
#     path = None
#     while q.size() > 0 and len(visited) != 18:
#         path = q.dequeue()
#         current = path[-1][0]
#         if current not in visited:
#             break
#         else:
#             for next_v in current.get_exits():
#                 new_path = path + [(current.get_room_in_direction(next_v),next_v)]
#                 q.enqueue(new_path)
#     if not path:
#         return
#     for i in range(1,len(path)):
#         traversal_path.append(path[i][1])
#         player.travel(path[i][1])





# def dft(traversal_path,player,world,visited):

#     current = player.current_room
#     travel_dead_ends(current,visited)
#     possible_paths = current.get_exits()

#     # for path in possible_paths:
#     #     room = current.get_room_in_direction(path)
#     #     if room not in visited and room in my_hash:
#     #         player.travel(path)
#     #         traversal_path.append(path)
#     #         travel_dead_ends(room,visited)
#     #         reverse = reverse_direction(path)
#     #         player.travel(reverse)
#     #         traversal_path.append(reverse)




#     return traversal_path
def bft(visited):
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


def get_longest_play(room,actual_visited):
    s = Stack()
    best = [(room,None)]
    s.push([(room,None)])
    visited = set()
    best_unvisited = 0
    while s.size() > 0:
        path = s.pop()
        current_room = path[-1][0]
        
        possible_paths = current_room.get_exits()
        unvisited = set()
        # if current_room.id == 123:
        #     if len(path) > len(best):
        #         best = path
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
    
       



    
    # actual_visited.add(player.current_room)
    return best

actual_visited = set()
#while len(actual_visited) < len(world.rooms):
while True:
    hey = get_longest_play(player.current_room,actual_visited)
    current_room = player.current_room
    #travel_dead_ends(current_room,actual_visited)
    print(f'{len(actual_visited)} Visited, {len(traversal_path)} Traveled')
    print()
    for i in range(1,len(hey)):
        #travel_dead_ends(player.current_room,actual_visited)
        player.travel(hey[i][1])
        traversal_path.append(hey[i][1])
        actual_visited.add(hey[i][0])
    break



print(traversal_path)

for h in hey:
    print(h[0].id)

# longest = 0
# optimal_path = []
# def get_longest_play(room,longest,optimal_path,visited=None,path=None):
#     if not path:
#         path = []

#     if not visited:
#         visited = set()

#     path = path[:]
#     path.append(room)

#     possible_paths = room.get_exits()
#     if len(possible_paths) == 1:
#         if len(path) > longest:
#             print("HEY")
#             optimal_path = path[:]
#             longest = len(path)

#     visited.add(room)

#     for direction in possible_paths:
#         next_room = room.get_room_in_direction(direction)
#         if next_room not in visited:
#             get_longest_play(next_room,longest,optimal_path,visited,path)



# longest = 0
# optimal_path = []


    # for next_v in self.get_neighbors(starting_vertex):
    #         if next_v not in visited:
    #             new_path = self.dfs_recursive(next_v,destination_vertex,path.copy(),visited)
    #             if new_path:
    #                 return new_path


    # while s.size() > 0:
    #     path = s.pop()
    #     current_room = path[-1][0]
        
    #     possible_paths = current_room.get_exits()

    #     if current_room not in actual_visited:
    #         if len(path) > len(best):
    #             best = path

    #     for direction in current_room.get_exits():
    #         next_room = current_room.get_room_in_direction(direction)
    #         able = True
            
    #         new_path = path + [(next_room,direction)]
    #         s.push(new_path)

# actual_visited = set()
# # dft(traversal_path,player,world,actual_visited)


# counter = 0
# while len(actual_visited) < len(world.rooms):
#     best = get_longest_play(player.current_room,world,actual_visited)
#     best.pop(0)
#     for path in best:
#         dft(traversal_path,player,world,actual_visited)
#         player.travel(path[1])
#         traversal_path.append(path[1])
#         actual_visited.add(path[0])

#     current = player.current_room
#     unvisited = set()

#     for direction in current.get_exits():
#         next_room = current.get_room_in_direction(direction)
#         if next_room not in actual_visited:
#             unvisited.add(next_room)

#     if not unvisited:
#         next_paths = bft(player,traversal_path,actual_visited)
#         best = []
#         best_length = 0
#         for target,path in next_paths.items():
#             room = path[-1][0]
#             longest =  get_longest_play(room,world,actual_visited)
#             if len(longest) > best_length:
#                 best = target
#                 best_length = len(longest)
#         print(next_paths[best])
        # for i in range(1,len(path)):
        #     traversal_path.append(path[i][1])
        #     player.travel(path[i][1])
        #     visited.add(path[i][0]) 
        
        #bft(player,traversal_path,actual_visited)
        
    


# actual_visited = set()
# counter = 0
# while len(actual_visited) != len(world.rooms):
#     counter += 1
#     best = dft(player,world,actual_visited)
#     current = best[-1][0]
#     check = bft(player,traversal_path,actual_visited)
#     if not check:
#         continue

#print(traversal_path)

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
