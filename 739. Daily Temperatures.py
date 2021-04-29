from typing import List

T = [55,38,53,81,61,93,97,32,43,78]
T = [73, 74, 75, 71, 69, 72, 76, 73]
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        result = [0]*len(T)
        stack = []


        for i in range(len(T)):
            while stack:
                if T[stack[-1]] < T[i]:
                   current_position = stack.pop()
                   result[current_position] = (i-current_position)

                else:
                    stack.append(i)
                    break
            stack.append(i)

        return result

print(Solution.dailyTemperatures(Solution,T))