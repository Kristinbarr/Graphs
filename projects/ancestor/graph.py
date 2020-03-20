from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

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
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")


    def dft_ancestors(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        stack = Stack()
        # push the starting vertex
        stack.push([starting_vertex])
        # create a set to store visited vertices
        ancestor_path = [starting_vertex]
        # while the stack is not empty,
        while stack.size() > 0:
            # remove from top path on the stack
            path = stack.pop()
            # save first vertex(parent) of the path
            vertex = path[-1]
            # find the longest path to oldest ancestor
            if len(ancestor_path) < len(path):
                ancestor_path = path
            # if two paths are the same, spec wants smaller vertex
            if len(ancestor_path) == len(path) and ancestor_path[-1] > path[-1]:
                ancestor_path = path
            # find vertices/parents of the vertex(parent)
            for neighbor in self.get_neighbors(vertex):
                # need to copy the path bc pass by reference
                path_copy = path.copy()
                # add a neighbor/vertex/parent to the path
                path_copy.append(neighbor)
                # push the whole path permutation to the stack
                stack.push(path_copy)

        # if no ancestors, return -1
        if len(ancestor_path) == 1 and ancestor_path[0] == starting_vertex:
            return -1
        else:
            return ancestor_path[-1]


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
