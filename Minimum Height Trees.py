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

n =6
edges =  [[3,0],[3,1],[3,2],[3,4],[5,4]]





n = 8
edges =  [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]



n =18
edges =  [[0,1],[1,2],[2,3],[3,4],[3,5],[5,6],[2,7],[0,8],[2,9],[4,10],[2,11],[4,12],[8,13],[12,14],[4,15],[13,16],[16,17]]
n = 7
edges =  [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
class Solution:
    max_height = -1
    max_height_path = []
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        grapgh = {}
        Solution.max_height = -1
        Solution.max_height_path = []
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
        h =[]
        def dfs(path:[], node:int, mode:bool):
            path.append(node)


            # print(node)
            # print(path)

            end_flag = True
            for i in grapgh[node]:
               if i not in path:
                  new_path = path[:]
                  dfs(new_path,i,mode)
                  end_flag = False

            if end_flag:
                if mode:
                    heapq.heappush(h,(-len(path), path))
                else:
                    heapq.heappush(h, (len(path), path))

        dfs([],edges[0][0],True)
        print(h)
        max_height = 0
        path_list = []
        h_end_flag = True

        result = set()
        result.add(edges[0][0])
        while h:
            next_node =  heapq.heappop(h)
            if next_node[0] < max_height:
                max_height = next_node[0]
                path_list.append(next_node[1])
            elif next_node[0] == max_height:
                path_list.append(next_node[1])
            else:

                break

        inspection_set = set()

        max_height = -max_height
        for i in path_list:

            middle_index = int(len(i)/2)

            inspection_set.add(i[middle_index])

            if middle_index-1 >=0:
                inspection_set.add(i[middle_index-1])
            if middle_index +1 <=len(i)-1:
                inspection_set.add( i[middle_index+1])

        print(inspection_set)


        for i in inspection_set:

            h =[]
            dfs([], i,True)

            temp_max_height = - h[0][0]
            print(temp_max_height)
            if max_height > temp_max_height:
                max_height = -h[0][0]
                result = set()
                result.add(i)
            elif -h[0][0] == max_height:
                result.add(i)

        result_list = list(result)
        return result_list

print(Solution.findMinHeightTrees(Solution,n,edges))