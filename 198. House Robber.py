import heapq
from typing import List

nums = [2,7,9,3,1]
nums = [2,3, 2]
nums = [2,7,9,3,1]

nums = [1,2,3,1]

nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]


sum = [200, 182, 194, 217, 162, 81, 232, 223, 139]
        X    X

#
# [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
# [200,    182,    87,    221,       162,       81    232,    223,    139]
# [200,    182,       194,    217,   162,       81,   232,    223,    139]
#
# [200, 232, 223, 221, 182, 162, 139, 87, 81]
#
# [    217, 234, 232, 223, 194, 162, 139, 111, 81]

answer2 = [194, 234, 232, 223, 217, 162, 139, 111, 81]
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        heap_orgin = []
        print(sorted(sum))
        s = 0
        for i in sum:
            s += i
        print(s)

        for i in range(len(nums)):
            heapq.heappush(heap_orgin, [-nums[i] , i])

        for i in heap_orgin:
            heap = heap_orgin[:]
            visited = []
            real_visited = []
            temp_result = i[0]
            visited.append(i[1] - 1)
            visited.append(i[1] )
            visited.append(i[1] + 1)

            real_visited.append(i[1])
            while(heap):
                maximum_house = heapq.heappop(heap)
                if (maximum_house[1] not in visited):
                    visited.append(maximum_house[1] - 1)
                    visited.append(maximum_house[1])
                    visited.append(maximum_house[1] + 1)
                    real_visited.append(maximum_house[1])
                    temp_result += maximum_house[0]

            print(temp_result,sorted(real_visited))
            real_val = []
            for i in range(len(real_visited)):
                real_val.append(nums[real_visited[i]])
            print(temp_result, real_val)

            result = min(result,temp_result)

        return -result

print(Solution.rob(Solution,nums))

