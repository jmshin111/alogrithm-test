from typing import List






gas = [5,8,2,8]
cost = [6,5,6,6]
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

gas = [2, 3, 4]
cost = [3, 4, 3]

gas = [3,1,1]
cost = [1,2,2]


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        print(gas)
        rest_fuel = []
        for i in range(len(gas)):
            rest_fuel.append([gas[i] - cost[i], i])

        rest_fuel_sorted = sorted(rest_fuel, key=lambda x: x[0], reverse=True)

        start = -1
        founded = False
        for i in rest_fuel_sorted:

            start = i[1]

            sum = 0
            if (rest_fuel[start][0] < 0):
                start = -1
                break
            for j in range(len(gas)):
                index = (start + j) % len(gas)
                sum += rest_fuel[index][0]
                if (sum < 0):
                    start = -1
                    break

            if(sum>=0):
                founded = True
            if(founded):
                break
        print(rest_fuel)

        return start


print(Solution.canCompleteCircuit(Solution, gas, cost))
