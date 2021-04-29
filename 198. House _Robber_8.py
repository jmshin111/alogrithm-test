import heapq
from typing import List



nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
nums = [0]

nums = [1,2,1,1]

nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]

nums = [4,1,2,7,5,3,1]
nums = [8,2,8,9,2]

nums = [1,7,9,4]

nums = [2,7,9,3,1]

nums = [1,3,1]




nums = [1,2,1,1]
nums = [8,4,8,5,9,6,5,4,4,10]
nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
nums = [1,2,3,1]
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
nums = [2,3, 2]
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class Solution:
    result = 0

    def recursive_rob(self, nums: List[int]) -> int:
        print(nums)
        if(len(nums)==1):
            return nums[0]
        else:
            max_temp = 0
            max_i = -1
            for i in range(len(nums)):
                if(nums[i] > max_temp):
                    max_temp = nums[i]
                    max_i = i
            if(max_i==-1):
                return 0
            sum_1 = 0
            sum_2 = 0
            if(max_i-2 >=0):
                sum_1 += Solution.recursive_rob(Solution,nums[:max_i-1])
            sum_1 += nums[max_i]
            if(max_i+2<=len(nums)-1):
                sum_1 += Solution.recursive_rob(Solution, nums[max_i+2:])

            if(max_i-1>=0):
                sum_2 += nums[max_i-1]
            if(max_i +1 <=len(nums)-1):
                sum_2 += nums[max_i + 1]
            if(max_i-3>=0):
                sum_2 += Solution.recursive_rob(Solution,nums[:max_i-2])
            if (max_i + 3 <= len(nums)-1):
                sum_2 += Solution.recursive_rob(Solution, nums[max_i + 3:])

        result = max(sum_1,sum_2)
        return result


    def rob(self, nums: List[int]) -> int:
        sum = 0
        if(len(nums)>=1):
            sum = Solution.recursive_rob(Solution,nums)
        return sum


print(Solution.rob(Solution,nums))




