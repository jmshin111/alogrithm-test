from typing import List


nums = [1,2,3,4,5,6,7,8,9]
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(self,i_num:List, start_index, end_index, target):

            middle_val = int((start_index + end_index) / 2)+1
            if middle_val >= len(i_num):
                middle_val =  len(i_num) - 1

            if i_num[middle_val] == target:
                return middle_val
            elif i_num[middle_val] < target :
                return  binary_search(self,i_num,middle_val,end_index,target)
            elif i_num[middle_val] > target :
                return binary_search(self, i_num, start_index, middle_val, target)
            else:
                return -1

        return binary_search(self,nums,0,len(nums)-1,target)

print(Solution.search(Solution,nums,4))