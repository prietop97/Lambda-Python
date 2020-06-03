
from util import Stack, Queue

g = {}
def get_neighbors(vertex_id,ancestors):
    """
    Get all neighbors (edges) of a vertex.
    """
    if vertex_id in g:
        return g[vertex_id]

    g[vertex_id] = set()
    for ancestor in ancestors:
        if ancestor[1] == vertex_id:
            g[ancestor[1]].add(ancestor[0])
    
    return g[vertex_id]
    

def earliest_ancestor(ancestors, starting_node):
    best_path = (-1,0)
   
    visited = set()
    s = Stack()
    s.push([starting_node])

    while s.size() > 0:
        path = s.pop()
        current = path[-1]
        visited.add(current)

        if not get_neighbors(current,ancestors):
            if (best_path[0] == -1 or best_path[1] < len(path)) and current != starting_node:
                best_path = (path[-1],len(path))
            elif best_path[1] == len(path):
                if best_path[0] > path[-1]:
                    best_path = (path[-1],len(path))
        else:
            for next_v in get_neighbors(current,ancestors):
                if current is starting_node:
                    s.push([next_v])
                else:
                    s.push(path + [next_v])

    return best_path[0]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors,1)






