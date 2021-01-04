import collections
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

        counter_s = collections.Counter(tasks)
        print('=== Change task to Counter')
        print(counter_s)
        heap = []

        for i in counter_s:
            heapq.heappush(heap,(-counter_s[i], i))

        result = []

        while heap:
            count = 0
            count_r = {}

            temp_list = []
            current_heap_count = len(heap)
            while True:
                if(heap.__len__() != 0):
                    temp_list.append(heapq.heappop(heap))


                if (current_heap_count != 0) and -temp_list[-1][0] >= 2:
                    count += 1
                elif (current_heap_count != 0) and -temp_list[-1][0] == 1:
                    current_heap_count -= 1
                    if count <= n :
                        count += 1
                        # if (heap.__len__() == 0):
                        #     temp_list.append((0,'I'))
                        continue
                    else:
                        heapq.heappush(heap, temp_list.pop())
                        break
                if heap.__len__() == 0 and count < n :
                   for i in range(n-count+1):
                      temp_list.append((0,'I'))
                   count = n+1
                current_heap_count -= 1
                if count > n :
                    break

            for i_temp_list in temp_list:
                result.append(i_temp_list)
                if (i_temp_list[0]+1 !=0):
                    heapq.heappush(heap, (i_temp_list[0]+1, i_temp_list[1]))


        return len(result)

print(Solution.leastInterval(Solution,tasks,n))

# 2개 이상인 것과 1개인 것 그룹을 분리함
# 개수가 2 개 이상인 것의 개수가 N+1개인지 확인한다
    # N+1일 경우 2개 이상 그룹에서 1을 빼서 다시 넣는다 값이 1로 바뀌는 것은 1인 그룹으로 이동한다.



# 아닐 경우 1개그룹에서 부족한 개수만큼 뺀다. 1이 없을 경우 Idle로 입력한다.

# 2그룹이 없을 경우 1그룹에서 N+1만큼 반복하게 만들고 나머지로는 Idle을 만든다. 1 그룹에 1개남으면 그것만 그대로 넣고 종료한다.

# 1그룹 2그룹 모두 없으면 종료한다.

