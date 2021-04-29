import heapq
from typing import List
from collections import Counter

batchSize = 4
groups = [1,3,2,5,2,2,1,6]
#Output: 4

batchSize = 4
groups = [1,2,3,4,5,6]
#Output: 4

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:

        devide_key = {}
        group_list = []
        result = 0
        for i in groups:
            devide_number =  i % batchSize
            if devide_number not in devide_key:
                devide_key[devide_number] =1
            else:
                devide_key[devide_number] += 1

        print(devide_key)
        for i in devide_key:
            group_list.append(i)
        possible_batch_list = []

        def addPossibleList(path:[]):
            path_sum = 0
            counter = Counter(path)

            for i in counter:
                if counter[i] > devide_key[i]:
                    return
                else:
                    path_sum += i * counter[i]

            if path_sum % batchSize == 0:
                if not counter in possible_batch_list:
                    possible_batch_list.append(counter)

        def findMaxRefreshDonut2(n: int, start_index: int, path: [],zero_count:int):

            if start_index == len(group_list)-1:
                while zero_count:
                    path.append(group_list[start_index])
                    zero_count -=1
                addPossibleList(path)


            for i in range(0, zero_count + 1):
                for j in range(start_index + 1, len(group_list)):
                    next_path = path[:] + ([group_list[start_index]] * i)

                    if zero_count >i:
                        findMaxRefreshDonut2(n, j, next_path, zero_count-i)
                    else:
                        addPossibleList(next_path)

        def findMaxRefreshDonut3(n: int, start_index: int, path: [],zero_count:int):





        max_group_number = 1



        return result

print(Solution.maxHappyGroups(Solution,batchSize,groups))