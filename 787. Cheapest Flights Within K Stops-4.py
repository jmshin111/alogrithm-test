import collections
import heapq
from typing import List

n =10
edges =  [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst =0
k =7

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7


n =5
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]]
src = 0
dst = 4
k =2


n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

k = 1
n =17
edges =  [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst =4
k =13

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst =0
k= 7






n =5
edges = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2


n =4
edges =  [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst =3
k =1

n= 5
edges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src =2
dst = 1
k =1

n =3
edges = [[0,1,2],[1,2,1],[2,0,10]]
src = 1
dst =2
k = 1

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

n = 18
edges = [[16,1,81],[15,13,47],[1,0,24],[5,10,21],[7,1,72],[0,4,88],[16,4,39],[9,3,25],[10,11,28],[13,8,93],[10,3,62],[14,0,38],[3,10,58],[3,12,46],[3,8,2],[10,16,27],[6,9,90],[14,8,6],[0,13,31],[6,4,65],[14,17,29],[13,17,64],[12,5,26],[12,1,9],[12,15,79],[16,11,79],[16,15,17],[4,0,21],[15,10,75],[3,17,23],[8,5,55],[9,4,19],[0,10,83],[3,7,17],[0,12,31],[11,5,34],[17,14,98],[11,14,85],[16,7,48],[12,6,86],[5,17,72],[4,12,5],[12,10,23],[3,2,31],[12,7,5],[6,13,30],[6,7,88],[2,17,88],[6,8,98],[0,7,69],[10,15,13],[16,14,24],[1,17,24],[13,9,82],[13,6,67],[15,11,72],[12,0,83],[1,4,37],[12,9,36],[9,17,81],[9,15,62],[8,15,71],[10,12,25],[7,6,23],[16,5,76],[7,17,4],[3,11,82],[2,11,71],[8,4,11],[14,10,51],[8,10,51],[4,1,57],[6,16,68],[3,9,100],[1,14,26],[10,7,14],[8,17,24],[1,11,10],[2,9,85],[9,6,49],[11,4,95]]
src = 7
dst = 2
k = 6
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        queue = []

        queue.append([src])

        visited = set()

        node_dist = {}

        stack = []
        h = []

        print(graph)
        heapq.heappush(h,(0, src, src )) # dist, from, to
        node_dist[src] = 0

        result = 99999

        while h:
            next_node =  heapq.heappop(h)
            temp_list = []

            while h:
                if next_node[1] in node_dist:
                    break
                else:
                    temp_list.append(next_node)
                    next_node = heapq.heappop(h)
            for i in temp_list:
                heapq.heappush(h,i)

            print(len(stack), stack)
            #print(node_dist)
            #print(next_node)

            if next_node[2] not in visited:

                node_dist[next_node[2]] = node_dist[next_node[1]]+next_node[0]
                stack.append(next_node[2])
                visited.add(next_node[2])



                if len(stack) <= K+2:

                    if next_node[2] == dst:
                        result = min (result,node_dist[dst])

                        remove_node = stack.pop()
                        visited.remove(remove_node)
                        node_dist.pop(remove_node)


                    elif len(stack) == K+2:
                        # 빼기
                        if h:
                            next_next_node = heapq.heappop(h)

                            temp_list = []

                            while h:
                                if next_next_node[1] in node_dist:
                                    break
                                else:
                                    temp_list.append(next_next_node)
                                    next_next_node = heapq.heappop(h)
                            for i in temp_list:
                                heapq.heappush(h, i)

                        else:
                            continue

                        while stack:

                            if next_next_node[1] == stack[-1]:
                                heapq.heappush(h,next_next_node)

                                break
                            else:
                                remove_node = stack.pop()
                                visited.remove(remove_node)
                                node_dist.pop(remove_node)

                    else:
                        for x, y in graph[next_node[2]]:
                            heapq.heappush(h, (y, next_node[2], x))
        if result == 99999:
            return -1
        else:
            return result
print(Solution.findCheapestPrice(Solution,n,edges,src,dst,k))
