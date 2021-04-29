from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
class Solution:
    def trap(self, height: List[int]) -> int:

        sum = 0
        p1 = 0
        p2 = 0
        while p1<len(height) and p2 <len(height):

            start_height = height[p1]
            p2 += 1
            while(p2<=len(height)-1 and height[p2]<=start_height):
                p2 +=1

            while(p1 != p2):
                one_width = height[p1] - height[p2-1]
                if(one_width>0):
                    sum += one_width
                p1 += 1

            p1 = p2
            print(sum)
        return sum

print(Solution.trap(Solution,height))



