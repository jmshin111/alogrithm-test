from typing import List


nums = [1]


nums = [-2,-1]
nums = [-2,1]
nums = [3,-2,-3,-3,1,3,0]

nums = [-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [4,8,0,-2,5,2,-8,7,1,-4,4,8,-2,5,-5,-2,8]
print(sum(nums))
class Solution:

    sum= 0

    def recursive_test(self,nums:List[int]) -> int :
        temp_sum = 0
        print(nums)
        for i in range(len(nums)):
            if(nums[i] < 0 ):

                temp_sum_2 = Solution.recursive_test(Solution,nums[i+1:])
                print(nums[0:i], nums[i], nums[i + 1:], 'recursive : ', temp_sum_2)
                merge_all = temp_sum + temp_sum_2 +nums[i]

                if merge_all >= temp_sum and merge_all >= temp_sum_2:
                    temp_sum = merge_all
                    Solution.sum = max(Solution.sum, temp_sum)
                    print('merge_all',merge_all,'Max Sum',Solution.sum)
                elif temp_sum_2 >= temp_sum and temp_sum_2 >= merge_all:
                    Solution.sum = max(Solution.sum, temp_sum_2)
                    print('temp_sum2', temp_sum_2, 'Max Sum', Solution.sum)
                    if(temp_sum < merge_all):
                        temp_sum = merge_all

                    return temp_sum
                else:
                    Solution.sum = max(Solution.sum, temp_sum)
                    print('temp_sum', temp_sum, 'Max Sum', Solution.sum)

                break
            else:
                temp_sum += nums[i]

        Solution.sum = max(Solution.sum, temp_sum)
        return temp_sum

    def maxSubArray(self, nums: List[int]) -> int:
        Solution.sum = 0
        if(len(nums) == 1):
            return nums[0]
        minimum_digit = -9999999
        minimum_digit_count =0
        for i in nums:
            if(i<0):
                minimum_digit_count += 1
                minimum_digit = max(minimum_digit,i)
        if(len(nums) == minimum_digit_count):
            return minimum_digit

        Solution.recursive_test(Solution,nums)
        return Solution.sum


print(Solution.maxSubArray(Solution,nums))

