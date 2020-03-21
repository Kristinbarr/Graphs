"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
# EXAMPLE (undirected)
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
# EXAMPLE (directed)
# {
#     '0': {'1', '3'},
#     '1': set(),
#     '2': set(),
#     '3': set()
# }

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add another row
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if that v1 or v2 is in self.vertices,
        if v1 in self.vertices and v2 in self.vertices:
            # add v1 key and v2 as the value in the set
            self.vertices[v1].add(v2)
        else:
            # print("ERROR: vertex does not exist")
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            # print("ERROR: vertex does not exist")
            raise ValueError("vertex does not exist")


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        q = Queue()
        # enqueue the starting vertex
        q.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty,
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # check if it's been visited
            # if it hasn't been visited,
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty,
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # check if it's been visited
            # if it hasn't been visited,
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # exception for python keeps reference to visited value
        if visited is None:
            visited = set()
        # Check if the node has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH (order matters for a path)
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH bc pass by ref issue
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH (order matters for a path)
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # PUSH A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH bc pass by ref issue
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # PUSH THE COPY
                    s.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # add arguments for things to traverse function instances

        # check if visited and path are None for python exception
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # check if vertex has been visited
        if starting_vertex not in visited:
            # add the vertex to visited
            visited.add(starting_vertex)
            # make a copy of the path
            path_copy = path.copy()
            # add vertex to copy path
            path_copy.append(starting_vertex)

            # 
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None


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
