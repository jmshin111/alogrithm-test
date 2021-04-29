import heapq
from typing import List
from collections import Counter

batchSize = 4
groups = [1,3,2,5,2,2,1,6]
#Output: 4

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

batchSize = 4
groups = [1,2,3,4,5,6]
#Output: 4

class Solution:
    devide_key = {}
    max_count_group = 0
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:

        Solution.devide_key = {}
        Solution.max_count_group = 0
        result = 0
        for i in groups:
            devide_number =  i % batchSize
            if devide_number not in Solution.devide_key:
                Solution.devide_key[devide_number] =1
            else:
                Solution.devide_key[devide_number] += 1

        print(Solution.devide_key)


        h=[]
        def findMaxGroup(hop:int, path:[], rest_counter_key:{}):

            if hop == 0:
                path_sum =0
                for i in path:
                    path_sum += i
                if path_sum % batchSize ==0:
                    max_group = 0
                    index = 1
                    i_counter = Counter(path)
                    break_parameter = False

                    while True:
                        for i in i_counter:
                            if i_counter[i] * index<=Solution.devide_key[i]:
                                continue
                            else:
                                break_parameter = True
                                break
                        index += 1
                        if break_parameter:
                               break
                        else:
                               max_group += 1
                    h.append([-max_group,i_counter])

                else:
                    return
            else:
                first_digit = list(rest_counter_key)[0]
                empty_temp_rest_counter_key = rest_counter_key.copy()
                empty_temp_rest_counter_key.pop(first_digit)
                findMaxGroup(hop , path, empty_temp_rest_counter_key)

                for i in range(rest_counter_key[first_digit]):
                    temp_rest_counter_key = rest_counter_key.copy()
                    temp_rest_counter_key.pop(first_digit)
                    temp_path = path.copy()
                    for j in range(i):
                        temp_path.append(first_digit)

                    temp_path.append(i)
                    findMaxGroup(hop-1,temp_path,empty_temp_rest_counter_key)


        def findMaxRefreshDonut3(n: int, max_f_group:int):

            h.clear()
            findMaxGroup(n,[],Solution.devide_key)

            if not h:
                max_count = 0
                for i in list(Solution.devide_key):
                    max_count +=Solution.devide_key[i]
                if max_count < n+1:
                    Solution.max_count_group = max_f_group
                else:
                    findMaxRefreshDonut3(n+1, max_f_group )
            else:

                max_heap_list = []

                temp_h = sorted(h, key=lambda x: x[0])
                print(temp_h)
                while temp_h:
                    temp_heap = temp_h.pop(0)
                    max_heap_list.append(temp_heap)
                    if max_heap_list[0][0] == temp_heap[0]:
                        continue
                    else:
                        if max_heap_list:
                            max_heap_list.remove(temp_heap)
                        break

                for i in max_heap_list:

                    current_max_group = -i[0]
                    for j in i[1]:
                        Solution.devide_key[j] -= i[1][j]
                    h.clear()
                    findMaxRefreshDonut3(n , max_f_group+current_max_group)


        #findMaxRefreshDonut3(1,0)

        print('Result')
        return Solution.max_count_group


print(Solution.maxHappyGroups(Solution,batchSize,groups))