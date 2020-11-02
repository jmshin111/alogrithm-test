
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

def recursive_dfs(index_graph):

    discovered.append(index_graph)

    if (graph[index_graph] ):
        for index_input_graph in graph[index_graph]:
            if(not index_input_graph in discovered):
                recursive_dfs(index_input_graph)

recursive_dfs(1)
print(discovered)
