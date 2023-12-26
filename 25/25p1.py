import networkx as nx

adj_list = {}
with open('input.txt') as file:
    for line in file:
        l, r = line.strip().split(':')
        adj_list[l] = r.split()

G = nx.Graph(adj_list)
_, part = nx.stoer_wagner(G)

print(len(part[0]) * len(part[1]))
