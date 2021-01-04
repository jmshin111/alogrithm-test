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

            if(i_task in counter_s and index - counter_s[i_task]< n):
                heapq.heappush(heap,(counter_s[i_task]+n+1,i_task ))
                counter_s[i_task] = counter_s[i_task]+n+1
            else:
                heapq.heappush(heap, (index, i_task))
                if i_task not in counter_s:
                    counter_s[i_task] = index
                index += 1

        result = []
        memory = {}

        print(heap)
        current_index = 0
        while heap:
            char = heapq.heappop(heap)
            if(current_index <char[0]):
                for i in range(char[0]-current_index):
                    result.append((0,'Idle'))
            result.append(char)
            current_index +=1
        print(result)
        return len(result)

print(Solution.leastInterval(Solution,tasks,n))