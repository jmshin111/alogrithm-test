import heapq
from typing import List

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

        if k==1:
            return nums

        h = []
        result = []
        print(len(nums))

        self.end_idx = k - 1
        for i in range(self.start_idx, self.end_idx + 1):
            heapq.heappush(h,(-nums[i],i))

        next_heap =  heapq.heappop(h)

        self.max_val = -next_heap[0]
        self.max_idx = next_heap[1]

        while h:
            if h[0][0] ==  -self.max_val:
                temp_heap = heapq.heappop(h)
                self.max_idx = temp_heap[1]
            else:
                break
        result.append(self.max_val)

        for next_idx in range(k, len(nums)):

            heapq.heappush(h,(-nums[next_idx],next_idx))

            if nums[next_idx] > self.max_val:

                temp_heap = heapq.heappop(h)
                self.max_idx = temp_heap[1]
                self.max_val = -temp_heap[0]

            elif next_idx - self.max_idx+1 > k :
                temp_heap = None
                while h:

                    temp_heap = heapq.heappop(h)
                    if temp_heap[1] < self.max_idx:
                        continue

                    if h[0][0] == -self.max_val:
                        self.max_idx = temp_heap[1]
                        continue

                    break
                self.max_idx = temp_heap[1]

                self.max_val = -temp_heap[0]

            result.append(self.max_val)

        return result

print(Solution.maxSlidingWindow(Solution,nums,k))