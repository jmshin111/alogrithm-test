import heapq
from typing import List

nums = [2,7,9,3,1]
nums = [2,3, 2]
nums = [2,7,9,3,1]
nums = [1,2,3,1]
nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]

nums = [8,2,8,9,2]
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
        heap = []
        visited = []
        for i in range(len(nums)):
            heapq.heappush(heap, [-nums[i] , i])


        while(heap):
           maximum_house = heapq.heappop(heap)
           if (maximum_house[1] not in visited):
               minus_one = 0
               minus_two = 0
               plus_one = 0
               plus_two = 0

               if(maximum_house[1] > 0 ):
                  minus_one = nums[maximum_house[1] - 1]
               if (maximum_house[1] > 1):
                  minus_two = nums[maximum_house[1] - 2]

               if (maximum_house[1] < len(nums)-1):
                  plus_one = nums[maximum_house[1] + 1]
               if (maximum_house[1] < len(nums) - 2):
                  plus_two = nums[maximum_house[1] + 2]

               if(-maximum_house[0]+minus_two+plus_two >= minus_one+plus_one):
                    visited.append(maximum_house[1] - 1)
                    visited.append(maximum_house[1])
                    visited.append(maximum_house[1] + 1)
                    result += maximum_house[0]


        return -result

print(Solution.rob(Solution,nums))

