from typing import List


nums = [0]




nums = [1, 2, 3,4]
nums = [1, 2, 3]
nums = [1, 2, 3,4]
nums = [1, 2, 3]
nums = [1, 2, 3,4]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def recursiveNum(nums:List[int],path:List[int]):
            #print(nums)

            if len(nums)== 1:
                result.append(path+nums)
            else:
                result.append(path+[nums[0]])
                for i in range(1,len(nums)):
                  recursiveNum(nums[i:],path+[nums[0]])


        recursiveNum(nums,[])

        return result



print(Solution.subsets(Solution,nums))
