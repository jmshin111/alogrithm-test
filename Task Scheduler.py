from typing import List
import heapq


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

tasks = ["A", "A", "A", "B", "B", "B"]
n = 50

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
#Output: 16
#Explanation:
#One possible solution is
#A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

class Solution:


    def leastInterval (self, tasks: List[str], n: int) -> int:

        counter_s = {}
        heap = []
        index = 0
        for i_task in tasks:
            if(i_task in counter_s):
                counter_s[i_task] += 1
            else:
                counter_s[i_task] = 1

            if(counter_s[i_task] ==1):
                heapq.heappush(heap,(index, i_task))
                index += 1
            else:
                heapq.heappush(heap, ((counter_s[i_task]-1) * n, i_task))

        result = []
        start = True

        while heap:
            char = heapq.heappop(heap)

            if(result and char[0]- result[-1][0] >1):

                for i in range(char[0]- result[-1][0]):
                    result.append(('0','Idle'))

            result.append(char)

        print(result)
        return len(result)

print(Solution.leastInterval(Solution,tasks,n))