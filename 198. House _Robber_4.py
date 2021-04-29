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
nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]


class Solution:
    result_s = 0
    def recursive_max_value(self,sum,nums):
        min_n = 999999
        target_index = -1
        if(len(nums)<1):
            return
        if(len(nums)==1):
            Solution.result_s += nums[0]
            return
        for i in range(len(nums)):
            if(i==0):
                if (min_n > nums[i + 1] ):
                    min_n = nums[i + 1]
                    target_index = i
                continue
            elif(i== len(nums)-1):
                if (min_n > nums[i - 1] ):
                    min_n = nums[i - 1]
                    target_index = i
                continue
            if(min_n > nums[i+1]+nums[i-1]):
                min_n = nums[i+1]+nums[i-1]
                target_index = i
        Solution.result_s += nums[target_index]
        if(target_index >=1):
            Solution.recursive_max_value(Solution, sum + nums[target_index], nums[:target_index-1])
        if(target_index <=len(nums)-2):
            Solution.recursive_max_value(Solution, sum + nums[target_index], nums[target_index+2:])

    def rob(self, nums: List[int]) -> int:
        Solution.result_s = 0
        if len(nums)==0:
            return 0
        Solution.recursive_max_value(Solution,0,nums)

        return Solution.result_s

print(Solution.rob(Solution,nums))


