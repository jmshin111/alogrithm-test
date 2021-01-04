from typing import List

nums1 = [1]
nums2 = [1]

#Output: [9,4]

class Solution:

    def find_binary_index(self,num_list,target):

        left = 0
        right = len(num_list)-1


        result = -1
        while(left<=right):
            mid = (left + right) // 2
            if(target > num_list[mid]):
                left = mid+1
            elif (target < num_list[mid]):
                right = mid - 1
            else:
                return num_list[mid]

        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = sorted(nums2)
        result = []
        for i_num1 in nums1:
            if i_num1 == Solution.find_binary_index(self,nums2,i_num1):
                result.append(i_num1)

        return result






print(Solution.intersection(Solution,nums1,nums2))

