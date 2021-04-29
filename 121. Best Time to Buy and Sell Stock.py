from typing import List

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = -1
        max_profit = -1
        index = len(prices)-1
        while True:
            if(index ==-1):
                break
            max_price = max(prices[index],max_price)
            max_profit = max( abs(prices[index]-max_price) ,max_profit)

            index -= 1
        return max_profit


print(Solution.maxProfit(Solution,prices))