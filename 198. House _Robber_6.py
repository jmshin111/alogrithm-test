import heapq
from typing import List



nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
nums = [0]



nums = [1,2,1,1]














nums = [1,2,1,1]
nums = [1,2,3,1]

nums = [1,3,1]







nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]










nums = [2,7,9,3,1]
nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
nums = [1,7,9,4]
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
nums = [2,3, 2]

nums = [8,2,8,9,2]
nums = [4,1,2,7,5,3,1]
class Solution:
    result = 0

    def recursive_rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            Solution.result += nums[0]
            print(nums[0])
        else:
            max = -1
            max_i = -1
            for i in range(len(nums)):
                if(nums[i] > max):
                    max = nums[i]
                    max_i = i

            if(max_i > int((len(nums)-1)/2)):
                loop_count = int((len(nums)-1-max_i)/2)
            else:
                loop_count = int(max_i / 2)

            max_current = nums[max_i]
            if(max_i<=len(nums)-3):
                max_current += nums[max_i + 2]
            if(max_i>=2):
                max_current += nums[max_i - 2]
            max_others = 0
            if(max_i<len(nums)-1):
                max_others += nums[max_i + 1]
            if(max_i >= 1):
                max_others += nums[max_i - 1]

            # for i in range(loop_count):
            #         if (max_i + 2 * (i + 1)  < len(nums)):
            #             max_current += nums[max_i+2*(i+1)]
            #
            #         if (max_i - 2 * (i + 1) >= 0 ):
            #             max_current +=  nums[max_i -2*(i+1)]
            #
            #         if(max_i+2*(i+1)+1< len(nums)):
            #             max_others += nums[max_i+2*(i+1)+1]
            #
            #         if (max_i - (2 * (i + 1) + 1) >=0):
            #             max_others +=  nums[max_i - (2 * (i + 1) + 1)]
            if(max_current >= max_others):
                if(max_i > 1):
                    Solution.recursive_rob(Solution,nums[:max_i-1])
                Solution.recursive_rob(Solution, [nums[max_i]])
                if(max_i <= len(nums)-3):
                    Solution.recursive_rob(Solution, nums[max_i+2:])
            else:
                if (max_i >= 3):
                    Solution.recursive_rob(Solution, nums[:max_i - 2])
                Solution.recursive_rob(Solution, [nums[max_i - 1]])
                Solution.recursive_rob(Solution, [nums[max_i +1]])
                if (max_i <= len(nums) - 4):
                    Solution.recursive_rob(Solution, nums[max_i + 3:])

        return Solution.result
    def rob(self, nums: List[int]) -> int:
        Solution.result = 0
        if(len(nums)>=1):
            Solution.recursive_rob(Solution,nums)
        return Solution.result


print(Solution.rob(Solution,nums))




