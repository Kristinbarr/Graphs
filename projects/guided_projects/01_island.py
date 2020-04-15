'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
'''

# islands consist of: connected components
# connected: neightbors (edges)
# directions: NSEW (edges)
# 2d array: graph, more or less
# returns (shape of solution): number of islands

# How could we write a get neighbor function that uses this shape?
# offset coordinates

# How can we find the extent of an island?
# Either of travels to find all of the nodes in an island

# How do we explore the larger set?
# Loop through and call traversal if we find a unvisited 1


def island_counter(islands):
    # get shape
    limit = len(islands)
    visited = [ [False] * limit ] * limit
    island_counter = 0
    # iterate through islands
    for i in range(limit):
        for j in range(limit):
            # search for a univisited 1
            if not visited[i][j] and islands[i][j] == 1:
                # get 1 neighbors
                get_neighbors() # TODO
                island_counter += 1
            else:
                visited[i][j] = True

    return island_counter
    # add to visited
    # if no more neighbors, go back


def get_neighbors(x, y, limit, visited, islands):
    # get shape of area

    # look north
    if x != 0 and islands[x-1][y] == 1:
    # look south
    # look east
    # look west