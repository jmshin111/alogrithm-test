from typing import List

candidates = [2, 3, 5]
target = 8

candidates = [1,2]
target = 4
class Solution:

    def recursiveCombinationSum(self,candidates: List[int], target: int)-> List[List[int]]:

        result = []

        print(candidates,target)

        if len(candidates)==1 and target % candidates[0] == 0:
            if candidates[-1]> target:
                return result
            for i in range(int(target / candidates[0])):
                result.append(candidates[0])

        elif len(candidates) !=1:

            if candidates[-1] > target and len(candidates)>2:
                return Solution.recursiveCombinationSum(Solution,candidates[0:len(candidates)-2],target)

            else:

                for i in range(int(target / candidates[-1])):

                    for j in range(i+1):
                        temp_result = []
                        for j in range(j+1):
                            temp_result.append(candidates[-1])
                        rest_target = target-(candidates[-1]*(j+1))
                        return_CombinationSum = []
                        if rest_target > 0:
                            return_CombinationSum = Solution.recursiveCombinationSum(Solution,candidates[0:len(candidates)-1],rest_target)
                        else:
                            result = temp_result
                        if len(return_CombinationSum) != 0:
                            for i in return_CombinationSum:
                                temp_result.append(i)

                            result = temp_result

        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates.sort()
        end_index = len(candidates)
        for i in range(len(candidates)):
            if candidates[i] > target:
                end_index = i

        while end_index >0:
            temp_result = Solution.recursiveCombinationSum(Solution,candidates[0:end_index],target)
            if len(temp_result)>0:
                result.append(temp_result)
            end_index -= 1

        return result

print(Solution.combinationSum(Solution,candidates,target))
