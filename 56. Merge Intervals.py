from typing import List

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result =[]

        sorted_list = sorted(intervals, key=lambda x : (x[0],x[1]))

        start_val = sorted_list[0][0]
        end_val = sorted_list[0][1]
        print(sorted_list)
        for i in sorted_list:
            first_val = i[0]
            second_val = i[1]

            if start_val == first_val:
                end_val = second_val

            if end_val >= first_val and end_val <= second_val:
                end_val = second_val

            if end_val < first_val:
                result.append([start_val,end_val])
                start_val = first_val
                end_val = second_val
        if sorted_list:
            result.append([start_val,end_val])


        return result

print(Solution.merge(Solution,intervals))

