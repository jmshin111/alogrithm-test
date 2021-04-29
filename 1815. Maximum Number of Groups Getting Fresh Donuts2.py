import heapq
from itertools import permutations, combinations
from typing import List
from collections import Counter




batchSize = 4
groups = [1,2,3,4,5,6]
#Output: 4

batchSize = 4
groups = [1,3,2,5,2,2,1,6]
#Output: 4

batchSize = 3
groups = [1,2,3,4,5,6]
#Output: 4

batchSize = 2
groups=[916210963,37071830,515639792,260640057,798574708,856206295,434101040,444866270,713762924,185765287,394196213,589268180,947826294,754884266,833049335,724223643,792652821,402334308,92843871]
#Output: 15

batchSize = 4
groups = [1,3,2,5,2,2,1,6]

batchSize = 2
groups = [652231582,818492002,823729239,2261354,747144855,478230860,285970257,774747712,860954510,245631565,634746161,109765576,967900367,340837477,32845752,23968185]

batchSize = 7
groups =[145326640,622724151,591814792,827053040,111964428,344376875,42023891,436582274,78590835,408269112,930041188,846233596,158192647,889601516,134236253,366035866,123146762]
# 9

batchSize = 9
groups = [3,1,3,3,5,6,1,1,9,10,3,3,3,1,1,3,3,3,19,20,1,3,3,3,3,1,1,3,3,30]
class Solution:

    result =0
    third_group_result = 0
    devide_global_key= {}
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        Solution.result = 0
        Solution.third_group_result = 0
        devide_key = {}
        group_list = []

        for i in groups:
            devide_number =  i % batchSize
            if devide_number not in devide_key:
                devide_key[devide_number] =1
            else:
                devide_key[devide_number] += 1




        print(devide_key)
        for i in devide_key:
            group_list.append(i)

        if 0 in devide_key:
            Solution.result += devide_key[0]
            devide_key.pop(0)

        visited = set()

        for i in list(devide_key):
            if i not in visited:
                others = batchSize-i
                if others in devide_key:
                    if devide_key[i]> devide_key[others]:
                        Solution.result += devide_key[others]
                        devide_key[i] -= devide_key[others]
                        devide_key.pop(others)
                        visited.add(i)
                        visited.add(others)
                    else:
                        if i == others:
                            Solution.result += int(devide_key[i] / 2)
                            if devide_key[i]%2==0:
                                devide_key[others] -= devide_key[i]
                                devide_key.pop(i)

                                visited.add(i)
                                visited.add(others)
                            else:
                                devide_key[i] =1


                                visited.add(i)
                                visited.add(others)
                        else:
                            Solution.result += devide_key[i]
                            devide_key[others] -= devide_key[i]

                            devide_key.pop(i)
                            visited.add(i)
                            visited.add(others)





        combination_list = []
        for i in list(devide_key):
            if devide_key[i] >0:
                for j in range(devide_key[i]):
                    combination_list.append(str(i))
        if len(combination_list)==0:
            return int(Solution.result)

        third_group =[]
        for i in (list(map(''.join, combinations( combination_list, 3)))):
            if (int(i[0])+int(i[1])+int(i[2])) % batchSize !=0 or [int(i[0]),int(i[1]),int(i[2])] in third_group:
                continue
            else:
                third_group.append([int(i[0]),int(i[1]),int(i[2])])

        print(devide_key)
        print(third_group)

        h = []

        def findMaxThirdPartyGroup(temp_third_group:[],temp_devide_key:{},max_group):

            h =[]
            for i in temp_third_group:
                    devide_key_copy = temp_devide_key.copy()
                    i_counter = Counter(i)

                    break_parameter = False
                    find_value= False
                    while True:

                        for j in i_counter:
                            if i_counter[j] <= devide_key_copy[j]:
                                continue
                            else:
                                break_parameter = True

                        if break_parameter:
                            break

                        for k in i_counter:
                            devide_key_copy[k] -= i_counter[k]
                        max_group +=1
                        find_value = True
                    if find_value:
                        heapq.heappush(h, (-max_group, i_counter))

            if not h:
                Solution.third_group_result = max(Solution.third_group_result,max_group)
                Solution.devide_global_key =temp_devide_key
                return


            max_heap_list=[]
            while h:
                temp_heap = heapq.heappop(h)
                max_heap_list.append(temp_heap)
                if max_heap_list[0][0] == temp_heap[0]:
                    continue
                else:
                    if max_heap_list:
                        max_heap_list.remove(temp_heap)
                    break

            for i in max_heap_list:
                revers_counter = []
                copy_third_group= temp_third_group[:]
                copy_device_key = temp_devide_key.copy()

                for j in copy_third_group:
                    temp_coutner = Counter(j)
                    if temp_coutner.values().__eq__(i[1].values()):
                        copy_third_group.remove(j)

                        break_parameter2 = False
                        while True:

                            for k in temp_coutner:
                                if copy_device_key[k] >= temp_coutner[k]:
                                    copy_device_key[k] -= temp_coutner[k]
                                else:
                                    break_parameter2 = True
                            if break_parameter2:
                                break
                        findMaxThirdPartyGroup(copy_third_group  ,copy_device_key  ,max_group -i[0])
                        break



        findMaxThirdPartyGroup(third_group, devide_key, 0)
        Solution.result += Solution.third_group_result
        devide_key = Solution.devide_global_key

        permutation_list = []

        for i in list(devide_key):
            if devide_key[i] >0:
                for j in range(devide_key[i]):
                    permutation_list.append(str(i))
        if len(permutation_list)==0:
            return int(Solution.result)
        real_max = 0

        print(permutation_list)
        for i in list(map(''.join, permutations(permutation_list))):
            #print(i)
            rest = 0
            temp_max = 0

            for j in i:

                rest = (int(j)+rest) % batchSize

                if rest == 0:
                    temp_max +=1
            if rest != 0:
                temp_max +=1
            real_max = max(temp_max,real_max)
        Solution.result += real_max
        return int(Solution.result)

print(Solution.maxHappyGroups(Solution,batchSize,groups))
