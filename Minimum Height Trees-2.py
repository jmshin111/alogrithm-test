import heapq
from typing import List

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

n = 4
edges = [[1,0],[1,2],[1,3]]
n = 2
edges = [[0, 1]]

n = 6
edges =[[0,1],[0,2],[0,3],[3,4],[4,5]]







n = 8
edges =  [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]




n = 7
edges =  [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
n =18
edges =  [[0,1],[1,2],[2,3],[3,4],[3,5],[5,6],[2,7],[0,8],[2,9],[4,10],[2,11],[4,12],[8,13],[12,14],[4,15],[13,16],[16,17]]

n =6
edges =  [[3,0],[3,1],[3,2],[3,4],[5,4]]
class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        grapgh = {}

        result = []

        if len(edges)==0:
            return [0]
        if len(edges)==1:
            return edges[0]

        for i in edges:
            if i[0] not in grapgh:
                grapgh[i[0]] = [i[1]]
            else:
                grapgh[i[0]].append(i[1])

            if i[1] not in grapgh:
                grapgh[i[1]] = [i[0]]
            else:
                grapgh[i[1]].append(i[0])

            visited = set()

        print(grapgh)

        visited = set()

        def dfs(node:int)->int :

            end_flag = True
            max_height= -1
            visited.add(node)
            for i in grapgh[node]:
                if i not in visited:
                    max_height =max(dfs(i)+1,max_height)
                    end_flag = False

            if end_flag:
                return 1
            else:
                return max_height

        max_height = 999999
        max_group = set()

        queue = []
        queue.append(0)
        queue_visited = set()
        while queue:

            max_list = []
            start_node = queue.pop(0)
            for i in grapgh[start_node]:
                visited = set()
                if i in queue_visited:
                    continue
                else:
                    i_max_height = dfs(i)

                if max_height > i_max_height:
                    max_group = set()
                    max_height = i_max_height
                    max_group.add(i)
                    queue.append(i)
                    queue_visited.add(i)
                elif max_height == i_max_height:
                    max_group.add(i)
                    queue.append(i)
                    queue_visited.add(i)


        return list(max_group)

print(Solution.findMinHeightTrees(Solution,n,edges))