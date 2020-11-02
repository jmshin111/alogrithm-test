graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

discovered = []
queue = []
def bfs_recursive(graph):

    while queue:
        bfs_discovered_index = queue.pop(0)
        discovered.append(bfs_discovered_index)

        for index_graph in graph[bfs_discovered_index]:
            #if not index_graph in discovered:
            if not index_graph in discovered and not index_graph in queue:
                queue.append(index_graph)

queue.append(1)
bfs_recursive(graph)
print(discovered)