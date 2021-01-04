from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        start = 0
        end = 0
        buying = False

        for i in range(len(prices)-1):
            if(not buying and prices[i] < prices[i+1]):
                start = i
                buying = True
            if(buying and prices[i] > prices[i+1] ):
                end = i
                buying = False
                max_profit += prices[end]-prices[start]
        if buying:
            max_profit += prices[len(prices)-1] - prices[start]
        return max_profit

prices = [7,1,5,3,6,4]
#Output: 7

print(Solution.maxProfit(Solution,prices), 7)

prices = [1,2,3,4,5]
#Output: 4
print(Solution.maxProfit(Solution,prices), 4)

prices = [7,6,4,3,1]
#Output: 0

print(Solution.maxProfit(Solution,prices), 0)


