from util import Stack
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # depth first traversal
    # build up graph
    # find longest path
    # if multiple long paths, return smaller num
    # else return -1

    # create a graph
    tree = Graph()
    visited = []

    # iterate through the ancestors
    for pair in ancestors:
        # if the person has not been visited,
        if pair[0] not in visited:
            # add starting vertex and add to visited
            tree.add_vertex(pair[0])
            visited.append(pair[0]) 
    
        print(tree.vertices)
        # add the relationships
        tree.add_edge(pair[0], pair[1])


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)  # 10)
# earliest_ancestor(test_ancestors, 2) # -1)
# earliest_ancestor(test_ancestors, 3) # 10)
# earliest_ancestor(test_ancestors, 4) # -1)
# earliest_ancestor(test_ancestors, 5) # 4)
# earliest_ancestor(test_ancestors, 6) # 10)
# earliest_ancestor(test_ancestors, 7) # 4)
# earliest_ancestor(test_ancestors, 8) # 4)
# earliest_ancestor(test_ancestors, 9) # 4)
# earliest_ancestor(test_ancestors, 10) # -1)
# earliest_ancestor(test_ancestors, 11) # -1)

print()
