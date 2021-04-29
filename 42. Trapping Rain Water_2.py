from typing import List


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

height = [4,2,3]
class Solution:
    def trap(self, height: List[int]) -> int:

        sum = 0
        p1 = 0
        p2 = len(height)-1

        while(p1<len(height)):
            start_height_index = p1
            if(p1 != p2 and height[p1] <= height[p2]):
                while(height[p1]<=height[p2]):
                    p1 +=1
                    if(height[start_height_index]<= height[p1]):
                        break
                    sum += height[start_height_index] - height[p1]
                    #print(sum,p1,p2)
            else:
                if(p1 == p2 and p1<len(height)):
                    p1 +=1
                    p2 = len(height)-1
                    continue
                p2 -=1

        return sum

print(Solution.trap(Solution,height))



