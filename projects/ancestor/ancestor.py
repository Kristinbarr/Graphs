from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # BUILD THE GRAPH
    ancestor_graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if parent not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(parent)
        if child not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(child)
        ancestor_graph.add_edge(child, parent)


    # TRAVERSE GRAPH - DFT
    return ancestor_graph.dft_ancestors(starting_node)

