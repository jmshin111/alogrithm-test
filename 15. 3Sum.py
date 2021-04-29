from collections import Counter
from typing import List

nums = [-1,0,1,2,-1,-4]
nums = [0]
nums = [0,0,0]
nums = [1,1,-2]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_key = {}
        zero_index = -1
        divide_index = -1
        nums_sorted = sorted(nums)
        zero_count = nums_sorted.count(0)
        if(zero_count >=3):
            result.append([0,0,0])
        for i in range(zero_count-1):
            nums_sorted.remove(0)


        if len(nums)<3:
            return []
        for i in range(len(nums_sorted)):
            if nums_sorted[i]==0:
                zero_index = i
            elif nums_sorted[i]>0:
                divide_index = i
                break
        if(zero_index != -1):
            minus_counter = Counter(nums_sorted[:zero_index])
            plus_counter = Counter(nums_sorted[zero_index+1:])

            for i in minus_counter:
                if -i in plus_counter:
                    for j in range(min(minus_counter[i],plus_counter[-i])):
                        if(str(i)+'-'+str(0)+'-'+str(-i) not in result_key ):
                            result_key[str(i)+'-'+str(0)+'-'+str(-i)]=1
                            result_key[str(-i)+'-'+str(0)+'-'+str(i)] = 1
                            result.append([i,0,-i])
        minus_group = {}
        plus_group = {}
        middle_index = divide_index

        if(zero_index !=-1):
            middle_index = zero_index

        for i in range(middle_index):
            j = i +1
            while j < middle_index:
                c_sum = nums_sorted[i] + nums_sorted[j]
                if c_sum not in minus_group:
                    minus_group[c_sum] = [[nums_sorted[i],nums_sorted[j]]]
                else:
                    minus_group[c_sum].append([nums_sorted[i],nums_sorted[j]])
                j += 1
        for i in range(divide_index,len(nums_sorted)):
            j = i+1
            while j < len(nums_sorted):
                c_sum = nums_sorted[i] + nums_sorted[j]
                if c_sum not in plus_group:
                    plus_group[c_sum] = [[nums_sorted[i], nums_sorted[j]]]
                else:
                    plus_group[c_sum].append([nums_sorted[i],nums_sorted[j]])
                j += 1

        for i in range(middle_index):
            if -nums_sorted[i] in plus_group:
                for j in plus_group[-nums_sorted[i]]:
                    if (str(nums_sorted[i])+'-'+str(j[0])+'-'+str(j[1]) not in result_key):
                        result_key[str(nums_sorted[i])+'-'+str(j[0])+'-'+str(j[1])] = 1
                        result.append([nums_sorted[i],j[0],j[1]])

        for i in range(divide_index,len(nums_sorted)):
            if -nums_sorted[i] in minus_group:
                for j in minus_group[-nums_sorted[i]]:

                    if (str(nums_sorted[i])+'-'+str(j[0])+'-'+str(j[1]) not in result_key):
                        result_key[str(nums_sorted[i])+'-'+str(j[0])+'-'+str(j[1])] = 1
                        result.append([nums_sorted[i],j[0],j[1]])

        return result

print(Solution.threeSum(Solution,nums))




