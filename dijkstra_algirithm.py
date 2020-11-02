import collections
import sys
from operator import itemgetter

#그래프는 노드간 소스 타깃만 표시
#노드간 거리는 별도 키셋으로 표시
times = [[2,1,1],[2,3,1],[3,4,1],[3,5,2],[2,5,1],[4,5,1]]

N = 4
K = 2

graph = collections.defaultdict(list)
for u,v,w in times:
    graph[u].append(v)


graph_div = collections.defaultdict()
for i_times in times:
    graph_div[(i_times[0],i_times[1])] = i_times[2]


dist = collections.defaultdict()
prev = collections.defaultdict(list)

print(graph)

def dijkstra(graph, source):

    dist[source] = 0

    priority_queue = []

    #재귀함수로 만들어야 함

    def make_dist_prev(i_node,source):
        if i_node not in graph[source]:
            dist[i_node] = sys.maxsize
            prev[i_node] = []
        else:
            dist[i_node] = graph_div[source, i_node]
            prev[i_node] = []
        if ([i_node, dist[i_node]])  not in priority_queue:
            priority_queue.append([i_node, dist[i_node]])

        if i_node not in graph:
            return
        for child_node in graph[i_node]:
            make_dist_prev(child_node,source)

    for child_node in list(graph):
        make_dist_prev(child_node,source)




    # for child_node in list(graph):
    #     if child_node not in graph[source]:
    #         dist[child_node] = sys.maxsize
    #         prev[child_node] = None
    #     else:
    #         dist[child_node] = graph_div[source,child_node]
    #
    #
    #     priority_queue.append([child_node,dist[child_node]])

    while priority_queue:
        priority_queue.sort(key= itemgetter(1),reverse=True)
        u = priority_queue.pop()
        u_node = u[0]

        for child_node in list(graph[u_node]):
            alt = dist[u_node] + graph_div[u_node, child_node]
            if alt < dist[child_node]:
                dist[child_node] = alt
                prev[child_node].append(u_node)
                priority_queue.append([child_node,alt])

    return dist,prev

print(dijkstra(graph,2))