from typing import List
from collections import Counter

nums = [1]
#Output: [1]

nums = [0]
#Output: [0]
nums = [2,0,1]
#Output: [0,1,2]

nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#[0,0,2,1,1,2]
#[0,0,2,1,1,2]

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_list = []
        one_list = []
        two_list = []
        nums_counter =  Counter(nums)

        if 0 in nums_counter:
           zero_list =[0]*nums_counter[0]

        if 1 in nums_counter:
           one_list = [1] * nums_counter[1]

        if 2 in nums_counter:
            two_list = [2] * nums_counter[2]
        return zero_list + one_list + two_list


print(Solution.sortColors(Solution, nums))
