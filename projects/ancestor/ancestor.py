from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # depth first traversal
    # build up graph
    # find longest path
    # if multiple long paths, return smaller num
    # else return -1

    # create a graph
    tree = Graph()

    # add ancestors to graph by iterating through ancestors
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        # if the parent or child has not been visited,
        if parent not in tree.vertices:
            # add starting vertex and add to visited
            tree.add_vertex(parent)
        if child not in tree.vertices:
            tree.add_vertex(child)
        # add the relationships, parent and child need to be flipped
        tree.add_edge(child, parent)
    print(tree.vertices)

    # generate paths with traversal
    longest_path = tree.bft(starting_node)
    oldest_ancestor = longest_path[-1]
    # if path is only 1 person long, no ancestors, return -1
    if longest_path[0] == oldest_ancestor:
        return -1

    return oldest_ancestor

# { 1:{10},  3:{1,2},  2:set(),  6:{3,5},  5:{4}, 
# 7:{5},  4:set(),  8:{11,4},  9:{8},  11:set(),  10:set() }

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)  # 10)
earliest_ancestor(test_ancestors, 2) # -1)

print()
