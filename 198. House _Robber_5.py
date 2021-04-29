import heapq
from typing import List

nums = [2,7,9,3,1]

nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
nums = [0]

nums = [1,2,1,1]

nums = [1,3,1]
nums = [2,7,9,3,1]
nums = [8,2,8,9,2]

nums = [1,2,1,1]

nums = [2,3, 2]
nums = [1,2,3,1]

nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
nums = [1,7,9,4]
[1,7] [4]


nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
[200][182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
[200][182,111,87,194,221,217,71,162,140,51,81][232][223,103,139,103]
[200][182,111,87,194,221,217,71,162,140,51,81][232][223][139,103]
[200][182,111,87,194,221,217,71,162,140,51,81][232][223][139]
[200][182,111][194][217][162,140,51,81][232][223][139]
[200][182][194][217][162][81][232][223][139]

221 87 71 182 140
194 217 111 162


232 81 223 140 139
80 193 51 103 162 103



[3,4,5,6,7]
[1,1,1,5,1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        heap_orgin = []
        print(sorted(sum))
        sum_all = 0

        for i in range(len(nums)):
            heapq.heappush(heap_orgin, [-nums[i] , i])
            sum_all += nums[i]

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


