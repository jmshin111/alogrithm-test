import collections
import heapq
from typing import List

from sqlalchemy.orm.collections import collection

nums = [1,-1]
k = 1



nums = [7,2,4]
k =2


nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [1,3,1,2,0,5]
k = 3

nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
k = 7
#[9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 8, 8]
#[9, 9, 10, 10, 10, 10, 10, 10, 10, 9,  9, 9,  8,8]
class Solution:
    start_idx = 0
    end_idx = 0

    max_idx = 0
    max_val = -10000000


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()

        current_max = float('-inf')

        for i, v  in enumerate(nums):
            window.append(v)
            if i<k-1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif  v>current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return results

print(Solution.maxSlidingWindow(Solution,nums,k))