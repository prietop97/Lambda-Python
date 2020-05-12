"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)

        while q.size() > 0:

            current = q.dequeue()

            if current not in visited:
                visited.add(current)
                print(current)

            for next_v in self.get_neighbors(current):
                if next_v not in visited:
                    q.enqueue(next_v)




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:

            current = s.pop()

            if current not in visited:
                visited.add(current)
                print(current)
            
            for next_v in self.get_neighbors(current):
                if next_v not in visited:
                    s.push(next_v)

            

    def dft_recursive(self, starting_vertex, visited = None):
        if visited is None:
            visited = set()
        
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
        
        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                self.dft_recursive(next_v,visited)
                
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            current = path[-1]

            for next_v in self.get_neighbors(current):
                new_path = path.copy()
                new_path.append(next_v)
                if next_v == destination_vertex:
                    return new_path
                q.enqueue(new_path)

                
    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            current = path[-1]

            for next_v in self.get_neighbors(current):
                new_path = path.copy()
                new_path.append(next_v)
                if next_v == destination_vertex:
                    return new_path
                s.push(new_path)

    # pathh = None
    def dfs_recursive(self, starting_vertex, destination_vertex,path=None,visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
       
        if path is None:
            path = []
        
        if visited is None:
            visited = set()

        path.append(starting_vertex)
        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            print(path)
            return path

        new_path = None
        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                new_path = self.dfs_recursive(next_v,destination_vertex,path.copy(),visited)
            if next_v is destination_vertex:
                return self.dfs_recursive(next_v,destination_vertex,path.copy(),visited)
        
        return new_path

        
        
            
            

        
        

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
