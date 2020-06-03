from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import sys

sys.setrecursionlimit(20000)
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


def bfs(room,visited):
    q = []
    q.append([room])
    newly_visited = set()
    while len(visited) != len(world.rooms):
        path = q.pop(0)
        print(path)
        if path[-1] not in newly_visited:
            newly_visited.add(path[-1])
            connections = room_graph[path[-1]][1]
            not_visited = {}
            for direction,room in connections.items():
                new_path = list(path)
                new_path.append(room)
                q.append(new_path)
                if room not in visited:
                    return path
            # if not_visited:
            #     if "w" in not_visited:
            #         return not_visited['w']
            #     elif "s" in not_visited:
            #         return not_visited['s']
            #     elif "e" in not_visited:
            #         return not_visited['e']
            #     elif "n" in not_visited:
            #         return not_visited['n']           
                
               


       
def walking(traversal_path):
    s = []
    visited = set()
    s.append(0)
    def dfs(room,visited):
        if len(visited) == len(world.rooms):
            return traversal_path
        visited.add(room)
        connections = room_graph[room][1]
        not_visited = {}

        for direction, room_id in connections.items():
            if room_id not in visited:
                not_visited[direction] = room_id
        
        if not not_visited:
            s.pop()
            new_room_list = bfs(room,visited)
            if not new_room_list:
                return traversal_path
            else:
                for i in range(1,len(new_room_list)):
                    connections2 = room_graph[new_room_list[i - 1]][1]
                    for direction, room_id in connections2.items():
                        if room_id == new_room_list[i]:
                            new_room_list[i - 1] = direction
                print(new_room_list)
                new_room = new_room_list.pop()
                print(new_room_list)
                traversal_path.extend(new_room_list)
                return dfs(new_room,visited)
        else:
            direction: None
            new_room = None
            
            if "w" in not_visited:
                direction = "w"
                new_room = not_visited["w"]
            elif "s" in not_visited:
                direction = "s"
                new_room = not_visited["s"]
            elif "n" in not_visited:
                direction = "n"
                new_room = not_visited["n"]
            elif "e" in not_visited:
                direction = "e"
                new_room = not_visited["e"]
            s.append(new_room)
            traversal_path.append(direction)
            return dfs(s[-1],visited)
            
           

    return dfs(s[-1],visited)


    #for i in range(count_back):

    #traversal_path.pop()


 




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
path = walking([])

traversal_path = path
print(traversal_path)
# TRAVERSAL TEST
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



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
