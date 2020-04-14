"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # This is our adjacency list
        # example:
        # {
        #     "A": {"B": 1},
        #     "B": {"C": 3, "D": 2},
        #     "C": {},
        #     "D": {},
        #     "E": {"D": 1}
        # }
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # check if v1 and v2 are valid/exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        # else print error
        else:
            print('ERROR ADDING EDGE: vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # TODO: maybe return an exception instead

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue starting vertex
        q = Queue()
        q.enqueue([starting_vertex])

        # create a set of traversed vertices
        visited = set()
        
        # while queue is not empty
        while q.size() > 0:
            # dequeue/pop the first vertex
            path = q.dequeue()
            # if not visited,
            if path[-1] not in visited:
                print(path[-1])
                # add it to visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # make a copy bc pass by reference
                    new_path = list(path)
                    # add next_vert to new path and enqueue the new path
                    new_path.append(next_vert)
                    q.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack and add starting vertex
        s = Stack()
        s.push([starting_vertex])

        # create a set of traversed vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # dequeue/pop the first vertex
            path = s.pop()
            # if not visited,
            if path[-1] not in visited:
                print(path[-1])
                # add it to visited
                visited.add(path[-1])
                # add all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # make a copy bc pass by reference
                    new_path = list(path)
                    # add next_vert to new path and enqueue the new path
                    new_path.append(next_vert)
                    s.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()
        # basecase: when we have no more neighbors

        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # call the function recursively - on neighbors not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)



        # # create a stack and add starting vertex
        # s = Stack()
        # s.push([starting_vertex])

        # # base case is if the stack size is 0
        # # or starting vertices has already been visited?
        # if s.size() <= 0:
        #     return None

        # # create a set of traversed vertices
        # visited = set()

        # # get path from from stack
        # path = s.pop()

        # # iterate get neighbors?
        # if path[-1] not in visited:
        #     print(path[-1])
        #     # recurse with next vertex
        #     self.dft_recursive(path[-1])

        # # once finshed, print path
        # print(path)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue and enqueue starting vertex
        q = Queue()
        q.enqueue([starting_vertex])

        # create a set of traversed vertices
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue/pop the first vertex
            path = q.dequeue()
            # if not visited,
            if path[-1] not in visited:
                # DO THE THING
                if path[-1] == destination_vertex:
                    return path
                # add it to visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # make a copy bc pass by reference
                    new_path = list(path)
                    # add next_vert to new path and enqueue the new path
                    new_path.append(next_vert)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack and add starting vertex
        s = Stack()
        s.push([starting_vertex])

        # create a set of traversed vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # dequeue/pop the first vertex
            path = s.pop()
            # if not visited,
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                # add it to visited
                visited.add(path[-1])
                # add all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # make a copy bc pass by reference
                    new_path = list(path)
                    # add next_vert to new path and enqueue the new path
                    new_path.append(next_vert)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
