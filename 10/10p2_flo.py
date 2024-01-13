import networkx as nx
import numpy as np
from scipy.ndimage import label

# Create the coordinate settings for the connectors
connectors = {
    "|" : [(-1, 0), (1, 0)],
    "-" : [(0, -1), (0, 1)],
    "L" : [(-1, 0), (0, 1)],
    "J" : [(-1, 0), (0, -1)],
    "7" : [(1, 0), (0, -1)],
    "F" : [(1, 0), (0, 1)]
}

# Read input into list of list of chars
inp = [[c for c in l.strip()] for l in open("input.txt").readlines()]

# Create empty DiGraph with dimensions of outer list above
G = nx.create_empty_copy(
    nx.grid_2d_graph(
        len(inp[0]),
        len(inp),
        create_using = nx.DiGraph
    )
)

# At every character, add unidirectional connections (edges) to connected nodes
for i, l in enumerate(inp):
    for j, c in enumerate(l):
        # Special case for starting tile: Add edges to all surrounding and capture coordinates
        if c == "S":
            G.add_edges_from(
                [
                    (
                        (i, j),
                        (i + x, j + y)
                    )
                    for x in range(-1, 2)
                    for y in range(-1, 2)
                    if abs(x + y) == 1
                ]
            )
            sx, sy = i, j
            continue
        for connector in connectors.get(c, []):
            G.add_edge(
                (i, j),
                (i + connector[0], j + connector[1])
            )

# Remove all edges that only exist in one direction
G.remove_edges_from(
    (i, j)
    for i, j in G.copy().edges()
    if not G.has_edge(j, i)
)

# Part 1 solution: Find the length of the cycle. Half of it is the furthest distance
print(len(nx.find_cycle(G.to_undirected(), (sx, sy))) // 2)

# Create an empty array of twice the size as the input
space = np.ones(
    (2 * len(inp), 2 * len(inp[0]))
)

# For each edge (x, y) --> (x + a, y + b) where a + b = 1, turn the array fields from (2x, 2y) --> (2(x+a), 2(y+b)) into zeros, i.e. empty tiles.)
# We do it all 2 instead of 1 spaces wide to account for the gaps between pipes
for e in nx.find_cycle(G.to_undirected(), (sx, sy)):
    x, y = list(zip(*e))
    space[2 * min(x):2 * max(x) + 1, 2 * min(y): 2 * max(y) + 1] = 0

#print(space)

# First, find all connected tiles; these are the result of the label function. We only need its first return value.
# Labels are sorted by desc. size, and by definition the largest one will be the one connected to the outside (hence the padding, too)
# Now we get rid of the extra gaps by skipping every second column and row
# We are only interested in those connected tiles with labels greater than 1
# Simply return the total count of all remaining tiles that aren't connected to the outside, i.e. labels > 1
print(len(np.where(label(np.pad(space, 1, constant_values = 1))[0][1::2, 1::2] > 1)[0]))
