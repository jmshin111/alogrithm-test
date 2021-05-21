from typing import List




nums = [1,-1]
k = 1


nums = [1,3,1,2,0,5]
k = 3
nums = [1,3,-1,-3,5,3,6,7]
k = 3


nums = [7,2,4]
k =2

class Solution:
    start_idx = 0
    end_idx = 0

    max_idx = 0
    max_val = -10000000


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k==1:
            return nums


        result= []
        self.end_idx = k-1
        for i in range(self.start_idx,self.end_idx+1):
             if self.max_val <= nums[i]:
                #self.max_idx = i
                self.max_val = nums[i]

        result.append(self.max_val)

        for next_idx in range(self.end_idx + 1, len(nums)):
                self.end_idx = next_idx
                if nums[next_idx] >= self.max_val:
                    #self.max_idx = next_idx
                    self.max_val = nums[next_idx]


                elif self.end_idx- self.start_idx  +1>k:
                    self.start_idx = self.end_idx - (k-1)
                    self.max_val = nums[self.start_idx]

                    for i in range(self.start_idx,self.end_idx+1):
                        if self.max_val <= nums[i]:
                            self.start_idx = i
                            self.max_val = nums[i]

                result.append(self.max_val)

        return result

print(Solution.maxSlidingWindow(Solution,nums,k))